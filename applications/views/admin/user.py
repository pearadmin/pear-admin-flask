from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from applications.models import db
from applications.models.admin import User, Role
from applications.service.admin.user import get_user_data_dict, get_user_by_name, add_user, delete_by_id, update_status, \
    batch_remove, update_user, update_user_role, is_user_exists

admin_user = Blueprint('adminUser', __name__, url_prefix='/admin/user')


# 用户管理
@admin_user.route('/')
@login_required
def index():
    return render_template('admin/user/main.html')


#   用户 分页查询
@admin_user.route('/data')
@login_required
def data():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    data, count = get_user_data_dict(page=page, limit=limit)
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
def add():
    roles = Role.query.all()
    return render_template('admin/user/add.html', roles=roles)


@admin_user.route('/save', methods=['POST'])
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

    add_user(username, realName, password)
    return jsonify(success=True, msg="增加成功")


# @admin_user.route('/add', methods=['GET', 'POST'])
# @login_required
# def insert():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         role = request.form.get('role')
#         if username and password and role:
#             if get_user_by_name(username=username) is None:
#                 add_user(username=username, password=password)
#                 return jsonify(msg="添加成功", code=200)
#             else:
#                 return jsonify(msg="用户已经存在", code=999)
#         else:
#             return jsonify(msg="用户名密码角色不能为空", code=999)
#
#     else:
#         role = ['管理员', '普通用户']
#         return render_template('admin/user_add.html', role=role)


#                               ==========================================================
#                                                            删除用户
#                               ==========================================================


@admin_user.route('/remove/<int:id>', methods=['DELETE'])
@login_required
def delete(id):
    user = delete_by_id(id)
    db.session.commit()
    if user:
        return jsonify(msg="删除成功", success=True)
    else:
        return jsonify(msg="删除失败", success=False)


#  编辑用户
@admin_user.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    user = User.query.filter_by(id=id).first()
    roles = Role.query.all()
    checked_roles = []
    for r in user.role:
        checked_roles.append(r.id)
    return render_template('admin/user/edit.html', user=user, roles=roles, checked_roles=checked_roles)
    #
    # if request.method == 'POST':
    #     username = request.form.get('username')
    #     password = request.form.get('password')
    #     role = request.form.get('role')
    #     if username and role:
    #         if password is None:
    #             if User.query.filter_by(id=id).first() is not None:
    #                 update_user(id, username)
    #                 return jsonify(msg="修改成功", code=200)
    #
    #             else:
    #                 res = {"msg": "用户已经存在", "code": 200}
    #                 return jsonify(res)
    #         else:
    #             user = User.query.filter_by(id=id).first()
    #             if user is not None:
    #                 User.query.filter_by(id=id).update({'username': username, 'role': role})
    #                 user.set_password(password)
    #                 db.session.commit()
    #                 return jsonify(msg="修改成功", code=200)
    #             else:
    #                 return jsonify(msg="用户不存在", code=200)
    #
    #     else:
    #
    #         return jsonify(msg="用户名密码角色不能为空", code=999)
    # else:
    #     user = User.query.filter_by(id=id).first()
    #     roles = Role.query.all()
    #     checked_roles = []
    #     for r in user.role:
    #         checked_roles.append(r.id)
    #     return render_template('admin/user/edit.html', user=user, roles=roles, checked_roles=checked_roles)


@admin_user.route('/update', methods=['PUT'])
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


# 更新用户状态
# @admin_user.route('/update/status', methods=['POST'])
# @login_required
# def ustatus():
#     id = request.form.get('id')
#     status = request.form.get('status')
#     if id and status:
#         res = update_status(status=status)
#         return res
#     return jsonify(msg="出错啦", code=999)


# 批量删除
@admin_user.route('/batchRemove', methods=['GET', 'POST'])
@login_required
def batchRemove():
    ids = request.form.getlist('ids[]')
    res = batch_remove(ids)
    return res
