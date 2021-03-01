from io import BytesIO
from flask import Blueprint, render_template, jsonify, request, session, make_response
from flask_login import login_user, login_required, logout_user, current_user
from applications.models.admin import User
from applications.service.CaptchaTool import gen_captcha
from applications.service.menuTreeYaml import make_tree
from flask_marshmallow import Marshmallow
from applications.service.route_auth import check_auth

admin_index = Blueprint('adminIndex', __name__, url_prefix='/admin')

ma = Marshmallow()


#                               ----------------------------------------------------------
#                               -------------------------  首页 --------------------------
#                               ----------------------------------------------------------

@admin_index.route('/')
@login_required
@check_auth(['管理员','普通用户','游客'])
def index():
    username = current_user.username
    return render_template('admin/index.html', username=username)


#                               ----------------------------------------------------------
#                               -------------------------  获取验证码 ----------------------
#                               ----------------------------------------------------------


@admin_index.route('/getCaptcha', methods=["GET"])
def get_captcha():
    code, image = gen_captcha()
    out = BytesIO()
    session["code"] = code
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp


#                               ==========================================================
#                                                             登录
#                               ==========================================================


@admin_index.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        code = request.form.get('code')

        if not username or not password or not code:
            res = {"msg": "用户名或密码没有输入", "code": 0}
            return jsonify(res)

        s_code = session.get("code", None)
        if not all([code, s_code]):
            return {"msg": "参数错误", "code": 0}
        if code != s_code:
            return {"msg": "验证码错误", "code": 0}

        user = User.query.filter_by(username=username).first()
        if user is None:
            res = {"msg": "不存在的用户", "code": 0}
            return jsonify(res)
        if user.status is 0:
            res = {"msg": "用户被暂停使用", "code": 0}
            return jsonify(res)

        if username == user.username and user.validate_password(password):
            login_user(user)
            res = {"msg": "登录成功", "code": 1}
            return jsonify(res)

        res = {"msg": "用户名或密码错误", "code": 0}
        #  return redirect(url_for('login'))
        return jsonify(res)

    return render_template('admin/login.html')


#                               ==========================================================
#                                                             退出登录
#                               ==========================================================


@admin_index.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    res = {"msg": "注销成功", "code": 200}
    return jsonify(res)


#                               ==========================================================
#                                                             生成目录树
#                               ==========================================================


@admin_index.route('/menu')
@login_required
def menu():
    menu_yaml = admin_index.root_path + "/../../config/menu/*.yaml"
    res = make_tree(menu_yaml, '管理员')
    return jsonify(res)


#                               ----------------------------------------------------------
#                               -------------------------  控制台页面 -----------------------
#                               ----------------------------------------------------------


@admin_index.route('/welcome')
@login_required
def welcome():
    return render_template('admin/console/console.html')
