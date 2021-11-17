from applications.extensions import ma
from marshmallow import fields, validate


class DeptInSchema(ma.Schema):
    parentId = fields.Integer(required=True)
    deptName = fields.Str(required=True)
    leader = fields.Str(required=True)
    phone = fields.Str(required=True)
    email = fields.Str(validate=validate.Email())
    address = fields.Str()
    status = fields.Str(validate=validate.OneOf(["0", "1"]))
    sort = fields.Integer()


class DeptOutSchema(ma.Schema):
    deptId = fields.Integer(attribute="id")
    parentId = fields.Integer(attribute="parent_id")
    deptName = fields.Str(attribute="dept_name")
    leader = fields.Str()
    phone = fields.Str()
    email = fields.Str(validate=validate.Email())
    address = fields.Str()
    status = fields.Str(validate=validate.OneOf(["0", "1"]))
    sort = fields.Integer()
