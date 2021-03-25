from flask import Blueprint, render_template, jsonify, request, session, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from applications.service.admin.index import add_auth_session, make_menu_tree, get_captcha
from applications.service.admin_log import login_log
from applications.models.admin import User

admin_index = Blueprint('adminIndex', __name__, url_prefix='/admin')


# 首页
@admin_index.route('/')
@login_required
def index():
    realname = current_user.realname
    return render_template('admin/index.html', realname=realname)


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
            return jsonify(msg="用户名或密码没有输入", code=0,success=False)
        s_code = session.get("code", None)

        if not all([code, s_code]):
            return jsonify(msg="参数错误", code=0,success=False)

        if code != s_code:
            return jsonify(msg="验证码错误", code=0,success=False)
        user = User.query.filter_by(username=username).first()

        if user is None:
            return jsonify(msg="不存在的用户", code=0,success=False)

        if user.enable is 0:
            return jsonify(msg="用户被暂停使用", code=0,success=False)

        if username == user.username and user.validate_password(password):
            # 登录
            login_user(user)
            # 记录登录日志
            login_log(request, uid=user.id, is_access=True)
            # 存入权限
            add_auth_session()
            return jsonify(msg="登录成功", code=1,success=True)
        login_log(request,uid=user.id, is_access=False)
        return jsonify(msg="用户名或密码错误", code=0,success=False)
    print(current_user.is_authenticated)
    if current_user.is_authenticated:
        return redirect(url_for('adminIndex.index'))
    return render_template('admin/login.html')


# 退出登录
@admin_index.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    session.pop('permissions')
    return jsonify(msg="注销成功", success=True)


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
