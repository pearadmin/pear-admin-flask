from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required

from applications.service.admin.role import get_role_data_dict, add_role, get_role_power, update_role_power, \
    get_role_by_id, update_role, remove_role, batch_remove
from applications.service.route_auth import authorize_and_log

admin_role = Blueprint('adminRole', __name__, url_prefix='/admin/role')


# 用户管理
@admin_role.route('/')
@authorize_and_log("admin:role:main")
def main():
    return render_template('admin/role/main.html')


# 表格数据
@admin_role.route('/data')
@authorize_and_log("admin:role:main")
def table():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    roleName = request.args.get('roleName', type=str)
    roleCode = request.args.get('roleCode', type=str)
    filters = {}
    if roleName:
        filters["name"] = ('%' + roleName + '%')
    if roleCode:
        filters["code"] = ('%' + roleCode + '%')
    data, count = get_role_data_dict(page=page, limit=limit, filters=filters)
    res = {
        'msg': "",
        'code': 0,
        'data': data,
        'count': count,
        'limit': "10"

    }
    return jsonify(res)


# 角色增加
@admin_role.route('/add')
@authorize_and_log("admin:role:add")
@login_required
def add():
    return render_template('admin/role/add.html')


# 角色增加
@admin_role.route('/save', methods=['POST'])
@authorize_and_log("admin:role:add")
def save():
    req = request.json
    add_role(req=req)
    return jsonify(msg="成功", success=True)


# 角色授权
@admin_role.route('/power/<int:id>')
@authorize_and_log("admin:role:power")
def power(id):
    return render_template('admin/role/power.html', id=id)


# 获取角色权限
@admin_role.route('/getRolePower/<int:id>')
@authorize_and_log("admin:role:main")
def getRolePower(id):
    powers = get_role_power(id)
    res = {
        "data": powers,
        "status": {"code": 200, "message": "默认"}
    }
    return jsonify(res)


# 保存角色权限
@admin_role.route('/saveRolePower', methods=['PUT'])
@authorize_and_log("admin:role:edit")
def saveRolePower():
    req_form = request.form
    powerIds = req_form.get("powerIds")
    power_list = powerIds.split(',')
    roleId = req_form.get("roleId")
    update_role_power(id=roleId, power_list=power_list)
    return jsonify(success=True, msg="授权成功")


# 角色编辑
@admin_role.route('/edit/<int:id>', methods=['GET', 'POST'])
@authorize_and_log("admin:role:edit")
def edit(id):
    role = get_role_by_id(id)
    return render_template('admin/role/edit.html', role=role)


# 更新角色
@admin_role.route('/update', methods=['PUT'])
@authorize_and_log("admin:role:edit")
def update():
    res = update_role(request.json)
    if not res:
        return jsonify(success=False, msg="更新角色失败")
    return jsonify(success=True, msg="更新角色成功")


@admin_role.route('/remove/<int:id>', methods=['DELETE'])
@authorize_and_log("admin:role:remove")
def remove(id):
    res = remove_role(id)
    if not res:
        return jsonify(success=False, msg="角色删除失败")
    return jsonify(success=True, msg="角色删除成功")


# 批量删除
@admin_role.route('/batchRemove', methods=['DELETE'])
@authorize_and_log("admin:role:remove")
@login_required
def batchRemove():
    ids = request.form.getlist('ids[]')
    batch_remove(ids)
    return jsonify(success=True,msg="批量删除成功")
