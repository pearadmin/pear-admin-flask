from flask import render_template, request, jsonify, make_response
from flask_restful import Resource

from . import rights_bp, rights_api, rights_curd
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
    """获取增加视图"""
    return render_template('admin/power/add.html')


@rights_bp.get('/selectParent')
@authorize("admin:power:main", log=True)
def select_parent():
    """获取选择父节点"""
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


@rights_api.resource('/power/<int:power_id>')
class RightsURD(Resource):
    @authorize("admin:power:edit", log=True)
    def get(self, power_id):
        power = rights_curd.get_power_by_id(power_id)
        icon = str(power.icon).split()
        if len(icon) == 2:
            icon = icon[1]
        else:
            icon = None
        return make_response(render_template('admin/power/edit.html', power=power, icon=icon))

    @authorize("admin:power:remove", log=True)
    def delete(self, power_id):
        r = rights_curd.remove_power(power_id)
        if r:
            return success_api(msg="删除成功")
        else:
            return fail_api(msg="删除失败")

    @authorize("admin:power:edit", log=True)
    def put(self, power_id):
        res = rights_curd.update_power(request.json)
        if not res:
            return fail_api(msg="更新权限失败")
        return success_api(msg="更新权限成功")


# 启用权限
@rights_bp.put('/enable')
@authorize("admin:power:edit", log=True)
def enable():
    power_id = request.json.get('powerId')
    if id:
        res = rights_curd.enable_status(power_id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="启用成功")
    return fail_api(msg="数据错误")


# 禁用权限
@rights_bp.put('/disable')
@authorize("admin:power:edit", log=True)
def dis_enable():
    _id = request.json.get('powerId')
    if _id:
        res = rights_curd.disable_status(_id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="禁用成功")
    return fail_api(msg="数据错误")


# 批量删除
@rights_bp.delete('/batchRemove')
@authorize("admin:power:remove", log=True)
def batch_remove():
    ids = request.form.getlist('ids[]')
    rights_curd.batch_remove(ids)
    return success_api(msg="批量删除成功")
