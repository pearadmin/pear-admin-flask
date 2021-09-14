from flask_restful import fields

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

    @staticmethod
    def fields():
        return {
            'powerId': fields.String(attribute="id"),
            'powerName': fields.String(attribute="name"),
            'powerType': fields.String(attribute="type"),
            'powerUrl': fields.String(attribute="url"),
            'openType': fields.String(attribute="open_type"),
            'parentId': fields.String(attribute="parent_id"),
            'icon': fields.String,
            'sort': fields.Integer,
            'create_at': fields.DateTime,
            'update_at': fields.DateTime,
            'enable': fields.Integer,
        }

    @staticmethod
    def fields2():
        return {
            'id': fields.Integer,
            'title': fields.String(attribute="name"),
            'type': fields.String,
            'code': fields.String,
            'href': fields.String(attribute="url"),
            'openType': fields.String(attribute="open_type"),
            'parent_id': fields.Integer,
            'icon': fields.String,
            'sort': fields.Integer,
            'enable': fields.Boolean,
            'update_at': fields.DateTime,
            'create_at': fields.DateTime,

        }
