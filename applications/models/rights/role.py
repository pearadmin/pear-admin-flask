import datetime
from applications.extensions import db, ma
from marshmallow import fields


class Role(db.Model):
    __tablename__ = 'rt_role'
    id = db.Column(db.Integer, primary_key=True, comment='角色ID')
    name = db.Column(db.String(255), comment='角色名称')
    code = db.Column(db.String(255), comment='角色标识')
    enable = db.Column(db.Integer, comment='是否启用')
    remark = db.Column(db.String(255), comment='备注')
    details = db.Column(db.String(255), comment='详情')
    sort = db.Column(db.Integer, comment='排序')
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='更新时间')
    power = db.relationship('Power', secondary="rt_role_power", backref=db.backref('role'))


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
