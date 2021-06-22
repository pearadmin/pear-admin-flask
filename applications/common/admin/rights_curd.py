from flask import escape
from applications.extensions import db
from applications.models.rights.power import Power, PowerSchema2
from applications.models import Role
from applications.common.curd import model_to_dicts


def get_power_dict():
    power = Power.query.all()
    res = model_to_dicts(Schema=PowerSchema2, model=power)
    return res


# 选择父节点
def select_parent():
    power = Power.query.all()
    res = model_to_dicts(Schema=PowerSchema2, model=power)
    res.append({"powerId": 0, "powerName": "顶级权限", "parentId": -1})
    return res


# 增加权限
def save_power(req):
    icon = escape(req.get("icon"))
    openType = escape(req.get("openType"))
    parentId = escape(req.get("parentId"))
    powerCode = escape(req.get("powerCode"))
    powerName = escape(req.get("powerName"))
    powerType = escape(req.get("powerType"))
    powerUrl = escape(req.get("powerUrl"))
    sort = escape(req.get("sort"))
    power = Power(
        icon=icon,
        open_type=openType,
        parent_id=parentId,
        code=powerCode,
        name=powerName,
        type=powerType,
        url=powerUrl,
        sort=sort,
        enable=1
    )
    r = db.session.add(power)
    db.session.commit()
    return r


# 根据id查询权限
def get_power_by_id(id):
    p = Power.query.filter_by(id=id).first()
    return p


# 更新权限
def update_power(req_json):
    id = req_json.get("powerId")
    data = {
        "icon": escape(req_json.get("icon")),
        "open_type": escape(req_json.get("openType")),
        "parent_id": escape(req_json.get("parentId")),
        "code": escape(req_json.get("powerCode")),
        "name": escape(req_json.get("powerName")),
        "type": escape(req_json.get("powerType")),
        "url": escape(req_json.get("powerUrl")),
        "sort": escape(req_json.get("sort"))
    }
    # print(data)
    power = Power.query.filter_by(id=id).update(data)
    db.session.commit()
    # print(power)
    return power


# 启动权限
def enable_status(id):
    enable = 1
    user = Power.query.filter_by(id=id).update({"enable": enable})
    if user:
        db.session.commit()
        return True
    return False


# 停用权限
def disable_status(id):
    enable = 0
    user = Power.query.filter_by(id=id).update({"enable": enable})
    if user:
        db.session.commit()
        return True
    return False


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


# 批量删除权限
def batch_remove(ids):
    for _id in ids:
        remove_power(_id)
