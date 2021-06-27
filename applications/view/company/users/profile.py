# 个人中心
from flask import render_template, request, make_response, jsonify
from flask_login import login_required, current_user
from flask_restful import Resource, reqparse
from sqlalchemy import desc

from applications.common.utils.http import fail_api, success_api
from applications.extensions import db
from applications.models import User, AdminLog
from applications.view.company.users import users_bp, user_api


@users_bp.get('/center')
@login_required
def center():
    user_info = current_user
    user_logs = AdminLog.query.filter_by(url='/passport/login').filter_by(uid=current_user.id).order_by(
        desc(AdminLog.create_time)).limit(10)
    return render_template('admin/user/profile.html', user_info=user_info, user_logs=user_logs)


@user_api.resource('/avatar')
class Avatar(Resource):
    """修改头像"""

    def get(self):
        return make_response(render_template('admin/user/avatar.html'))

    def put(self):
        url = request.json.get("avatar").get("src")
        ret = User.query.filter_by(id=current_user.id).update({"avatar": url})
        db.session.commit()
        if not ret:
            return fail_api(msg="出错啦")
        return success_api(msg="修改成功")


# 修改当前用户信息
@users_bp.put('/updateInfo')
@login_required
def update_info():

    parser = reqparse.RequestParser()
    parser.add_argument('realname', type=str, dest='real_name')
    parser.add_argument('remark', type=str)
    parser.add_argument('details', type=str)

    res = parser.parse_args()

    ret = User.query.filter_by(
        id=current_user.id).update({"realname": res.real_name,
                                    "remark": res.details})
    if not ret:
        return fail_api(msg="出错啦")
    return success_api(msg="更新成功")


@user_api.resource('/editPassword')
class EditPassword(Resource):
    """前用户密码"""

    @login_required
    def get(self):
        return make_response(render_template('admin/user/edit_password.html'))

    @login_required
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('oldPassword', type=str, required=True, help='旧密码不得为空')
        parser.add_argument('newPassword', type=str, required=True, help='新密码不得为空')
        parser.add_argument('confirmPassword', type=str, required=True, help='确认密码不能为空')

        res = parser.parse_args()

        if res.newPassword != res.confirmPassword:
            return fail_api(msg='确认密码不一致')

        """ 修改当前用户密码 """
        is_right = current_user.validate_password(res.oldPassword)
        if not is_right:
            return jsonify(success=False, msg="旧密码错误")
        current_user.set_password(res.newPassword)
        db.session.add(current_user)
        db.session.commit()

        return jsonify(success=True, msg="更改成功")
