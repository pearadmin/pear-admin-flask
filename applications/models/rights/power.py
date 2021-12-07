from applications.extensions import db
from ..base import BaseModel


class RightsPower(db.Model, BaseModel):
    __tablename__ = 'rt_power'
    id = db.Column(db.Integer, primary_key=True, comment='权限编号')
    name = db.Column(db.String(255), comment='权限名称')
    type = db.Column(db.SMALLINT, comment='权限类型')
    code = db.Column(db.String(30), comment='权限标识')
    url = db.Column(db.String(255), comment='权限路径')
    open_type = db.Column(db.String(10), comment='打开方式')
    parent_id = db.Column(db.Integer, db.ForeignKey("rt_power.id"), comment='父类编号')
    icon = db.Column(db.String(128), comment='图标')
    sort = db.Column(db.Integer, comment='排序')
    enable = db.Column(db.Boolean, comment='是否开启')

    parent = db.relationship("RightsPower", remote_side=[id])  # 自关联
