from flask import Blueprint
from flask import render_template
from flask_login import login_required, current_user

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def index():
    return render_template('index/index.html')


# 首页
@index_bp.get('/admin/')
@login_required
def admin_index():
    return render_template('index/admin_index.html', user=current_user)


# 控制台页面
@index_bp.get('/admin/welcome')
@login_required
def welcome():
    return render_template('index/welcome.html')
