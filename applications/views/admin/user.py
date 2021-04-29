from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from applications.models.admin_user import User
from applications.models.admin_role import Role
from applications.service.admin.user import get_user_data_dict, add_user, delete_by_id, \
    batch_remove, update_user, update_user_role, is_user_exists, add_user_role, enable_status, disable_status, \
    edit_password, get_current_user_logs, update_current_user_info, update_avatar
from applications.service.common.response import table_api, fail_api, success_api
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
    user_data, count = get_user_data_dict(page=page, limit=limit, filters=filters)
    return table_api(data=user_data, count=count)


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
        return fail_api(msg="账号姓名密码不得为空")

    if is_user_exists(username):
        return fail_api(msg="用户已经存在")

    id = add_user(username, realName, password)
    add_user_role(id, role_ids)

    return success_api(msg="增加成功")


# 删除用户
@admin_user.route('/remove/<int:id>', methods=['DELETE'])
@authorize_and_log("admin:user:remove")
def delete(id):
    res = delete_by_id(id)
    if not res:
        return fail_api(msg="删除失败")
    return success_api(msg="删除成功")


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
    return success_api(msg="更新成功")


# 个人中心
@admin_user.route('/center')
@login_required
def center():
    user_info = current_user
    user_logs = get_current_user_logs()
    return render_template('admin/user/center.html', user_info=user_info, user_logs=user_logs)


# 修改头像
@admin_user.route('/profile')
@login_required
def profile():
    return render_template('admin/user/profile.html')


# 修改头像
@admin_user.route('/updateAvatar', methods=['PUT'])
@login_required
def updateAvatar():
    url = request.json.get("avatar").get("src")
    if not update_avatar(url):
        return fail_api(msg="出错啦")
    return success_api(msg="修改成功")


# 修改当前用户信息
@admin_user.route('/updateInfo', methods=['PUT'])
@login_required
def updateInfo():
    res_json = request.json
    if not update_current_user_info(req_json=res_json):
        return fail_api(msg="出错啦")
    return success_api(msg="更新成功")


# 修改当前用户密码
@admin_user.route('/editPassword', methods=['GET'])
@login_required
def editPassword():
    return render_template('admin/user/edit_password.html')


# 修改当前用户密码
@admin_user.route('/editPassword', methods=['PUT'])
@login_required
def edit_password_put():
    res_json = request.json
    return edit_password(res_json=res_json)


# 启用用户
@admin_user.route('/enable', methods=['PUT'])
@authorize_and_log("admin:user:edit")
def enable():
    id = request.json.get('userId')
    print(id)
    if id:
        res = enable_status(id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="启动成功")
    return fail_api(msg="数据错误")


# 禁用用户
@admin_user.route('/disable', methods=['PUT'])
@authorize_and_log("admin:user:edit")
def disenable():
    id = request.json.get('userId')
    if id:
        res = disable_status(id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="禁用成功")
    return fail_api(msg="数据错误")


# 批量删除
@admin_user.route('/batchRemove', methods=['DELETE'])
@authorize_and_log("admin:user:remove")
def batchRemove():
    ids = request.form.getlist('ids[]')
    batch_remove(ids)
    return success_api(msg="批量删除成功")
