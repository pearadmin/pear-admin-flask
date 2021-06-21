from flask import render_template, request, jsonify

from . import rights_bp
from ...common.admin import rights_curd
from ...common.utils.http import success_api, fail_api
from ...common.utils.rights import authorize


@rights_bp.get('/')
@authorize("admin:power:main", log=True)
def index():
    return render_template('admin/power/main.html')


@rights_bp.get('/data')
@authorize("admin:power:main", log=True)
def data():
    power_data = rights_curd.get_power_dict()
    res = {
        "data": power_data
    }
    return jsonify(res)


@rights_bp.get('/add')
@authorize("admin:power:add", log=True)
def add():
    return render_template('admin/power/add.html')


@rights_bp.get('/selectParent')
@authorize("admin:power:main", log=True)
def select_parent():
    power_data = rights_curd.select_parent()
    res = {
        "status": {"code": 200, "message": "默认"},
        "data": power_data

    }
    return jsonify(res)


# 增加
@rights_bp.post('/save')
@authorize("admin:power:add", log=True)
def save():
    req = request.json
    rights_curd.save_power(req)
    return success_api(msg="成功")


# 权限编辑
@rights_bp.get('/edit/<int:_id>')
@authorize("admin:power:edit", log=True)
def edit(_id):
    power = rights_curd.get_power_by_id(_id)
    icon = str(power.icon).split()
    if len(icon) == 2:
        icon = icon[1]
    else:
        icon = None
    return render_template('admin/power/edit.html', power=power, icon=icon)


# 权限更新
@rights_bp.put('/update')
@authorize("admin:power:edit", log=True)
def update():
    res = rights_curd.update_power(request.json)
    if not res:
        return fail_api(msg="更新权限失败")
    return success_api(msg="更新权限成功")


# 启用权限
@rights_bp.put('/enable')
@authorize("admin:power:edit", log=True)
def enable():
    _id = request.json.get('powerId')
    if id:
        res = rights_curd.enable_status(_id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="启用成功")
    return fail_api(msg="数据错误")


# 禁用权限
@rights_bp.put('/disable')
@authorize("admin:power:edit", log=True)
def dis_enable():
    _id = request.json.get('powerId')
    if id:
        res = rights_curd.disable_status(_id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="禁用成功")
    return fail_api(msg="数据错误")


# 权限删除
@rights_bp.delete('/remove/<int:_id>')
@authorize("admin:power:remove", log=True)
def remove(_id):
    r = rights_curd.remove_power(_id)
    if r:
        return success_api(msg="删除成功")
    else:
        return fail_api(msg="删除失败")


# 批量删除
@rights_bp.delete('/batchRemove')
@authorize("admin:power:remove", log=True)
def batch_remove():
    ids = request.form.getlist('ids[]')
    rights_curd.batch_remove(ids)
    return success_api(msg="批量删除成功")


"""
    https://developer.aliyun.com/article/778501
    四位权限值： 增删改查
    八位部门值： 流量 接待&转化 讲师 运营 1111 1111
    四位公司值： 
"""
