from flask_marshmallow import Marshmallow
from marshmallow import fields

from applications.models import db
from applications.models.admin import Role, Power

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


'''
获取用户的sqlalchemy对象
分页器
'''


def get_role_data(page, limit):
    role = Role.query.paginate(page=page, per_page=limit, error_out=False)
    count = Role.query.count()
    return role, count


def get_role_data_dict(page, limit):
    role, count = get_role_data(page, limit)
    role_schema = RoleSchema(many=True)  # 用已继承ma.ModelSchema类的自定制类生成序列化类
    output = role_schema.dump(role.items)  # 生成可序列化对象
    return output, count


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
