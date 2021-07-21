from flask import Blueprint, render_template
from flask_login import login_required, current_user
from flask_restful import Api
from sqlalchemy import desc

from applications.common.utils.rights import authorize
from ...models import AdminLog

users_bp = Blueprint('users', __name__, url_prefix='/users')


# 用户增加
@users_bp.get('/')
@authorize("admin:user:main", log=True)
def get():
    return render_template('users/main.html')


@users_bp.get('/center')
@login_required
def center():
    user_logs = AdminLog.query.filter_by(url='/passport/login').filter_by(uid=current_user.id).order_by(
        desc(AdminLog.create_time)).limit(10)
    return render_template('users/profile.html', user_info=current_user, user_logs=user_logs)


user_api = Api(users_bp)
from . import profile, _utils
from . import user_view
