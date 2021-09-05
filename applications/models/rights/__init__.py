from applications.extensions import db
from .power import RightsPower
from .role import RightsRole

# 创建中间表
user_role = db.Table(
    "rt_user_role",  # 中间表名称
    db.Column("id", db.Integer, primary_key=True, autoincrement=True, comment='标识'),  # 主键
    db.Column("user_id", db.Integer, db.ForeignKey("cp_user.id"), comment='用户编号'),  # 属性 外键
    db.Column("role_id", db.Integer, db.ForeignKey("rt_role.id"), comment='角色编号'),  # 属性 外键
)

# 创建中间表
role_power = db.Table(
    "rt_role_power",  # 中间表名称
    db.Column("id", db.Integer, primary_key=True, autoincrement=True, comment='标识'),  # 主键
    db.Column("power_id", db.Integer, db.ForeignKey("rt_power.id"), comment='用户编号'),  # 属性 外键
    db.Column("role_id", db.Integer, db.ForeignKey("rt_role.id"), comment='角色编号'),  # 属性 外键
)
