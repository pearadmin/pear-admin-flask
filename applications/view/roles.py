from flask import Blueprint, render_template

from applications.common.utils.rights import permission_required, view_logging_required

from applications.models import RightsRole

role_bp = Blueprint('role', __name__, url_prefix='/admin/role')


# 角色而管理
@role_bp.get('/')
@view_logging_required
@permission_required("admin:role:main")
def main():
    return render_template('admin/roles/roles.html')


# 角色授权操作
@role_bp.get('/power/<int:role_id>')
@view_logging_required
@permission_required("admin:role:power")
def power(role_id):
    return render_template('admin/roles/roles_power.html', role_id=role_id)


# 角色编辑
@role_bp.get('/edit/<int:role_id>')
@view_logging_required
@permission_required("admin:role:edit")
def role_editor(role_id):
    role = RightsRole.query.filter_by(id=role_id).first()
    return render_template('admin/roles/roles_edit.html', role=role)


@role_bp.get('/add')
@view_logging_required
@permission_required("admin:role:edit")
def role_add():
    return render_template('admin/roles/roles_add.html')
