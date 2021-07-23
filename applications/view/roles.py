from flask import Blueprint, render_template

from applications.common.utils.rights import authorize

from applications.models import Role

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


# 角色编辑
@authorize("admin:role:edit", log=True)
@role_bp.get('/edit/<int:role_id>')
def role_editor(role_id):
    role = Role.query.filter_by(id=role_id).first()
    return render_template('roles/edit.html', role=role)
