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
    'create_at': fields.DateTime,
    'update_time': fields.DateTime,
    'enable': fields.Integer,
}

power2_fields = {
    'id': fields.Integer,
    'title': fields.String(attribute="name"),
    'type': fields.String,
    'code': fields.String,
    'href': fields.String(attribute="url"),
    'openType': fields.String(attribute="open_type"),
    'parent_id': fields.Integer,
    'icon': fields.String,
    'sort': fields.Integer,
    'create_at': fields.DateTime,
    'update_time': fields.DateTime,
    'enable': fields.Integer,
}

role_fields = {
    'id': fields.Integer,
    'roleName': fields.String(attribute="name"),
    'roleCode': fields.String(attribute="code"),
    'enable': fields.String,
    'remark': fields.String,
    'details': fields.String,
    'sort': fields.Integer,
    'create_at': fields.DateTime,
    'update_at': fields.DateTime,
}

log_fields = {
    'id': fields.Integer,
    'method': fields.String,
    'uid': fields.String,
    'url': fields.String,
    'desc': fields.String,
    'ip': fields.String,
    'user_agent': fields.String,
    'success': fields.Boolean,
    'create_at': fields.DateTime,
}

dept_fields = {
    'deptId': fields.Integer(attribute="id"),
    'parentId': fields.Integer(attribute="parent_id"),
    'deptName': fields.String(attribute="dept_name"),
    'leader': fields.String,
    'phone': fields.String,
    'email': fields.String,
    'address': fields.String,
    'status': fields.Integer,
    'sort': fields.Integer,
}

photo_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'href': fields.String,
    'mime': fields.String,
    'size': fields.String,
    'ext': fields.String,
    'create_at': fields.DateTime,
}
