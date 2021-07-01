from applications.extensions import db
from applications.models import Power, Role, User


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
    r = Role.query.filter_by(id=_id).delete()
    db.session.commit()
    return r


def batch_remove_role(ids):
    """ 批量删除 """
    for _id in ids:
        remove_role(_id)
