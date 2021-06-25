from flask import Blueprint, request, render_template
from flask_restful import Api

from applications.common.utils.http import table_api
from applications.common.utils.rights import authorize
from applications.models import Role

users_bp = Blueprint('users', __name__, url_prefix='/users')
user_api = Api(users_bp)


#   用户分页查询
@users_bp.get('/data')
@authorize("admin:user:main", log=True)
def data():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    real_name = request.args.get('realName', type=str)
    username = request.args.get('username', type=str)
    dept_id = request.args.get('deptId', type=int)
    filters = {}
    if real_name:
        filters["realname"] = ('%' + real_name + '%')
    if username:
        filters["username"] = ('%' + username + '%')
    user_data, count = user_curd.get_user_data_dict(page=page, limit=limit, filters=filters, deptId=dept_id)
    return table_api(data=user_data, count=count)


# 用户增加
@users_bp.get('/add')
@authorize("admin:user:add", log=True)
def add():
    roles = Role.query.all()
    return render_template('admin/user/add.html', roles=roles)


from . import profile, user_curd
from . import user_view
