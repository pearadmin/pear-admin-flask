from flask import render_template
from flask_login import login_required, current_user
from sqlalchemy import desc

from applications.common.utils.rights import authorize
from applications.models import AdminLog, Role, User

from . import index_bp


# 用户增加
@index_bp.get('/users/')
@authorize("admin:user:main", log=True)
def users_main():
    return render_template('users/main.html')


@index_bp.get('/users/center')
@login_required
def users_center():
    user_logs = AdminLog.query.filter_by(url='/passport/login').filter_by(uid=current_user.id).order_by(
        desc(AdminLog.create_time)).limit(10)
    return render_template('users/profile.html', user_info=current_user, user_logs=user_logs)


@index_bp.get('/users/add')
@authorize("admin:user:add", log=True)
def users_get_user():
    roles = Role.query.all()
    return render_template('users/add.html', roles=roles)


@index_bp.get('/users/<user_id>')
@authorize("admin:user:edit", log=True)
def users_user_id_view(user_id):
    #  获取编辑用户信息
    user = User.query.filter_by(id=user_id).first()
    roles = Role.query.all()
    checked_roles = []
    for r in user.role:
        checked_roles.append(r.id)
    return render_template('users/edit_users.html', user=user, roles=roles, checked_roles=checked_roles)


@index_bp.get('/users/avatar')
def users_avatar_view():
    return render_template('users/avatar.html')
