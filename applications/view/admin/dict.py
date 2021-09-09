from flask import Blueprint, render_template, request, jsonify

from applications.common import curd
from applications.common.helper import ModelFilter
from applications.common.utils.http import table_api, success_api, fail_api
from applications.common.utils.rights import authorize
from applications.common.utils.validate import xss_escape
from applications.extensions import db
from applications.models import DictType, DictData
from applications.schemas import DictTypeSchema, DictDataSchema

admin_dict = Blueprint('adminDict', __name__, url_prefix='/admin/dict')


# 数据字典
@admin_dict.get('/')
@authorize("admin:dict:main", log=True)
def main():
    return render_template('admin/dict/main.html')


@admin_dict.get('/dictType/data')
@authorize("admin:dict:main", log=True)
def dict_type_data():
    # 获取请求参数
    type_name = xss_escape(request.args.get('typeName', type=str))
    # 查询参数构造
    mf = ModelFilter()
    if type_name:
        mf.vague(field_name="type_name", value=type_name)
    # orm查询
    # 使用分页获取data需要.items
    dict_all = DictType.query.filter(mf.get_filter(DictType)).layui_paginate()
    count = DictType.query.filter(mf.get_filter(DictType)).count()
    data = curd.model_to_dicts(schema=DictTypeSchema, data=dict_all.items)
    return table_api(data=data, count=count)


@admin_dict.get('/dictType/add')
@authorize("admin:dict:add", log=True)
def dict_type_add():
    return render_template('admin/dict/add.html')


@admin_dict.post('/dictType/save')
@authorize("admin:dict:add", log=True)
def dict_type_save():
    req_json = request.json
    description = xss_escape(req_json.get("description"))
    enable = xss_escape(req_json.get("enable"))
    type_code = xss_escape(req_json.get("typeCode"))
    type_name = xss_escape(req_json.get("typeName"))
    d = DictType(type_name=type_name, type_code=type_code, enable=enable, description=description)
    db.session.add(d)
    db.session.commit()
    if d.id is None:
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
        res = curd.enable_status(DictType,_id)
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
        res = curd.disable_status(DictType,_id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api("禁用成功")
    return fail_api(msg="数据错误")


# 删除字典类型
@admin_dict.delete('/dictType/remove/<int:_id>')
@authorize("admin:dict:remove", log=True)
def dict_type_delete(_id):
    res = curd.delete_one_by_id(DictType,_id)
    if not res:
        return fail_api(msg="删除失败")
    return success_api(msg="删除成功")


@admin_dict.get('/dictData/data')
@authorize("admin:dict:main", log=True)
def dict_code_data():
    type_code = xss_escape(request.args.get('typeCode', type=str))
    dict_data = DictData.query.filter_by(type_code=type_code).layui_paginate()
    count = DictType.query.count()
    data = curd.model_to_dicts(schema=DictDataSchema, data=dict_data.items)
    return table_api(data=data, count=count)


# 增加字典数据
@admin_dict.get('/dictData/add')
@authorize("admin:dict:add", log=True)
def dict_data_add():
    type_code = request.args.get('typeCode', type=str)
    return render_template('admin/dict/data/add.html', type_code=type_code)


# 增加字典数据
@admin_dict.post('/dictData/save')
@authorize("admin:dict:add", log=True)
def dict_data_save():
    req_json = request.json
    data_label = xss_escape(req_json.get("dataLabel"))
    data_value = xss_escape(req_json.get("dataValue"))
    enable = xss_escape(req_json.get("enable"))
    remark = xss_escape(req_json.get("remark"))
    type_code = xss_escape(req_json.get("typeCode"))
    d = DictData(data_label=data_label, data_value=data_value, enable=enable, remark=remark, type_code=type_code)
    db.session.add(d)
    db.session.commit()
    if not d.id:
        return jsonify(success=False, msg="增加失败")
    return jsonify(success=True, msg="增加成功")


#  编辑字典数据
@admin_dict.get('/dictData/edit')
@authorize("admin:dict:edit", log=True)
def dict_data_edit():
    _id = request.args.get('dataId', type=str)
    dict_data = curd.get_one_by_id(DictData, _id)
    return render_template('admin/dict/data/edit.html', dict_data=dict_data)


#  编辑字典数据
@admin_dict.put('/dictData/update')
@authorize("admin:dict:edit", log=True)
def dict_data_update():
    req_json = request.json
    id = req_json.get("dataId")
    DictData.query.filter_by(id=id).update({
        "data_label": xss_escape(req_json.get("dataLabel")),
        "data_value": xss_escape(req_json.get("dataValue")),
        "enable": xss_escape(req_json.get("enable")),
        "remark": xss_escape(req_json.get("remark")),
        "type_code": xss_escape(req_json.get("typeCode"))
    })
    db.session.commit()
    return success_api(msg="更新成功")


# 启用字典数据
@admin_dict.put('/dictData/enable')
@authorize("admin:dict:edit", log=True)
def dict_data_enable():
    _id = request.json.get('dataId')
    if _id:
        res = curd.enable_status(model=DictData, id=_id)
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
        res = curd.disable_status(model=DictData, id=_id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="禁用成功")
    return fail_api(msg="数据错误")


# 删除字典类型
@admin_dict.delete('dictData/remove/<int:id>')
@authorize("admin:dict:remove", log=True)
def dict_data_delete(id):
    res = curd.delete_one_by_id(model=DictData, id=id)
    if not res:
        return fail_api(msg="删除失败")
    return success_api(msg="删除成功")
