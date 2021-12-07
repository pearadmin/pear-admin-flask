from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import fields

from applications.extensions import db
from ..base import BaseModel


class CompanyUser(db.Model, UserMixin, BaseModel):
    __tablename__ = 'cp_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='用户ID')
    username = db.Column(db.String(20), comment='用户名')
    realname = db.Column(db.String(20), comment='真实名字')
    mobile = db.Column(db.String(11), comment='电话号码')
    avatar = db.Column(db.String(255), comment='头像', default="/static/admin/admin/images/avatar.jpg")
    comment = db.Column(db.String(255), comment='备注')
    password_hash = db.Column(db.String(128), comment='哈希密码')
    enable = db.Column(db.Integer, default=0, comment='启用')
    dept_id = db.Column(db.Integer, comment='部门id')

    role = db.relationship('RightsRole', secondary="rt_user_role", backref=db.backref('user'), lazy='dynamic')

    def set_password(self, password):
        """设置密码，对密码进行加密存储"""
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        """校验密码方法"""
        return check_password_hash(self.password_hash, password)
