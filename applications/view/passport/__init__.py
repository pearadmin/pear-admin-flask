from flask import Blueprint, session, redirect, url_for, render_template, request, make_response
from flask_login import current_user, login_user, login_required, logout_user
from flask_restful import Resource, Api, reqparse
from applications.common.admin import index_curd
from applications.common.admin_log import login_log
from applications.common.utils.http import fail_api, success_api
from applications.models import User

passport_bp = Blueprint('passport', __name__, url_prefix='/passport')
passport_api = Api(passport_bp)


def register_passport_views(app):
    app.register_blueprint(passport_bp)


# 获取验证码
@passport_bp.get('/getCaptcha')
def get_captcha():
    resp, code = index_curd.get_captcha()
    session["code"] = code
    return resp


@passport_api.resource('/login')
class Login(Resource):
    login_req = reqparse.RequestParser(bundle_errors=True)
    login_req.add_argument('username', type=str, help='请输入用户名', required=True)
    login_req.add_argument('password', type=str, help='请输入密码', required=True)
    login_req.add_argument('captcha', type=str, help='请输入验证码', required=True)

    def get(self):
        if current_user.is_authenticated:
            return redirect(url_for('admin.index'))

        return make_response(render_template('admin/login.html'))

    def post(self):

        req = self.login_req.parse_args()

        s_code = session.get("code", None)

        if req.captcha != s_code:
            return fail_api(msg="验证码错误")
        user = User.query.filter_by(username=req.username).first()

        if user is None:
            return fail_api(msg="不存在的用户")

        if user.enable is 0:
            return fail_api(msg="用户被暂停使用")

        if user.validate_password(req.password):
            # 登录
            login_user(user)
            # 记录登录日志
            login_log(request, uid=user.id, is_access=True)
            # 存入权限
            index_curd.add_auth_session()
            return success_api(msg="登录成功")
        login_log(request, uid=user.id, is_access=False)
        return fail_api(msg="用户名或密码错误")


# 退出登录
@passport_bp.post('/logout')
@login_required
def logout():
    logout_user()
    session.pop('permissions')
    return success_api(msg="注销成功")
