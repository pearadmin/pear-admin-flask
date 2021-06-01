from flask import Blueprint, render_template, request, jsonify
from applications.service.admin import dept as dept_curd
from applications.service.common.response import table_api, success_api, fail_api
from applications.service.route_auth import authorize_and_log, authorize

admin_dept = Blueprint('adminDept', __name__, url_prefix='/admin/dept')


@admin_dept.route('/')
@authorize_and_log("admin:dept:main")
def main():
    return render_template('admin/dept/main.html')


@admin_dept.route('/data')
@authorize_and_log("admin:dept:main")
def data():
    power_data = dept_curd.get_dept_dict()
    res = {
        "data": power_data
    }
    return jsonify(res)


@admin_dept.route('/add')
@authorize_and_log("admin:dept:add")
def add():
    return render_template('admin/dept/add.html')


@admin_dept.route('/tree')
@authorize_and_log("admin:dept:main")
def tree():
    power_data = dept_curd.get_dept_dict()
    res = {
        "status": {"code": 200, "message": "默认"},
        "data": power_data

    }
    return jsonify(res)


@admin_dept.route('/save', methods=['POST'])
@authorize_and_log("admin:dept:edit")
def save():
    req = request.json
    dept_curd.save_dept(req)
    return success_api(msg="成功")


@admin_dept.route('/edit', methods=['GET', 'POST'])
@authorize_and_log("admin:dept:edit")
def edit():
    id = request.args.get("deptId")
    dept = dept_curd.get_dept_by_id(id)
    return render_template('admin/dept/edit.html', dept=dept)


# 启用
@admin_dept.route('/enable', methods=['PUT'])
@authorize_and_log("admin:dept:edit")
def enable():
    id = request.json.get('deptId')
    if id:
        res = dept_curd.enable_status(id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="启用成功")
    return fail_api(msg="数据错误")


# 禁用
@admin_dept.route('/disable', methods=['PUT'])
@authorize_and_log("admin:dept:edit")
def disenable():
    id = request.json.get('deptId')
    if id:
        res = dept_curd.disable_status(id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="禁用成功")
    return fail_api(msg="数据错误")


@admin_dept.route('/update', methods=['PUT'])
@authorize_and_log("admin:dept:edit")
def update():
    res = dept_curd.update_dept(request.json)
    if not res:
        return fail_api(msg="更新失败")
    return success_api(msg="更新成功")


@admin_dept.route('/remove/<int:id>', methods=['DELETE'])
@authorize_and_log("admin:dept:remove")
def remove(id):
    res = dept_curd.remove_dept(id)
    if res:
        return success_api(msg="删除成功")
    else:
        return fail_api(msg="删除失败")
