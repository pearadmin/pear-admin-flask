from sqlalchemy import and_
from applications.models import db
from applications.models.admin_role import Role, RoleSchema
from applications.models.admin_power import Power, PowerSchema2
from applications.models.admin_user import User

# 获取角色对象
from applications.service.common.curd import model_to_dicts


def get_role_data(page, limit, filters):
    role = Role.query.filter(and_(*[getattr(Role, k).like(v) for k, v in filters.items()])).paginate(page=page,
                                                                                                     per_page=limit,
                                                                                                     error_out=False)
    count = Role.query.count()
    return role, count


# 获取角色dict
def get_role_data_dict(page, limit, filters):
    role, count = get_role_data(page, limit, filters)
    data = model_to_dicts(Schema=RoleSchema, model=role.items)
    return data, count


# 增加角色
def add_role(req):
    details = req.get("details")
    enable = req.get("enable")
    roleCode = req.get("roleCode")
    roleName = req.get("roleName")
    sort = req.get("sort")
    role = Role(
        details=details,
        enable=enable,
        code=roleCode,
        name=roleName,
        sort=sort
    )
    db.session.add(role)
    db.session.commit()


# 通过id获取角色
def get_role_by_id(id):
    r = Role.query.filter_by(id=id).first()
    return r


# 更新角色
def update_role(req_json):
    id = req_json.get("roleId")
    data = {
        "code": req_json.get("roleCode"),
        "name": req_json.get("roleName"),
        "sort": req_json.get("sort"),
        "enable": req_json.get("enable"),
        "details": req_json.get("details")
    }
    print(data)
    role = Role.query.filter_by(id=id).update(data)
    db.session.commit()
    return role


# 获取角色的权限
def get_role_power(id):
    role = Role.query.filter_by(id=id).first()
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


# 更新角色权限
def update_role_power(id, power_list):
    role = Role.query.filter_by(id=id).first()
    power_id_list = []
    for p in role.power:
        power_id_list.append(p.id)
        print(p.id)
    print(power_id_list)
    powers = Power.query.filter(Power.id.in_(power_id_list)).all()
    for p in powers:
        role.power.remove(p)
    powers = Power.query.filter(Power.id.in_(power_list)).all()
    for p in powers:
        role.power.append(p)
    db.session.commit()


# 启动角色
def enable_status(id):
    enable = 1
    role = Role.query.filter_by(id=id).update({"enable": enable})
    if role:
        db.session.commit()
        return True
    return False


# 停用角色
def disable_status(id):
    enable = 0
    role = Role.query.filter_by(id=id).update({"enable": enable})
    if role:
        db.session.commit()
        return True
    return False


# 删除角色
def remove_role(id):
    role = Role.query.filter_by(id=id).first()
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


# 批量删除
def batch_remove(ids):
    # role = Role.query.filter(Role.id.in_(ids)).delete(synchronize_session=False)
    # db.session.commit()
    for id in ids:
        remove_role(id)
