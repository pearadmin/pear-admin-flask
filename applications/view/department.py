from flask import render_template, request

from applications.common.utils.rights import authorize
from applications.models import CompanyDepartment
from applications.view import index_bp


@index_bp.get('/dept')
@authorize("admin:dept:main", log=True)
def dept_index():
    return render_template('admin/department/main.html')


@index_bp.get('/dept/add')
@authorize("admin:dept:add", log=True)
def add():
    return render_template('admin/department/add.html')


@index_bp.get('/dept/edit')
@authorize("admin:dept:edit", log=True)
def edit():
    dept_id = request.args.get("deptId", type=int)
    dept = CompanyDepartment.query.get(dept_id)
    return render_template('admin/department/edit.html', dept=dept)
