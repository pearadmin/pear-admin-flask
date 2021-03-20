from flask_marshmallow import Marshmallow
from marshmallow import fields
from sqlalchemy import and_

from applications.models import db
from applications.models.admin import Role, Power, User

ma = Marshmallow()


class RoleSchema(ma.Schema):
    id = fields.Integer()
    roleName = fields.Str(attribute="name")
    roleCode = fields.Str(attribute="code")
    enable = fields.Str()
    remark = fields.Str()
    details = fields.Str()
    sort = fields.Integer()
    create_at = fields.DateTime()
    update_at = fields.DateTime()


class PowerSchema(ma.Schema):  # 序列化类
    powerId = fields.Str(attribute="id")
    powerName = fields.Str(attribute="name")
    powerType = fields.Str(attribute="type")
    powerUrl = fields.Str(attribute="url")
    openType = fields.Str(attribute="pen_type")
    parentId = fields.Str(attribute="parent_id")
    icon = fields.Str()
    sort = fields.Integer()
    create_time = fields.DateTime()
    update_time = fields.DateTime()
    enable = fields.Integer()


# 获取角色对象
def get_role_data(page, limit, filters):
    role = Role.query.filter(and_(*[getattr(Role, k).like(v) for k, v in filters.items()])).paginate(page=page,
                                                                                                     per_page=limit,
                                                                                                     error_out=False)
    count = Role.query.count()
    return role, count


# 获取角色dict
def get_role_data_dict(page, limit, filters):
    role, count = get_role_data(page, limit, filters)
    role_schema = RoleSchema(many=True)  # 用已继承ma.ModelSchema类的自定制类生成序列化类
    output = role_schema.dump(role.items)  # 生成可序列化对象
    return output, count


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
    power_schema = PowerSchema(many=True)  # 用已继承ma.ModelSchema类的自定制类生成序列化类
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
