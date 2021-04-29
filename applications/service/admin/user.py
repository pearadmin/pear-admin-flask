from flask import jsonify
from flask_login import current_user
from sqlalchemy import and_, desc
from applications.models import db
from applications.models.admin_user import User, UserSchema
from applications.models.admin_role import Role
from applications.models.admin_log import AdminLog


# 获取用户的sqlalchemy对象分页器
from applications.service.common.curd import model_to_dicts


def get_user_data(page, limit, filters):
    user = User.query.filter(and_(*[getattr(User, k).like(v) for k, v in filters.items()])).paginate(page=page,
                                                                                                     per_page=limit,
                                                                                                     error_out=False)
    count = User.query.count()
    return user, count


# 获取用户的dict数据分页器
def get_user_data_dict(page, limit, filters):
    user, count = get_user_data(page, limit, filters)
    data = model_to_dicts(Schema=UserSchema,model=user.items)
    return data, count


# 通过名称获取用户
def get_user_by_name(username):
    return User.query.filter_by(username=username).first()


# 获取当前用户日志
def get_current_user_logs():
    log = AdminLog.query.filter_by(url='/admin/login').filter_by(uid=current_user.id).order_by(
        desc(AdminLog.create_time)).limit(10)
    return log


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
    return user.id


# 增加用户角色
def add_user_role(id, roles_list):
    user = User.query.filter_by(id=id).first()
    roles = Role.query.filter(Role.id.in_(roles_list)).all()
    for r in roles:
        user.role.append(r)
    db.session.commit()


# 更新用户头像
def update_avatar(url):
    r = User.query.filter_by(id=current_user.id).update({"avatar": url})
    db.session.commit()
    return r


# 更新用户信息
def update_user(id, username, realname):
    user = User.query.filter_by(id=id).update({'username': username, 'realname': realname})
    db.session.commit()
    return user


# 更新当前用户信息
def update_current_user_info(req_json):
    r = User.query.filter_by(id=current_user.id).update(
        {"realname": req_json.get("realName"), "remark": req_json.get("details")})
    db.session.commit()
    return r


# 修改当前用户密码
def edit_password(res_json):
    if res_json.get("newPassword") == '':
        return jsonify(success=False, msg="新密码不得为空")
    if res_json.get("newPassword") != res_json.get("confirmPassword"):
        return jsonify(success=False, msg="俩次密码不一样")
    user = current_user
    is_right = user.validate_password(res_json.get("oldPassword"))
    if not is_right:
        return jsonify(success=False, msg="旧密码错误")
    user.set_password(res_json.get("newPassword"))
    db.session.add(user)
    db.session.commit()
    return jsonify(success=True, msg="更改成功")


# 删除用户
def delete_by_id(id):
    user = User.query.filter_by(id=id).first()
    roles_id = []
    for role in user.role:
        roles_id.append(role.id)
    roles = Role.query.filter(Role.id.in_(roles_id)).all()
    for r in roles:
        user.role.remove(r)
    res = User.query.filter_by(id=id).delete()
    db.session.commit()
    return res


# 启用用户
def enable_status(id):
    enable = 1
    user = User.query.filter_by(id=id).update({"enable": enable})
    if user:
        db.session.commit()
        return True
    return False


# 停用用户
def disable_status(id):
    enable = 0
    user = User.query.filter_by(id=id).update({"enable": enable})
    if user:
        db.session.commit()
        return True
    return False


# 批量删除
def batch_remove(ids):
    for id in ids:
        delete_by_id(id)


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
