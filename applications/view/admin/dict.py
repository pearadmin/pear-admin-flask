from flask import Blueprint, render_template, request, jsonify
from applications.common.utils.http import table_api, success_api, fail_api
from applications.common.utils.rights import authorize
from applications.common.utils.validate import xss_escape
from applications.models import DictType, DictData
from applications.common.admin import dict_curd

admin_dict = Blueprint('adminDict', __name__, url_prefix='/admin/dict')


# 数据字典
@admin_dict.get('/')
@authorize("admin:dict:main", log=True)
def main():
    return render_template('admin/dict/main.html')


@admin_dict.get('/dictType/data')
@authorize("admin:dict:main", log=True)
def dict_type_data():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    type_name = xss_escape(request.args.get('typeName', type=str))
    data, count = dict_curd.get_dict_type(page=page, limit=limit, type_name=type_name)
    return table_api(data=data,count=count)


@admin_dict.get('/dictType/add')
@authorize("admin:dict:add", log=True)
def dict_type_add():
    return render_template('admin/dict/add.html')


@admin_dict.post('/dictType/save')
@authorize("admin:dict:add", log=True)
def dict_type_save():
    req_json = request.json
    res = dict_curd.save_dict_type(req_json=req_json)
    if res is None:
        return fail_api(msg="增加失败")
    return success_api(msg="增加成功")


#  编辑字典类型
@admin_dict.get('/dictType/edit')
@authorize("admin:dict:edit", log=True)
def dict_type_edit():
    _id = request.args.get('dictTypeId', type=int)
    dict_type = DictType.query.filter_by(id=_id).first()
    return render_template('admin/dict/edit.html', dict_type=dict_type)


#  编辑字典类型
@admin_dict.put('/dictType/update')
@authorize("admin:dict:edit", log=True)
def dict_type_update():
    req_json = request.json
    dict_curd.update_dict_type(req_json)
    return success_api(msg="更新成功")


# 启用字典
@admin_dict.put('/dictType/enable')
@authorize("admin:dict:edit", log=True)
def dict_type_enable():
    _id = request.json.get('id')
    if id:
        res = dict_curd.enable_dict_type_status(_id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api("启动成功")
    return fail_api(msg="数据错误")


# 禁用字典
@admin_dict.put('/dictType/disable')
@authorize("admin:dict:edit", log=True)
def dict_type_dis_enable():
    _id = request.json.get('id')
    if id:
        res = dict_curd.disable_dict_type_status(_id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api("禁用成功")
    return fail_api(msg="数据错误")


# 删除字典类型
@admin_dict.delete('/dictType/remove/<int:_id>')
@authorize("admin:dict:remove", log=True)
def dict_type_delete(_id):
    res = dict_curd.delete_type_by_id(_id)
    if not res:
        return fail_api(msg="删除失败")
    return success_api(msg="删除成功")


@admin_dict.get('/dictData/data')
@authorize("admin:dict:main", log=True)
def dict_code_data():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    type_code = xss_escape(request.args.get('typeCode', type=str))
    data, count = dict_curd.get_dict_data(page=page, limit=limit, type_code=type_code)
    return table_api(data=data,count=count)


# 增加字典数据
@admin_dict.get('/dictData/add')
@authorize("admin:dict:add", log=True)
def dict_data_add():
    type_code = request.args.get('typeCode', type=str)
    return render_template('admin/dict/data/add.html', type_code=type_code)


# 增加字典数据
@admin_dict.get('/dictData/save')
@authorize("admin:dict:add", log=True)
def dict_data_save():
    req_json = request.json
    res = dict_curd.save_dict_data(req_json=req_json)
    if not res:
        return jsonify(success=False, msg="增加失败")
    return jsonify(success=True, msg="增加成功")


#  编辑字典数据
@admin_dict.get('/dictData/edit')
@authorize("admin:dict:edit", log=True)
def dict_data_edit():
    _id = request.args.get('dataId', type=str)
    dict_data = DictData.query.filter_by(id=_id).first()
    return render_template('admin/dict/data/edit.html', dict_data=dict_data)


#  编辑字典数据
@admin_dict.put('/dictData/update')
@authorize("admin:dict:edit", log=True)
def dict_data_update():
    req_json = request.json
    dict_curd.update_dict_data(req_json)
    return success_api(msg="更新成功")


# 启用字典数据
@admin_dict.put('/dictData/enable')
@authorize("admin:dict:edit", log=True)
def dict_data_enable():
    _id = request.json.get('dataId')
    if _id:
        res = dict_curd.enable_dict_data_status(_id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="启动成功")
    return fail_api(msg="数据错误")


# 禁用字典数据
@admin_dict.put('/dictData/disable')
@authorize("admin:dict:edit", log=True)
def dict_data_disenable():
    _id = request.json.get('dataId')
    if _id:
        res = dict_curd.disable_dict_data_status(_id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="禁用成功")
    return fail_api(msg="数据错误")


# 删除字典类型
@admin_dict.delete('dictData/remove/<int:id>')
@authorize("admin:dict:remove", log=True)
def dict_data_delete(id):
    res = dict_curd.delete_data_by_id(id)
    if not res:
        return fail_api(msg="删除失败")
    return success_api(msg="删除成功")
