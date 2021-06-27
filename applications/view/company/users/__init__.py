from flask import Blueprint, request, render_template
from flask_restful import Api, reqparse

from applications.common.utils.http import table_api
from applications.common.utils.rights import authorize
from applications.models import Role, User, Dept

users_bp = Blueprint('users', __name__, url_prefix='/users')
user_api = Api(users_bp)


#   用户分页查询
@users_bp.get('/data')
@authorize("admin:user:main", log=True)
def data():
    parser = reqparse.RequestParser()
    parser.add_argument('page', type=int, default=1)
    parser.add_argument('limit', type=int, default=10)
    parser.add_argument('realName', type=str, dest='real_name')
    parser.add_argument('username', type=str)
    parser.add_argument('deptId', type=int, dest='dept_id', default=0)

    res = parser.parse_args()

    filters = []

    if res.real_name:
        filters.append(User.realname.like('%' + res.real_name + '%'))
    if res.username:
        filters.append(User.username.like('%' + res.username + '%'))
    if res.dept_id:
        filters.append(User.dept_id == res.dept_id)

    paginate = User.query.filter(*filters).paginate(page=res.page,
                                                    per_page=res.limit,
                                                    error_out=False)

    dept_name = lambda dept_id: Dept.query.filter_by(id=dept_id).first().dept_name
    user_data = [{
        'id': item.id,
        'username': item.username,
        'realname': item.realname,
        'enable': item.enable,
        'create_at': item.create_at,
        'update_at': item.update_at,
        'dept': dept_name(item.dept_id),
    } for item in paginate.items]

    return table_api(data=user_data, count=paginate.total)


# 用户增加
@users_bp.get('/')
@authorize("admin:user:main", log=True)
def get():
    return render_template('admin/user/main.html')


from . import profile, _utils
from . import user_view
