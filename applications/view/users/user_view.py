from flask import request
from flask_restful import Resource, reqparse
from applications.extensions import db

from applications.common.utils.http import fail_api, success_api, table_api
from applications.common.utils.rights import authorize
from applications.models import User, Role, Dept
from applications.view.users import user_api, users_bp, _utils

# TODO 分离视图操作
from flask import render_template, make_response


@user_api.resource('/add')
class Users(Resource):
    """用户列表数据操作"""

    @authorize("admin:user:add", log=True)
    def get(self):
        roles = Role.query.all()
        return make_response(render_template('users/add.html', roles=roles))

    @authorize("admin:user:add", log=True)
    def post(self):
        """新建单个用户"""
        parser = reqparse.RequestParser()
        parser.add_argument("roleIds", type=str, dest='role_ids')
        parser.add_argument("username", type=str, required=True, help="用户名不能为空")
        parser.add_argument("realName", type=str, required=True, help="真实姓名不能为空", dest='real_name')
        parser.add_argument("password", type=str, required=True, help="密码不得为空")

        res = parser.parse_args()

        role_ids = res.role_ids.split(',')

        if _utils.is_user_exists(res.username):
            return fail_api(msg="用户已经存在")

        user = User()
        user.username = res.username
        user.realname = res.real_name
        user.set_password(res.password)
        db.session.add(user)
        db.session.commit()

        """ 增加用户角色 """
        user = User.query.filter_by(id=user.id).first()
        roles = Role.query.filter(Role.id.in_(role_ids)).all()
        for r in roles:
            user.role.append(r)
        db.session.commit()

        return success_api(msg="增加成功")


@user_api.resource('/<user_id>')
class CURDUser(Resource):
    """修改用户数据"""

    @authorize("admin:user:edit", log=True)
    def get(self, user_id):
        #  获取编辑用户信息
        user = User.query.filter_by(id=user_id).first()
        roles = Role.query.all()
        checked_roles = []
        for r in user.role:
            checked_roles.append(r.id)
        return make_response(
            render_template('users/edit_users.html', user=user, roles=roles, checked_roles=checked_roles))

    @authorize("admin:users:remove", log=True)
    def delete(self, user_id):
        # 删除用户
        res = _utils.delete_by_id(user_id)
        if not res:
            return fail_api(msg="删除失败")
        return success_api(msg="删除成功")

    @authorize("admin:users:edit", log=True)
    def put(self, user_id):

        parser = reqparse.RequestParser()
        parser.add_argument('roleIds', type=str, dest='role_ids')
        parser.add_argument('userId', type=str, dest='user_id')
        parser.add_argument('username', type=str)
        parser.add_argument('realName', type=str, dest='real_name')
        parser.add_argument('deptId', type=str, dest='dept_id')

        res = parser.parse_args()
        role_ids = res.role_ids.split(',')

        # 更新用户数据
        User.query.filter_by(id=user_id).update({'username': res.username,
                                                 'realname': res.real_name,
                                                 'dept_id': res.dept_id})
        db.session.commit()

        _utils.update_user_role(user_id, role_ids)

        return success_api(msg="更新成功")


# 批量删除
@users_bp.delete('/batchRemove')
@authorize("admin:user:remove", log=True)
def batch_remove():
    ids = request.form.getlist('ids[]')
    _utils.batch_remove(ids)
    return success_api(msg="批量删除成功")


@users_bp.put('/enable')
def user_enable():
    # 启用或者禁用用户 enable disable

    parser = reqparse.RequestParser()
    parser.add_argument('userId', type=int, required=True, dest='user_id')
    parser.add_argument('operate', type=int, required=True, dest='operate', choices=[0, 1])

    res = parser.parse_args()

    if res.operate == 1:
        user = User.query.filter_by(id=res.user_id).update({"enable": res.operate})
        message = success_api(msg="启动成功")
    else:
        user = User.query.filter_by(id=res.user_id).update({"enable": res.operate})
        message = success_api(msg="禁用成功")
    if user:
        db.session.commit()
    else:
        return fail_api(msg="出错啦")
    return message


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
