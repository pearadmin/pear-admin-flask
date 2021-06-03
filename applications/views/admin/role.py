from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from applications.service.admin import role_curd
from applications.service.common.response import table_api, success_api, fail_api
from applications.service.common.validate import xss_escape
from applications.service.route_auth import authorize

admin_role = Blueprint('adminRole', __name__, url_prefix='/admin/role')


# 用户管理
@admin_role.route('/')
@authorize("admin:role:main", log=True)
def main():
    return render_template('admin/role/main.html')


# 表格数据
@admin_role.route('/data')
@authorize("admin:role:main", log=True)
def table():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    roleName = xss_escape(request.args.get('roleName', type=str))
    roleCode = xss_escape(request.args.get('roleCode', type=str))
    filters = {}
    if roleName:
        filters["name"] = ('%' + roleName + '%')
    if roleCode:
        filters["code"] = ('%' + roleCode + '%')
    data, count = role_curd.get_role_data_dict(page=page, limit=limit, filters=filters)
    return table_api(data=data, count=count)


# 角色增加
@admin_role.route('/add')
@authorize("admin:role:add", log=True)
@login_required
def add():
    return render_template('admin/role/add.html')


# 角色增加
@admin_role.route('/save', methods=['POST'])
@authorize("admin:role:add", log=True)
def save():
    req = request.json
    role_curd.add_role(req=req)
    return success_api(msg="成功")


# 角色授权
@admin_role.route('/power/<int:id>')
@authorize("admin:role:power", log=True)
def power(id):
    return render_template('admin/role/power.html', id=id)


# 获取角色权限
@admin_role.route('/getRolePower/<int:id>')
@authorize("admin:role:main", log=True)
def getRolePower(id):
    powers = role_curd.get_role_power(id)
    res = {
        "data": powers,
        "status": {"code": 200, "message": "默认"}
    }
    return jsonify(res)


# 保存角色权限
@admin_role.route('/saveRolePower', methods=['PUT'])
@authorize("admin:role:edit", log=True)
def saveRolePower():
    req_form = request.form
    powerIds = req_form.get("powerIds")
    power_list = powerIds.split(',')
    roleId = req_form.get("roleId")
    role_curd.update_role_power(id=roleId, power_list=power_list)
    return success_api(msg="授权成功")


# 角色编辑
@admin_role.route('/edit/<int:id>', methods=['GET', 'POST'])
@authorize("admin:role:edit", log=True)
def edit(id):
    role = role_curd.get_role_by_id(id)
    return render_template('admin/role/edit.html', role=role)


# 更新角色
@admin_role.route('/update', methods=['PUT'])
@authorize("admin:role:edit", log=True)
def update():
    res = role_curd.update_role(request.json)
    if not res:
        return fail_api(msg="更新角色失败")
    return success_api(msg="更新角色成功")


# 启用用户
@admin_role.route('/enable', methods=['PUT'])
@authorize("admin:role:edit", log=True)
def enable():
    id = request.json.get('roleId')
    # print(id)
    if id:
        res = role_curd.enable_status(id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="启动成功")
    return fail_api(msg="数据错误")


# 禁用用户
@admin_role.route('/disable', methods=['PUT'])
@authorize("admin:role:edit", log=True)
def disenable():
    id = request.json.get('roleId')
    if id:
        res = role_curd.disable_status(id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="禁用成功")
    return fail_api(msg="数据错误")


# 角色删除
@admin_role.route('/remove/<int:id>', methods=['DELETE'])
@authorize("admin:role:remove", log=True)
def remove(id):
    res = role_curd.remove_role(id)
    if not res:
        return fail_api(msg="角色删除失败")
    return success_api(msg="角色删除成功")


# 批量删除
@admin_role.route('/batchRemove', methods=['DELETE'])
@authorize("admin:role:remove", log=True)
@login_required
def batchRemove():
    ids = request.form.getlist('ids[]')
    role_curd.batch_remove(ids)
    return success_api(msg="批量删除成功")
