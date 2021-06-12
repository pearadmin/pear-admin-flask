from flask import Blueprint, render_template, request, jsonify
from marshmallow import INCLUDE

from applications.common.utils.http import success_api, fail_api
from applications.common.utils.rights import authorize
from applications.common.utils.validate import check_data
from applications.models import DeptSchema
from applications.common.admin import dept_curd as dept_curd

admin_dept = Blueprint('adminDept', __name__, url_prefix='/admin/dept')


@admin_dept.get('/')
@authorize("admin:dept:main", log=True)
def main():
    return render_template('admin/dept/main.html')


@admin_dept.get('/data')
@authorize("admin:dept:main", log=True)
def data():
    power_data = dept_curd.get_dept_dict()
    res = {
        "data": power_data
    }
    return jsonify(res)


@admin_dept.get('/add')
@authorize("admin:dept:add", log=True)
def add():
    return render_template('admin/dept/add.html')


@admin_dept.get('/tree')
@authorize("admin:dept:main", log=True)
def tree():
    power_data = dept_curd.get_dept_dict()
    res = {
        "status": {"code": 200, "message": "默认"},
        "data": power_data

    }
    return jsonify(res)


@admin_dept.post('/save')
@authorize("admin:dept:add", log=True)
def save():
    req = request.json
    check_data(DeptSchema(unknown=INCLUDE), req)
    dept_curd.save_dept(req)
    return success_api(msg="成功")


@admin_dept.get('/edit')
@authorize("admin:dept:edit", log=True)
def edit():
    _id = request.args.get("deptId")
    dept = dept_curd.get_dept_by_id(_id)
    return render_template('admin/dept/edit.html', dept=dept)


# 启用
@admin_dept.put('/enable')
@authorize("admin:dept:edit", log=True)
def enable():
    _id = request.json.get('deptId')
    if id:
        res = dept_curd.enable_status(_id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="启用成功")
    return fail_api(msg="数据错误")


# 禁用
@admin_dept.put('/disable')
@authorize("admin:dept:edit", log=True)
def dis_enable():
    _id = request.json.get('deptId')
    if id:
        res = dept_curd.disable_status(_id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="禁用成功")
    return fail_api(msg="数据错误")


@admin_dept.put('/update')
@authorize("admin:dept:edit", log=True)
def update():
    req = request.json
    check_data(DeptSchema(unknown=INCLUDE), req)
    res = dept_curd.update_dept(req)
    if not res:
        return fail_api(msg="更新失败")
    return success_api(msg="更新成功")


@admin_dept.delete('/remove/<int:_id>')
@authorize("admin:dept:remove", log=True)
def remove(_id):
    res = dept_curd.remove_dept(_id)
    if res:
        return success_api(msg="删除成功")
    else:
        return fail_api(msg="删除失败")
