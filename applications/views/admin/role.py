from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required

from applications.service.admin.role import get_role_data_dict, add_role, get_role_power, update_role_power

admin_role = Blueprint('adminRole', __name__, url_prefix='/admin/role')


# 用户管理
@admin_role.route('/')
@login_required
def index():
    return render_template('admin/role/main.html')


# @admin_role.route('/test')
# @login_required
# def test():
#     return jsonify(current_user.role)

#   用户 分页查询


@admin_role.route('/data')
@login_required
def table():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    data, count = get_role_data_dict(page=page, limit=limit)
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


@admin_role.route('/save', methods=['POST'])
@login_required
def save():
    req = request.json
    add_role(req=req)
    return jsonify(msg="成功", success=True)


@admin_role.route('/power/<int:id>')
def power(id):
    return render_template('admin/role/power.html', id=id)


@admin_role.route('/getRolePower/<int:id>')
def getRolePower(id):
    powers = get_role_power(id)
    res = {
        "data": powers,
        "status":{"code": 200, "message": "默认"}
    }
    return jsonify(res)

@admin_role.route('/saveRolePower',methods=['PUT'])
def saveRolePower():
    req_form =request.form
    powerIds=req_form.get("powerIds")
    power_list=powerIds.split(',')
    roleId=req_form.get("roleId")
    update_role_power(id=roleId,power_list=power_list)
    return jsonify(success=True,msg="授权成功")

# @admin_user.route('/delete', methods=['POST'])
# @login_required
# def delete():
#     id = request.form.get('id')
#     user = delete_by_id()
#     db.session.commit()
#     if user:
#         return jsonify(msg="删除成功", code=200)
#     else:
#         return jsonify(msg="删除失败", code=999)
#

#  编辑用户
# @admin_user.route('/edit/<int:id>', methods=['GET', 'POST'])
# @login_required
# def update(id):
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         role = request.form.get('role')
#         if username and role:
#             if password is None:
#                 if User.query.filter_by(id=id).first() is not None:
#                     update_user(id,username)
#                     return jsonify(msg="修改成功", code=200)
#
#                 else:
#                     res = {"msg": "用户已经存在", "code": 200}
#                     return jsonify(res)
#             else:
#                 user = User.query.filter_by(id=id).first()
#                 if user is not None:
#                     User.query.filter_by(id=id).update({'username': username, 'role': role})
#                     user.set_password(password)
#                     db.session.commit()
#                     return jsonify(msg="修改成功", code=200)
#                 else:
#                     return jsonify(msg="用户不存在", code=200)
#
#         else:
#
#             return jsonify(msg="用户名密码角色不能为空", code=999)
#     else:
#         role = ['管理员', '普通用户']
#         user = User.query.filter_by(id=id).first()
#         return render_template('admin/user_edit.html', user=user, role=role)


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
# @admin_user.route('/batchRemove', methods=['GET', 'POST'])
# @login_required
# def batchRemove():
#     ids = request.form.getlist('ids[]')
#     res = batch_remove(ids)
#     return res
