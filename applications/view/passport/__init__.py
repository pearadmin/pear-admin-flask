from flask import Blueprint, session
from flask_login import login_required, logout_user

from applications.common.utils.http import success_api
from ._utils import get_captcha_image, add_auth_session

passport_bp = Blueprint('passport', __name__, url_prefix='/passport')


# 获取验证码
@passport_bp.get('/getCaptcha')
def get_captcha():
    resp, code = get_captcha_image()
    session["code"] = code
    return resp


# 退出登录
@passport_bp.post('/logout')
@login_required
def logout():
    logout_user()
    session.pop('permissions')
    return success_api(msg="注销成功")


from . import api
