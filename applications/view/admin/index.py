from flask import Blueprint, render_template
from flask_login import login_required, current_user

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


# 首页
@admin_bp.get('/')
@login_required
def index():
    user = current_user
    return render_template('admin/index.html', user=user)


# 控制台页面
@admin_bp.get('/welcome')
@login_required
def welcome():
    return render_template('admin/console/console.html')
