# 个人中心
from flask import request, jsonify
from flask_login import login_required
from flask_restful import Resource, reqparse

from applications.common.utils.http import fail_api, success_api
from applications.extensions import db
from applications.models import CompanyUser


class UserStatusResource(Resource):
    def put(self, user_id):
        # 启用或者禁用用户 enable disable

        parser = reqparse.RequestParser()
        parser.add_argument('userId', type=int, required=True, dest='user_id')
        parser.add_argument('operate', type=int, required=True, dest='operate', choices=[0, 1])

        res = parser.parse_args()

        if res.operate == 1:
            user = CompanyUser.query.get(user_id)
            user.enable = res.operate
            message = success_api(message="启动成功")
        else:
            user = CompanyUser.query.filter_by(id=res.user_id).update({"enable": res.operate})
            message = success_api(message="禁用成功")
        if user:
            db.session.commit()
        else:
            return fail_api(message="出错啦")
        return message


class UserAvatarResource(Resource):
    """修改头像"""

    def put(self, user_id):
        url = request.json.get("avatar").get("src")
        ret = CompanyUser.query.get(user_id)
        ret.avatar = url
        db.session.commit()
        if not ret:
            return fail_api(message="出错啦")
        return success_api(message="修改成功")


class UserInfoResource(Resource):

    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('realName', type=str, dest='real_name')
        parser.add_argument('username', type=str)
        parser.add_argument('remark', type=str)
        parser.add_argument('details', type=str)

        res = parser.parse_args()

        ret = CompanyUser.query.get(user_id)
        ret.username = res.username
        ret.realname = res.real_name
        ret.remark = res.details
        db.session.commit()
        if not ret:
            return fail_api(message="出错啦")
        return success_api(message="更新成功")


class UserPasswordResource(Resource):
    """前用户密码"""

    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('oldPassword', type=str, required=True, help='旧密码不得为空')
        parser.add_argument('newPassword', type=str, required=True, help='新密码不得为空')
        parser.add_argument('confirmPassword', type=str, required=True, help='确认密码不能为空')

        res = parser.parse_args()

        if res.newPassword != res.confirmPassword:
            return fail_api(message='确认密码不一致')

        """ 修改当前用户密码 """
        user = CompanyUser.query.get(user_id)
        is_right = user.validate_password(res.oldPassword)
        if not is_right:
            return jsonify(success=False, message="旧密码错误")
        user.set_password(res.newPassword)
        db.session.add(user)
        db.session.commit()

        return jsonify(success=True, message="更改成功")
