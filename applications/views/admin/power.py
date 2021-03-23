from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from applications.service.admin.power import get_power_dict, select_parent, save_power, remove_power, get_power_by_id, \
    update_power
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
    return jsonify(msg="成功", success=True)


# 权限删除
@admin_power.route('/remove/<int:id>', methods=['DELETE'])
@authorize_and_log("admin:power:remove")
def remove(id):
    r = remove_power(id)
    if r:
        return jsonify(success=True, msg="删除成功")
    else:
        return jsonify(success=False, msg="删除失败")


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
        return jsonify(success=False, msg="更新权限失败")
    return jsonify(success=True, msg="更新权限成功")
