from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from applications.models.admin import User, Role
from applications.service.admin.user import get_user_data_dict, add_user, delete_by_id, \
    batch_remove, update_user, update_user_role, is_user_exists, add_user_role, enable_status, disable_status
from applications.service.route_auth import authorize_and_log

admin_user = Blueprint('adminUser', __name__, url_prefix='/admin/user')


# 用户管理
@admin_user.route('/')
@authorize_and_log("admin:user:main")
def main():
    return render_template('admin/user/main.html')


#   用户分页查询
@admin_user.route('/data')
@authorize_and_log("admin:user:main")
def data():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    realName = request.args.get('realName', type=str)
    username = request.args.get('username', type=str)
    filters = {}
    if realName:
        filters["realname"] = ('%' + realName + '%')
    if username:
        filters["username"] = ('%' + username + '%')
    data, count = get_user_data_dict(page=page, limit=limit, filters=filters)
    res = {
        'msg': "",
        'code': 0,
        'data': data,
        'count': count,
        'limit': "10"

    }
    return jsonify(res)


# 用户增加
@admin_user.route('/add')
@authorize_and_log("admin:user:add")
def add():
    roles = Role.query.all()
    return render_template('admin/user/add.html', roles=roles)


@admin_user.route('/save', methods=['POST'])
@authorize_and_log("admin:user:add")
def save():
    req_json = request.json
    a = req_json.get("roleIds")
    username = req_json.get('username')
    realName = req_json.get('realName')
    password = req_json.get('password')
    role_ids = a.split(',')

    if not username or not realName or not password:
        return jsonify(success=False, msg="账号姓名密码不得为空")

    if is_user_exists(username):
        return jsonify(success=False, msg="用户已经存在")

    id = add_user(username, realName, password)
    add_user_role(id, role_ids)

    return jsonify(success=True, msg="增加成功")


# 删除用户
@admin_user.route('/remove/<int:id>', methods=['DELETE'])
@authorize_and_log("admin:user:remove")
def delete(id):
    res = delete_by_id(id)
    if not res:
        return jsonify(msg="删除失败", success=False)
    return jsonify(msg="删除成功", success=True)


#  编辑用户
@admin_user.route('/edit/<int:id>', methods=['GET', 'POST'])
@authorize_and_log("admin:user:edit")
def edit(id):
    user = User.query.filter_by(id=id).first()
    roles = Role.query.all()
    checked_roles = []
    for r in user.role:
        checked_roles.append(r.id)
    return render_template('admin/user/edit.html', user=user, roles=roles, checked_roles=checked_roles)

#  编辑用户
@admin_user.route('/update', methods=['PUT'])
@authorize_and_log("admin:user:edit")
def update():
    req_json = request.json
    a = req_json.get("roleIds")
    id = req_json.get("userId")
    username = req_json.get('username')
    realName = req_json.get('realName')
    role_ids = a.split(',')
    update_user(id, username, realName)
    update_user_role(id, role_ids)
    return jsonify(success=True, msg="更新成功")


# 启用用户
@admin_user.route('/enable', methods=['PUT'])
@authorize_and_log("admin:user:edit")
def enable():
    id = request.json.get('userId')
    print(id)
    if id:
        res = enable_status(id)
        if not res:
            return jsonify(msg="出错啦", success=False)
        return jsonify(msg="启动成功", success=True)
    return jsonify(msg="数据错误", success=False)


# 禁用用户
@admin_user.route('/disable', methods=['PUT'])
@authorize_and_log("admin:user:edit")
def disenable():
    id = request.json.get('userId')
    print(id)
    if id:
        res = disable_status(id)
        if not res:
            return jsonify(msg="出错啦", success=False)
        return jsonify(msg="禁用成功", success=True)
    return jsonify(msg="数据错误", success=False)


# 批量删除
@admin_user.route('/batchRemove', methods=['DELETE'])
@authorize_and_log("admin:user:remove")
def batchRemove():
    ids = request.form.getlist('ids[]')
    batch_remove(ids)
    return jsonify(success=True, msg="批量删除成功")

