from flask import render_template, make_response
from flask import session, redirect, url_for, request
from flask_login import current_user, login_user
from flask_restful import Resource, reqparse

from applications.common.gen_captcha import add_auth_session
from applications.common.utils.http import fail_api, success_api
from applications.common.utils.rights import record_logging
from applications.models import CompanyUser


class Login(Resource):
    login_req = reqparse.RequestParser(bundle_errors=True)
    login_req.add_argument('username', type=str, help='请输入用户名', required=True)
    login_req.add_argument('password', type=str, help='请输入密码', required=True)
    login_req.add_argument('captcha', type=str, help='请输入验证码', required=True)

    def get(self):
        if current_user.is_authenticated:
            return redirect(url_for('admin.index'))
        # TODO 分离视图操作 最终实现接口登录与视图登录两套逻辑
        return make_response(render_template('index/login.html'))

    def post(self):

        req = self.login_req.parse_args()

        s_code = session.get("code", None)

        if req.captcha != s_code:
            return fail_api(msg="验证码错误")
        user = CompanyUser.query.filter_by(username=req.username).first()

        if user is None:
            return fail_api(msg="不存在的用户")

        if user.enable == 0:
            return fail_api(msg="用户被暂停使用")

        if user.validate_password(req.password):
            # 登录
            login_user(user)
            # 记录登录日志
            record_logging()

            # 存入权限
            add_auth_session()
            return success_api(msg="登录成功")
        record_logging()
        return fail_api(msg="用户名或密码错误")
