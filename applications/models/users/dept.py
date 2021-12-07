from flask_restful import fields
from applications.extensions import db
from ..base import BaseModel


class CompanyDepartment(db.Model, BaseModel):
    __tablename__ = 'cp_dept'
    id = db.Column(db.Integer, primary_key=True, comment="部门ID")
    parent_id = db.Column(db.Integer, comment="父级编号")
    dept_name = db.Column(db.String(50), comment="部门名称")
    leader = db.Column(db.String(50), comment="负责人")
    phone = db.Column(db.String(20), comment="联系方式")
    email = db.Column(db.String(50), comment="邮箱")
    status = db.Column(db.Boolean, comment='状态(1开启,0关闭)')
    comment = db.Column(db.Text, comment="备注")
    address = db.Column(db.String(255), comment="详细地址")
    sort = db.Column(db.Integer, comment="排序")

    @staticmethod
    def fields():
        """
        定义模型的常用输出字段，新手请忽略。可以简化字段序列化操作，
        详细操作请查看 flask-restful marshal 的用法
        """
        return {
            'deptId': fields.Integer(attribute="id"),
            'parentId': fields.Integer(attribute="parent_id"),
            'deptName': fields.String(attribute="dept_name"),
            'sort': fields.Integer,
            'leader': fields.String,
            'phone': fields.String,
            'email': fields.String,
            'status': fields.Boolean,
            'comment': fields.String,
            'address': fields.String,
            'create_at': fields.DateTime
        }
