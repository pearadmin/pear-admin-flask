from sqlalchemy import and_

from applications.extensions import db
from applications.models import Role, RoleSchema
from applications.models.rights.power import Power
from applications.models import User

# 获取角色对象
from applications.common.curd import model_to_dicts


def get_role_data(page, limit, filters):
    print(page, limit, filters)
    role = Role.query.filter(
        and_(*[getattr(Role, k).like(v) for k, v in filters.items()])
    ).paginate(page=page, error_out=False)
    count = Role.query.count()
    return role, count


def get_role_data_dict(page, limit, filters):
    """ 获取角色dict """
    role, count = get_role_data(page, limit, filters)
    data = model_to_dicts(Schema=RoleSchema, model=role.items)
    return data, count


def get_role_by_id(_id):
    """ 通过id获取角色 """
    r = Role.query.filter_by(id=_id).first()
    return r


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
