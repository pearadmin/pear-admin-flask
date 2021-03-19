from flask import jsonify
from flask_login import current_user
from flask_marshmallow import Marshmallow
from marshmallow import fields
from sqlalchemy import and_
from sqlalchemy.sql import exists

from applications.models import db
from applications.models.admin import User, Role
from sqlalchemy.orm.dynamic import AppenderQuery

ma = Marshmallow()


# 用户models的序列化类
class UserSchema(ma.Schema):
    id = fields.Integer()
    username = fields.Str()
    realname = fields.Str()
    enable = fields.Bool()
    create_at = fields.DateTime()
    update_at = fields.DateTime()


'''
获取用户的sqlalchemy对象
分页器
'''


def get_user_data(page, limit,filters):
    user = User.query.filter(and_(*[getattr(User, k).like(v) for k,v in filters.items()])).paginate(page=page, per_page=limit, error_out=False)
    count = User.query.count()
    return user, count


'''
获取用户的dict数据
分页器
'''


def get_user_data_dict(page, limit, filters):
    user, count = get_user_data(page, limit,filters)
    user_schema = UserSchema(many=True)  # 用已继承ma.ModelSchema类的自定制类生成序列化类
    output = user_schema.dump(user.items)  # 生成可序列化对象
    return output, count


'''
通过名称获取用户
'''


def get_user_by_name(username):
    return User.query.filter_by(username=username).first()


# 判断用户是否存在
def is_user_exists(username):
    res = User.query.filter_by(username=username).count()
    return bool(res)


# 增加用户
def add_user(username, realName, password):
    user = User(username=username, realname=realName)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()


# 更新用户信息
def update_user(id, username, realname):
    user = User.query.filter_by(id=id).update({'username': username, 'realname': realname})
    db.session.commit()
    return user


def delete_by_id(id):
    user = User.query.filter_by(id=id).delete()
    return user


def update_status(status):
    user = User.query.filter_by(id=id).update({'status': status})
    if user:
        db.session.commit()
        return jsonify(msg="更新成功", code=200)
    return jsonify(msg="出错啦", code=999)


def batch_remove(ids):
    user = User.query.filter(User.id.in_(ids)).delete(synchronize_session=False)
    db.session.commit()
    if user:
        res = jsonify(msg="批量删除成功", code=200)
        return jsonify(res)
    else:
        res = jsonify(msg="批量删除失败", code=999)
        return jsonify(res)


def update_user_role(id, roles_list):
    user = User.query.filter_by(id=id).first()
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
