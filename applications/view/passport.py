from flask import Blueprint, session, redirect, render_template, url_for
from flask_login import login_required, logout_user, current_user

from applications.common.gen_captcha import get_captcha_image
from applications.common.utils.http import success_api

# 获取验证码
from applications.view import index_bp


@index_bp.get('/passport/getCaptcha')
def get_captcha():
    resp, code = get_captcha_image()
    session["code"] = code
    return resp


# 退出登录
@index_bp.post('/passport/logout')
@login_required
def logout():
    logout_user()
    session.pop('permissions')
    return success_api(message="注销成功")


@index_bp.get('/passport/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))
    # TODO 分离视图操作 最终实现接口登录与视图登录两套逻辑
    return render_template('index/login.html')
