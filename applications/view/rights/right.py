from flask import render_template, request, jsonify, make_response
from flask_restful import Resource, reqparse

from . import rights_bp, rights_api, right_curd
from ...common.utils.http import success_api, fail_api
from ...common.utils.rights import authorize
from ...extensions import db
from ...models import Power


@rights_bp.get('/')
@authorize("admin:power:main", log=True)
def index():
    return render_template('admin/rights/main.html')


@rights_bp.get('/data')
@authorize("admin:power:main", log=True)
def data():
    power_data = right_curd.get_power_dict()
    res = {
        "data": power_data
    }
    return jsonify(res)


@rights_api.resource('/power')
class AddRight(Resource):
    @authorize("admin:power:add", log=True)
    def get(self):
        """获取增加视图"""
        return make_response(render_template('admin/rights/add.html'))

    @authorize("admin:power:add", log=True)
    def post(self):
        req = request.json
        right_curd.save_power(req)
        return success_api(msg="成功")


@rights_bp.get('/selectParent')
@authorize("admin:power:main", log=True)
def select_parent():
    """获取选择父节点"""
    power_data = right_curd.select_parent()
    res = {
        "status": {"code": 200, "message": "默认"},
        "data": power_data

    }
    return jsonify(res)


@rights_api.resource('/power/<int:power_id>')
class RightsURD(Resource):
    @authorize("admin:power:edit", log=True)
    def get(self, power_id):
        power = right_curd.get_power_by_id(power_id)
        icon = str(power.icon).split()
        if len(icon) == 2:
            icon = icon[1]
        else:
            icon = None
        return make_response(render_template('admin/rights/edit.html', power=power, icon=icon))

    @authorize("admin:power:remove", log=True)
    def delete(self, power_id):
        r = right_curd.remove_power(power_id)
        if r:
            return success_api(msg="删除成功")
        else:
            return fail_api(msg="删除失败")

    @authorize("admin:power:edit", log=True)
    def put(self, power_id):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('icon', type=str)
        parser.add_argument('openType', type=str, dest='open_type')
        parser.add_argument('parentId', type=str, dest='parent_id')
        parser.add_argument('powerCode', type=str, dest='power_code')
        parser.add_argument('powerName', type=str, dest='power_name')
        parser.add_argument('powerType', type=str, dest='power_type')
        parser.add_argument('powerUrl', type=str, dest='power_url')
        parser.add_argument('sort', type=int, dest='sort')

        res = parser.parse_args()
        data = {
            "icon": res.icon,
            "open_type": res.open_type,
            "parent_id": res.parent_id,
            "code": res.power_code,
            "name": res.power_name,
            "type": res.power_type,
            "url": res.power_url,
            "sort": res.sort
        }
        power = Power.query.filter_by(id=power_id).update(data)
        db.session.commit()

        if not power:
            return fail_api(msg="更新权限失败")
        return success_api(msg="更新权限成功")


# 启用权限
@rights_bp.put('/enable')
@authorize("admin:power:edit", log=True)
def enable():
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('powerId', dest='power_id', type=int, required=True)
    parser.add_argument('operate', type=int, required=True, choices=[0, 1])

    res = parser.parse_args()

    power = Power.query.filter_by(id=res.power_id).update({"enable": res.operate})
    if power:
        db.session.commit()
        message = "启用成功" if res.operate else '禁用成功'
        return success_api(msg=message)
    else:
        return fail_api(msg="出错啦")


# 批量删除
@rights_bp.delete('/batchRemove')
@authorize("admin:power:remove", log=True)
def batch_remove():
    ids = request.form.getlist('ids[]')
    right_curd.batch_remove(ids)
    return success_api(msg="批量删除成功")
