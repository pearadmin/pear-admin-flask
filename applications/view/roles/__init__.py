from flask import Blueprint, render_template

from applications.common.utils.rights import authorize

from applications.view.roles._utils import remove_role, batch_remove_role

role_bp = Blueprint('role', __name__, url_prefix='/admin/role')


# 角色而管理
@role_bp.get('/')
@authorize("admin:role:main", log=True)
def main():
    return render_template('roles/main.html')


# 角色授权操作
@role_bp.get('/power/<int:_id>')
@authorize("admin:role:power", log=True)
def power(_id):
    return render_template('roles/power.html', id=_id)


from . import role