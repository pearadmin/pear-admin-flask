from flask_restful import fields

from applications.extensions import db
from ..base import BaseModel


class RightsRole(db.Model, BaseModel):
    __tablename__ = 'rt_role'
    id = db.Column(db.Integer, primary_key=True, comment='角色ID')
    name = db.Column(db.String(255), comment='角色名称')
    code = db.Column(db.String(255), comment='角色标识')
    enable = db.Column(db.Boolean, comment='是否启用')
    comment = db.Column(db.String(255), comment='备注')
    details = db.Column(db.String(255), comment='详情')
    sort = db.Column(db.Integer, comment='排序')

    power = db.relationship('RightsPower', secondary="rt_role_power", backref=db.backref('role'))
