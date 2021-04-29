from flask import Blueprint, render_template, request, jsonify
from applications.service.admin.power import get_power_dict, select_parent, save_power, remove_power, get_power_by_id, \
    update_power, enable_status, disable_status, batch_remove
from applications.service.common.response import success_api, fail_api
from applications.service.route_auth import authorize_and_log

admin_power = Blueprint('adminPower', __name__, url_prefix='/admin/power')


@admin_power.route('/')
@authorize_and_log("admin:power:main")
def index():
    return render_template('admin/power/main.html')


@admin_power.route('/data')
@authorize_and_log("admin:power:main")
def data():
    power_data = get_power_dict()
    res = {
        "data": power_data
    }
    return jsonify(res)


@admin_power.route('/add')
@authorize_and_log("admin:power:add")
def add():
    return render_template('admin/power/add.html')


@admin_power.route('/selectParent')
@authorize_and_log("admin:power:main")
def selectParent():
    power_data = select_parent()
    res = {
        "status": {"code": 200, "message": "默认"},
        "data": power_data

    }
    return jsonify(res)


# 增加
@admin_power.route('/save', methods=['POST'])
@authorize_and_log("admin:power:add")
def save():
    req = request.json
    save_power(req)
    return success_api(msg="成功")


# 权限编辑
@admin_power.route('/edit/<int:id>', methods=['GET', 'POST'])
@authorize_and_log("admin:power:edit")
def edit(id):
    power = get_power_by_id(id)
    icon = str(power.icon).split()
    if len(icon) == 2:
        icon = icon[1]
    else:
        icon = None
    return render_template('admin/power/edit.html', power=power, icon=icon)


# 权限更新
@admin_power.route('/update', methods=['PUT'])
@authorize_and_log("admin:power:edit")
def update():
    res = update_power(request.json)
    if not res:
        return fail_api(msg="更新权限失败")
    return success_api(msg="更新权限成功")


# 启用用户
@admin_power.route('/enable', methods=['PUT'])
@authorize_and_log("admin:power:edit")
def enable():
    id = request.json.get('powerId')
    print(id)
    if id:
        res = enable_status(id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="启动成功")
    return fail_api(msg="数据错误")


# 禁用用户
@admin_power.route('/disable', methods=['PUT'])
@authorize_and_log("admin:power:edit")
def disenable():
    id = request.json.get('powerId')
    print(id)
    if id:
        res = disable_status(id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="禁用成功")
    return fail_api(msg="数据错误")


# 权限删除
@admin_power.route('/remove/<int:id>', methods=['DELETE'])
@authorize_and_log("admin:power:remove")
def remove(id):
    r = remove_power(id)
    if r:
        return success_api(msg="删除成功")
    else:
        return fail_api(msg="删除失败")


# 批量删除
@admin_power.route('/batchRemove', methods=['DELETE'])
@authorize_and_log("admin:power:remove")
def batchRemove():
    ids = request.form.getlist('ids[]')
    batch_remove(ids)
    return success_api(msg="批量删除成功")
