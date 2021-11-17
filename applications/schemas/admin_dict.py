from applications.extensions import ma
from marshmallow import fields


class DictTypeOutSchema(ma.Schema):
    id = fields.Str(attribute="id")
    typeName = fields.Str(attribute="type_name")
    typeCode = fields.Str(attribute="type_code")
    description = fields.Str(attribute="description")
    createTime = fields.Str(attribute="create_time")
    updateName = fields.Str(attribute="update_time")
    remark = fields.Str()
    enable = fields.Str()


class DictDataOutSchema(ma.Schema):
    dataId = fields.Str(attribute="id")
    dataLabel = fields.Str(attribute="data_label")
    dataValue = fields.Str(attribute="data_value")
    remark = fields.Str()
    enable = fields.Str()
