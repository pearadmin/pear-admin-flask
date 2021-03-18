from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from applications.service.admin.power import get_power_dict, select_parent, save_power, remove_power

admin_power = Blueprint('adminPower', __name__, url_prefix='/admin/power')


@admin_power.route('/')
@login_required
def index():
    return render_template('admin/power/main.html')


@admin_power.route('/data')
@login_required
def data():
    power_data = get_power_dict()
    res = {
        "data": power_data
    }
    return jsonify(res)


@admin_power.route('/add')
@login_required
def add():
    return render_template('admin/power/add.html')


@admin_power.route('/selectParent')
def selectParent():
    power_data = select_parent()
    res = {
        "status": {"code": 200, "message": "默认"},
        "data": power_data

    }
    return jsonify(res)


@admin_power.route('/save', methods=['POST'])
def save():
    req = request.json
    save_power(req)
    return jsonify(msg="成功", success=True)


@admin_power.route('/remove/<int:id>', methods=['DELETE'])
def remove(id):
    r = remove_power(id)
    if r:
        return jsonify(success=True, msg="删除成功")
    else:
        return jsonify(success=False, msg="删除失败")
