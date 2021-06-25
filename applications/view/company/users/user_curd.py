from flask import jsonify
from flask_login import current_user
from sqlalchemy import and_, desc
from applications.extensions import db
from applications.models import User, UserSchema
from applications.models import Role
from applications.models import AdminLog

# 获取用户的 sqlalchemy 对象分页器
from applications.common.curd import model_to_dicts


def get_user_data(page, limit, filters, deptId):
    if deptId:
        user = User.query.filter_by(dept_id=deptId).filter(
            and_(*[getattr(User, k).like(v) for k, v in filters.items()])).paginate(page=page,
                                                                                    per_page=limit,
                                                                                    error_out=False)
    else:
        user = User.query.filter(and_(*[getattr(User, k).like(v) for k, v in filters.items()])).paginate(page=page,
                                                                                                         per_page=limit,
                                                                                                         error_out=False)
    count = User.query.count()
    return user, count


def get_user_data_dict(page, limit, filters, deptId):
    """ 获取用户的dict数据分页器 """
    user, count = get_user_data(page, limit, filters, deptId)
    data = model_to_dicts(Schema=UserSchema, model=user.items)
    return data, count


def get_user_by_name(username):
    """ 通过名称获取用户 """
    return User.query.filter_by(username=username).first()


def get_current_user_logs():
    """ 获取当前用户日志 """
    log = AdminLog.query.filter_by(url='/admin/login').filter_by(uid=current_user.id).order_by(
        desc(AdminLog.create_time)).limit(10)
    return log


def is_user_exists(username):
    """ 判断用户是否存在 """
    res = User.query.filter_by(username=username).count()
    return bool(res)


def add_user(username, real_name, password):
    """ 增加用户 """
    user = User()
    user.username = username
    user.realname = real_name
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user.id


def add_user_role(_id, roles_list):
    """ 增加用户角色 """
    user = User.query.filter_by(id=_id).first()
    roles = Role.query.filter(Role.id.in_(roles_list)).all()
    for r in roles:
        user.role.append(r)
    db.session.commit()


def update_avatar(url):
    """ 更新用户头像 """
    r = User.query.filter_by(id=current_user.id).update({"avatar": url})
    db.session.commit()
    return r


def update_user(_id, username, realname, deptId):
    """ 更新用户信息 """
    user = User.query.filter_by(id=_id).update({'username': username, 'realname': realname, 'dept_id': deptId})
    db.session.commit()
    return user


def update_current_user_info(req_json):
    """ 更新当前用户信息 """
    r = User.query.filter_by(id=current_user.id).update(
        {"realname": req_json.get("realName"), "remark": req_json.get("details")})
    db.session.commit()
    return r


def edit_password(res_json):
    """ 修改当前用户密码 """
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


def enable_status(_id):
    """ 启用用户 """
    enable = 1
    user = User.query.filter_by(id=_id).update({"enable": enable})
    if user:
        db.session.commit()
        return True
    return False


def disable_status(_id):
    """ 停用用户 """
    enable = 0
    user = User.query.filter_by(id=_id).update({"enable": enable})
    if user:
        db.session.commit()
        return True
    return False


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
