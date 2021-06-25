from flask import render_template, request, make_response
from flask_restful import Resource
from applications.extensions import db

from applications.common.utils.http import fail_api, success_api
from applications.common.utils.rights import authorize
from applications.models import User, Role
from applications.view.company.users import user_api, users_bp, user_curd


@user_api.resource('/')
class Users(Resource):
    """用户列表数据操作"""

    @authorize("admin:user:main", log=True)
    def get(self):
        return make_response(render_template('admin/user/main.html'))

    @authorize("admin:user:add", log=True)
    def post(self):
        """新建单个用户"""
        req_json = request.json
        a = req_json.get("roleIds")
        username = req_json.get('username')
        real_name = req_json.get('realName')
        password = req_json.get('password')
        role_ids = a.split(',')

        if not username or not real_name or not password:
            return fail_api(msg="账号姓名密码不得为空")

        if user_curd.is_user_exists(username):
            return fail_api(msg="用户已经存在")

        _id = user_curd.add_user(username, real_name, password)
        user_curd.add_user_role(_id, role_ids)

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
            render_template('admin/user/edit_users.html', user=user, roles=roles, checked_roles=checked_roles))

    @authorize("admin:user:remove", log=True)
    def delete(self, user_id):
        # 删除用户
        res = user_curd.delete_by_id(user_id)
        if not res:
            return fail_api(msg="删除失败")
        return success_api(msg="删除成功")

    @authorize("admin:user:edit", log=True)
    def put(self, user_id):
        # 更新用户数据
        req_json = request.json
        a = req_json.get("roleIds")
        _id = req_json.get("userId")
        username = req_json.get('username')
        real_name = req_json.get('realName')
        dept_id = req_json.get('deptId')
        role_ids = a.split(',')
        user_curd.update_user(user_id, username, real_name, dept_id)
        user_curd.update_user_role(_id, role_ids)
        return success_api(msg="更新成功")


# 批量删除
@users_bp.delete('/batchRemove')
@authorize("admin:user:remove", log=True)
def batch_remove():
    ids = request.form.getlist('ids[]')
    user_curd.batch_remove(ids)
    return success_api(msg="批量删除成功")


@users_bp.put('/enable')
def user_enable():
    # 启用或者禁用用户 enable disable
    user_id = request.json.get('userId')
    operate = request.json.get('operate')
    user_id = int(user_id)
    operate = int(operate)
    if user_id:
        if operate == 1:
            user = User.query.filter_by(id=user_id).update({"enable": operate})
            message = success_api(msg="启动成功")
        else:
            user = User.query.filter_by(id=user_id).update({"enable": operate})
            message = success_api(msg="禁用成功")
        if user:
            db.session.commit()
        else:
            return fail_api(msg="出错啦")
        return message
    return fail_api(msg="数据错误")
