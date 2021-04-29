from flask import Blueprint, render_template, jsonify, request, session, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from applications.service.admin.index import add_auth_session, make_menu_tree, get_captcha
from applications.service.admin_log import login_log
from applications.models.admin_user import User
from applications.service.common.response import fail_api, success_api

admin_index = Blueprint('adminIndex', __name__, url_prefix='/admin')


# 首页
@admin_index.route('/')
@login_required
def index():
    user = current_user
    return render_template('admin/index.html', user=user)


# 获取验证码
@admin_index.route('/getCaptcha', methods=["GET"])
def getCaptcha():
    resp,code=get_captcha()
    session["code"] = code
    return resp


# 登录
@admin_index.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        req = request.form
        username = req.get('username')
        password = req.get('password')
        code = req.get('captcha')

        if not username or not password or not code:
            return fail_api(msg="用户名或密码没有输入")
        s_code = session.get("code", None)

        if not all([code, s_code]):
            return fail_api(msg="参数错误")

        if code != s_code:
            return fail_api(msg="验证码错误")
        user = User.query.filter_by(username=username).first()

        if user is None:
            return fail_api(msg="不存在的用户")

        if user.enable is 0:
            return  fail_api(msg="用户被暂停使用")

        if username == user.username and user.validate_password(password):
            # 登录
            login_user(user)
            # 记录登录日志
            login_log(request, uid=user.id, is_access=True)
            # 存入权限
            add_auth_session()
            return success_api(msg="登录成功")
        login_log(request,uid=user.id, is_access=False)
        return fail_api(msg="用户名或密码错误")
    if current_user.is_authenticated:
        return redirect(url_for('adminIndex.index'))
    return render_template('admin/login.html')


# 退出登录
@admin_index.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    session.pop('permissions')
    return success_api(msg="注销成功")


# 菜单
@admin_index.route('/menu')
@login_required
def menu():
    menu_tree = make_menu_tree()
    return jsonify(menu_tree)


# 控制台页面
@admin_index.route('/welcome')
@login_required
def welcome():
    return render_template('admin/console/console.html')
