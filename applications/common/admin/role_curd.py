from sqlalchemy import and_

from applications.common.utils.validate import xss_escape
from applications.extensions import db
from applications.models import Role, RoleSchema
from applications.models.rights.power import Power, PowerSchema2
from applications.models import User

# 获取角色对象
from applications.common.curd import model_to_dicts


def get_role_data(page, limit, filters):
    role = Role.query.filter(and_(*[getattr(Role, k).like(v) for k, v in filters.items()])).paginate(page=page,
                                                                                                     per_page=limit,
                                                                                                     error_out=False)
    count = Role.query.count()
    return role, count


def get_role_data_dict(page, limit, filters):
    """ 获取角色dict """
    role, count = get_role_data(page, limit, filters)
    data = model_to_dicts(Schema=RoleSchema, model=role.items)
    return data, count


def add_role(req):
    """ 增加角色 """
    details = xss_escape(req.get("details"))
    enable = xss_escape(req.get("enable"))
    roleCode = xss_escape(req.get("roleCode"))
    roleName = xss_escape(req.get("roleName"))
    sort = xss_escape(req.get("sort"))
    role = Role(
        details=details,
        enable=enable,
        code=roleCode,
        name=roleName,
        sort=sort
    )
    db.session.add(role)
    db.session.commit()


def get_role_by_id(_id):
    """ 通过id获取角色 """
    r = Role.query.filter_by(id=_id).first()
    return r


def update_role(req_json):
    """ 更新角色 """
    _id = req_json.get("roleId")
    data = {
        "code": xss_escape(req_json.get("roleCode")),
        "name": xss_escape(req_json.get("roleName")),
        "sort": xss_escape(req_json.get("sort")),
        "enable": xss_escape(req_json.get("enable")),
        "details": xss_escape(req_json.get("details"))
    }
    role = Role.query.filter_by(id=_id).update(data)
    db.session.commit()
    return role


def get_role_power(_id):
    """ 获取角色的权限 """
    role = Role.query.filter_by(id=_id).first()
    check_powers = role.power
    check_powers_list = []
    for cp in check_powers:
        check_powers_list.append(cp.id)
    powers = Power.query.all()
    power_schema = PowerSchema2(many=True)  # 用已继承ma.ModelSchema类的自定制类生成序列化类
    output = power_schema.dump(powers)  # 生成可序列化对象
    for i in output:
        if int(i.get("powerId")) in check_powers_list:
            i["checkArr"] = "1"
        else:
            i["checkArr"] = "0"
    return output


def update_role_power(_id, power_list):
    """ 更新角色权限 """
    role = Role.query.filter_by(id=_id).first()
    power_id_list = []
    for p in role.power:
        power_id_list.append(p.id)
    powers = Power.query.filter(Power.id.in_(power_id_list)).all()
    for p in powers:
        role.power.remove(p)
    powers = Power.query.filter(Power.id.in_(power_list)).all()
    for p in powers:
        role.power.append(p)
    db.session.commit()


def enable_status(_id):
    """ 启用角色 """
    enable = 1
    role = Role.query.filter_by(id=_id).update({"enable": enable})
    if role:
        db.session.commit()
        return True
    return False


def disable_status(_id):
    """ 停用角色 """
    enable = 0
    role = Role.query.filter_by(id=_id).update({"enable": enable})
    if role:
        db.session.commit()
        return True
    return False


def remove_role(_id):
    """ 删除角色 """
    role = Role.query.filter_by(id=_id).first()
    # 删除该角色的权限
    power_id_list = []
    for p in role.power:
        power_id_list.append(p.id)

    powers = Power.query.filter(Power.id.in_(power_id_list)).all()
    for p in powers:
        role.power.remove(p)
    user_id_list = []
    for u in role.user:
        user_id_list.append(u.id)
    users = User.query.filter(User.id.in_(user_id_list)).all()
    for u in users:
        role.user.remove(u)
    r = Role.query.filter_by(id=id).delete()
    db.session.commit()
    return r


def batch_remove(ids):
    """ 批量删除 """
    for _id in ids:
        remove_role(_id)
