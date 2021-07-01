from flask import jsonify
from flask_login import current_user
from sqlalchemy import and_, desc
from applications.extensions import db
from applications.models import User
from applications.models import Role
from applications.models import AdminLog



def get_current_user_logs():
    """ 获取当前用户日志 """
    log = AdminLog.query.filter_by(url='/passport/login').filter_by(uid=current_user.id).order_by(
        desc(AdminLog.create_time)).limit(10)
    return log


def is_user_exists(username):
    """ 判断用户是否存在 """
    res = User.query.filter_by(username=username).count()
    return bool(res)


def delete_by_id(_id):
    """ 删除用户 """
    user = User.query.filter_by(id=_id).first()
    roles_id = []
    for role in user.role:
        roles_id.append(role.id)
    roles = Role.query.filter(Role.id.in_(roles_id)).all()
    for r in roles:
        user.role.remove(r)
    res = User.query.filter_by(id=_id).delete()
    db.session.commit()
    return res


def batch_remove(ids):
    """ 批量删除 """
    for _id in ids:
        delete_by_id(_id)


def update_user_role(_id, roles_list):
    user = User.query.filter_by(id=_id).first()
    roles_id = []
    for role in user.role:
        roles_id.append(role.id)
    roles = Role.query.filter(Role.id.in_(roles_id)).all()
    for r in roles:
        user.role.remove(r)
    roles = Role.query.filter(Role.id.in_(roles_list)).all()
    for r in roles:
        user.role.append(r)
    db.session.commit()
