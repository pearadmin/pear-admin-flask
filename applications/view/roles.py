from flask import Blueprint, render_template

from applications.common.utils.rights import authorize

from applications.models import RightsRole

role_bp = Blueprint('role', __name__, url_prefix='/admin/role')


# 角色而管理
@role_bp.get('/')
@authorize("admin:role:main", log=True)
def main():
    return render_template('admin/roles/roles.html')


# 角色授权操作
@role_bp.get('/power/<int:role_id>')
@authorize("admin:role:power", log=True)
def power(role_id):
    return render_template('admin/roles/roles_power.html', role_id=role_id)


# 角色编辑
@authorize("admin:role:edit", log=True)
@role_bp.get('/edit/<int:role_id>')
def role_editor(role_id):
    role = RightsRole.query.filter_by(id=role_id).first()
    return render_template('admin/roles/roles_edit.html', role=role)


@authorize("admin:role:edit", log=True)
@role_bp.get('/add')
def role_add():
    return render_template('admin/roles/roles_add.html')
