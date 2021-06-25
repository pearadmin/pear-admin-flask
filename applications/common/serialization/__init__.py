from flask_restful import fields

power_fields = {
    'powerId': fields.String(attribute="id"),
    'powerName': fields.String(attribute="name"),
    'powerType': fields.String(attribute="type"),
    'powerUrl': fields.String(attribute="url"),
    'openType': fields.String(attribute="open_type"),
    'parentId': fields.String(attribute="parent_id"),
    'icon': fields.String,
    'sort': fields.Integer,
    'create_time': fields.DateTime,
    'update_time': fields.DateTime,
    'enable': fields.Integer,
}
