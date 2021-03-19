from flask_marshmallow import Marshmallow
from marshmallow import fields

from applications.models import db
from applications.models.admin import Power, Role

ma = Marshmallow()


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


def get_power_dict():
    power = Power.query.all()
    power_schema = PowerSchema(many=True)
    power_dict = power_schema.dump(power)
    return power_dict


# 选择父节点
def select_parent():
    power = Power.query.all()
    power_schema = PowerSchema(many=True)
    power_dict = power_schema.dump(power)
    power_dict.append({"powerId": 0, "powerName": "顶级权限", "parentId": -1})
    return power_dict


# 增加权限
def save_power(req):
    icon = req.get("icon")
    openType = req.get("openType")
    parentId = req.get("parentId")
    powerCode = req.get("powerCode")
    powerName = req.get("powerName")
    powerType = req.get("powerType")
    powerUrl = req.get("powerUrl")
    sort = req.get("sort")
    power = Power(
        icon=icon,
        open_type=openType,
        parent_id=parentId,
        code=powerCode,
        name=powerName,
        type=powerType,
        url=powerUrl,
        sort=sort
    )
    r = db.session.add(power)
    db.session.commit()
    return r


# 根据id查询权限
def get_power_by_id(id):
    p = Power.query.filter_by(id=id).first()
    return p


# 更新角色
def update_power(req_json):
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


# 删除权限（目前没有判断父节点自动删除子节点）
def remove_power(id):
    power = Power.query.filter_by(id=id).first()
    role_id_list = []
    roles = power.role
    for role in roles:
        role_id_list.append(role.id)
    roles = Role.query.filter(Role.id.in_(role_id_list)).all()
    for p in roles:
        power.role.remove(p)
    r = Power.query.filter_by(id=id).delete()
    db.session.commit()
    return r
