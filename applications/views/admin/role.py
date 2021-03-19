from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required

from applications.service.admin.role import get_role_data_dict, add_role, get_role_power, update_role_power, \
    get_role_by_id, update_role

admin_role = Blueprint('adminRole', __name__, url_prefix='/admin/role')


# 用户管理
@admin_role.route('/')
@login_required
def index():
    return render_template('admin/role/main.html')


# 表格数据
@admin_role.route('/data')
@login_required
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
@login_required
def add():
    return render_template('admin/role/add.html')


# 角色增加
@admin_role.route('/save', methods=['POST'])
@login_required
def save():
    req = request.json
    add_role(req=req)
    return jsonify(msg="成功", success=True)


# 角色授权
@admin_role.route('/power/<int:id>')
def power(id):
    return render_template('admin/role/power.html', id=id)


# 获取角色权限
@admin_role.route('/getRolePower/<int:id>')
def getRolePower(id):
    powers = get_role_power(id)
    res = {
        "data": powers,
        "status": {"code": 200, "message": "默认"}
    }
    return jsonify(res)


# 保存角色权限
@admin_role.route('/saveRolePower', methods=['PUT'])
def saveRolePower():
    req_form = request.form
    powerIds = req_form.get("powerIds")
    power_list = powerIds.split(',')
    roleId = req_form.get("roleId")
    update_role_power(id=roleId, power_list=power_list)
    return jsonify(success=True, msg="授权成功")


# 角色编辑
@admin_role.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    role = get_role_by_id(id)
    return render_template('admin/role/edit.html', role=role)


# 更新角色
@admin_role.route('/update', methods=['PUT'])
def update():
    res = update_role(request.json)
    if not res:
        return jsonify(success=False, msg="更新角色失败")
    return jsonify(success=True, msg="更新角色成功")

# 批量删除
# @admin_user.route('/batchRemove', methods=['GET', 'POST'])
# @login_required
# def batchRemove():
#     ids = request.form.getlist('ids[]')
#     res = batch_remove(ids)
#     return res
