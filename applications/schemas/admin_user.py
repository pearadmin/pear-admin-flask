from applications.extensions import ma
from marshmallow import fields
from applications.models import Dept


# 用户models的序列化类
class UserOutSchema(ma.Schema):
    id = fields.Integer()
    username = fields.Str()
    realname = fields.Str()
    enable = fields.Integer()
    create_at = fields.DateTime()
    update_at = fields.DateTime()
    dept = fields.Method("get_dept")

    def get_dept(self, obj):
        if obj.dept_id != None:
            return Dept.query.filter_by(id=obj.dept_id).first().dept_name
        else:
            return None
