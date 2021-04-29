from flask import Blueprint, render_template, request, jsonify

from applications.models.admin_dict import DictType, DictData
from applications.service.admin.dict import get_dict_type, get_dict_data, save_dict_type, save_dict_data, \
    delete_type_by_id, delete_data_by_id, update_dict_type, enable_dict_type_status, disable_dict_type_status, \
    enable_dict_data_status, disable_dict_data_status, update_dict_data
from applications.service.common.response import table_api, success_api, fail_api
from applications.service.route_auth import authorize_and_log

admin_dict = Blueprint('adminDict', __name__, url_prefix='/admin/dict')


# 数据字典
@admin_dict.route('/')
@authorize_and_log("admin:dict:main")
def main():
    return render_template('admin/dict/main.html')


@admin_dict.route('/dictType/data')
@authorize_and_log("admin:dict:main")
def dictType_data():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    type_name = request.args.get('typeName', type=str)
    data, count = get_dict_type(page=page, limit=limit, type_name=type_name)
    return table_api(data=data,count=count)


@admin_dict.route('/dictType/add')
@authorize_and_log("admin:dict:add")
def dictType_add():
    return render_template('admin/dict/add.html')


@admin_dict.route('/dictType/save', methods=['POST'])
@authorize_and_log("admin:dict:add")
def dictType_save():
    req_json = request.json
    res = save_dict_type(req_json=req_json)
    if res == None:
        return fail_api(msg="增加失败")
    return success_api(msg="增加成功")


#  编辑字典类型
@admin_dict.route('/dictType/edit', methods=['GET', 'POST'])
@authorize_and_log("admin:dict:edit")
def dictType_edit():
    id = request.args.get('dictTypeId', type=str)
    dict_type = DictType.query.filter_by(id=id).first()
    return render_template('admin/dict/edit.html', dict_type=dict_type)


#  编辑字典类型
@admin_dict.route('/dictType/update', methods=['PUT'])
@authorize_and_log("admin:dict:edit")
def dictType_update():
    req_json = request.json
    update_dict_type(req_json)
    return success_api(msg="更新成功")


# 启用字典
@admin_dict.route('/dictType/enable', methods=['PUT'])
@authorize_and_log("admin:dict:edit")
def dictType_enable():
    id = request.json.get('id')
    if id:
        res = enable_dict_type_status(id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api("启动成功")
    return fail_api(msg="数据错误")


# 禁用字典
@admin_dict.route('/dictType/disable', methods=['PUT'])
@authorize_and_log("admin:dict:edit")
def dictType_disenable():
    id = request.json.get('id')
    if id:
        res = disable_dict_type_status(id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api("禁用成功")
    return fail_api(msg="数据错误")


# 删除字典类型
@admin_dict.route('/dictType/remove/<int:id>', methods=['DELETE'])
@authorize_and_log("admin:dict:remove")
def dictType_delete(id):
    res = delete_type_by_id(id)
    if not res:
        return fail_api(msg="删除失败")
    return success_api(msg="删除成功")


@admin_dict.route('/dictData/data')
@authorize_and_log("admin:dict:main")
def dictCode_data():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    type_code = request.args.get('typeCode', type=str)
    data, count = get_dict_data(page=page, limit=limit, type_code=type_code)
    return table_api(data=data,count=count)


# 增加字典数据
@admin_dict.route('/dictData/add')
@authorize_and_log("admin:dict:add")
def dictData_add():
    type_code = request.args.get('typeCode', type=str)
    return render_template('admin/dict/data/add.html', type_code=type_code)


# 增加字典数据
@admin_dict.route('/dictData/save', methods=['POST'])
@authorize_and_log("admin:dict:add")
def dictData_save():
    req_json = request.json
    res = save_dict_data(req_json=req_json)
    if res == None:
        return jsonify(success=False, msg="增加失败")
    return jsonify(success=True, msg="增加成功")


#  编辑字典数据
@admin_dict.route('/dictData/edit', methods=['GET', 'POST'])
@authorize_and_log("admin:dict:edit")
def dictData_edit():
    id = request.args.get('dataId', type=str)
    dict_data = DictData.query.filter_by(id=id).first()
    return render_template('admin/dict/data/edit.html', dict_data=dict_data)


#  编辑字典数据
@admin_dict.route('/dictData/update', methods=['PUT'])
@authorize_and_log("admin:dict:edit")
def dictData_update():
    req_json = request.json
    update_dict_data(req_json)
    return success_api(msg="更新成功")


# 启用字典数据
@admin_dict.route('/dictData/enable', methods=['PUT'])
@authorize_and_log("admin:dict:edit")
def dictData_enable():
    id = request.json.get('dataId')
    if id:
        res = enable_dict_data_status(id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="启动成功")
    return fail_api(msg="数据错误")


# 禁用字典数据
@admin_dict.route('/dictData/disable', methods=['PUT'])
@authorize_and_log("admin:dict:edit")
def dictData_disenable():
    id = request.json.get('dataId')
    if id:
        res = disable_dict_data_status(id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="禁用成功")
    return fail_api(msg="数据错误")


# 删除字典类型
@admin_dict.route('dictData/remove/<int:id>', methods=['DELETE'])
@authorize_and_log("admin:dict:remove")
def dictData_delete(id):
    res = delete_data_by_id(id)
    if not res:
        return fail_api(msg="删除失败")
    return success_api(msg="删除成功")
