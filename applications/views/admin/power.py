from flask import Blueprint, render_template, request, jsonify
from applications.service.admin import power_curd
from applications.service.common.response import success_api, fail_api
from applications.service.route_auth import authorize

admin_power = Blueprint('adminPower', __name__, url_prefix='/admin/power')


@admin_power.get('/')
@authorize("admin:power:main", log=True)
def index():
    return render_template('admin/power/main.html')


@admin_power.get('/data')
@authorize("admin:power:main", log=True)
def data():
    power_data = power_curd.get_power_dict()
    res = {
        "data": power_data
    }
    return jsonify(res)


@admin_power.get('/add')
@authorize("admin:power:add", log=True)
def add():
    return render_template('admin/power/add.html')


@admin_power.get('/selectParent')
@authorize("admin:power:main", log=True)
def selectParent():
    power_data = power_curd.select_parent()
    res = {
        "status": {"code": 200, "message": "默认"},
        "data": power_data

    }
    return jsonify(res)


# 增加
@admin_power.post('/save')
@authorize("admin:power:add", log=True)
def save():
    req = request.json
    power_curd.save_power(req)
    return success_api(msg="成功")


# 权限编辑
@admin_power.get('/edit/<int:id>')
@authorize("admin:power:edit", log=True)
def edit(id):
    power = power_curd.get_power_by_id(id)
    icon = str(power.icon).split()
    if len(icon) == 2:
        icon = icon[1]
    else:
        icon = None
    return render_template('admin/power/edit.html', power=power, icon=icon)


# 权限更新
@admin_power.put('/update')
@authorize("admin:power:edit", log=True)
def update():
    res = power_curd.update_power(request.json)
    if not res:
        return fail_api(msg="更新权限失败")
    return success_api(msg="更新权限成功")


# 启用权限
@admin_power.put('/enable')
@authorize("admin:power:edit", log=True)
def enable():
    id = request.json.get('powerId')
    if id:
        res = power_curd.enable_status(id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="启用成功")
    return fail_api(msg="数据错误")


# 禁用权限
@admin_power.put('/disable')
@authorize("admin:power:edit", log=True)
def disenable():
    id = request.json.get('powerId')
    if id:
        res = power_curd.disable_status(id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="禁用成功")
    return fail_api(msg="数据错误")


# 权限删除
@admin_power.delete('/remove/<int:id>')
@authorize("admin:power:remove", log=True)
def remove(id):
    r = power_curd.remove_power(id)
    if r:
        return success_api(msg="删除成功")
    else:
        return fail_api(msg="删除失败")


# 批量删除
@admin_power.delete('/batchRemove')
@authorize("admin:power:remove", log=True)
def batchRemove():
    ids = request.form.getlist('ids[]')
    power_curd.batch_remove(ids)
    return success_api(msg="批量删除成功")
