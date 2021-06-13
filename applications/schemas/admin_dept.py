from applications.extensions import  ma
from marshmallow import fields, validate


class DeptSchema(ma.Schema):
    deptId = fields.Integer(attribute="id")
    parentId = fields.Integer(attribute="parent_id")
    deptName = fields.Str(attribute="dept_name")
    leader = fields.Str()
    phone = fields.Str()
    email = fields.Str(validate=validate.Email())
    address = fields.Str()
    status = fields.Str(validate=validate.OneOf(["0", "1"]))
    sort = fields.Integer()
