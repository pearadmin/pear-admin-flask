from flask import jsonify
from flask_login import login_required
from flask_restful import Resource, Api, reqparse, marshal

from applications.common.utils.http import table_api, success_api, fail_api
from applications.common.utils.rights import authorize
from applications.common.serialization import power_fields

from applications.extensions import db
from applications.models import RightsPower, RightsRole, CompanyUser
from . import api_bp


def remove_role(role_id):
    """ 删除角色 """
    role = RightsRole.query.filter_by(id=role_id).first()
    # 删除该角色的权限
    power_id_list = []
    for p in role.power:
        power_id_list.append(p.id)

    powers = RightsPower.query.filter(RightsPower.id.in_(power_id_list)).all()
    for p in powers:
        role.power.remove(p)
    user_id_list = []
    for u in role.user:
        user_id_list.append(u.id)
    users = CompanyUser.query.filter(CompanyUser.id.in_(user_id_list)).all()
    for u in users:
        role.user.remove(u)
    r = RightsRole.query.filter_by(id=role_id).delete()
    db.session.commit()
    return r


def batch_remove_role(role_ids):
    """ 批量删除 """
    for role_id in role_ids:
        remove_role(role_id)


role_api = Api(api_bp, prefix='/roles')


@role_api.resource('/roles')
class RoleRoles(Resource):
    # 表格数据
    @authorize("admin:role:main", log=True)
    def get(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('limit', type=int, default=10)
        parser.add_argument('roleName', type=str, dest='role_name', default="")
        parser.add_argument('roleCode', type=str, dest='role_code', default="")

        res = parser.parse_args()

        filters = []
        if res.role_name:
            filters.append(RightsRole.name.like('%' + res.role_name + '%'))
        if res.role_code:
            filters.append(RightsRole.code.like('%' + res.role_code + '%'))

        paginate = RightsRole.query.filter(*filters).paginate(page=res.page, per_page=res.limit, error_out=False)

        return table_api(data=[
            {
                'id': item.id,
                'roleName': item.name,
                'roleCode': item.code,
                'enable': item.enable,
                'remark': item.remark,
                'details': item.details,
                'sort': item.sort,
                'create_at': item.create_at,
            } for item in paginate.items
        ], count=paginate.total, code=0)

    @authorize("admin:role:remove", log=True)
    @login_required
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ids[]', action='append', dest='ids')

        res = parser.parse_args()

        batch_remove_role(res.ids)
        return success_api(msg="批量删除成功")


@role_api.resource('/role/<int:role_id>')
class RoleRole(Resource):

    @authorize("admin:role:add", log=True)
    def post(self, role_id):
        parser = reqparse.RequestParser()
        parser.add_argument('details', type=str)
        parser.add_argument('enable', type=int)
        parser.add_argument('roleCode', type=str, dest='role_code')
        parser.add_argument('roleName', type=str, dest='role_name')
        parser.add_argument('sort', type=int)

        res = parser.parse_args()

        role = RightsRole(
            details=res.details,
            enable=res.enable,
            code=res.role_code,
            name=res.role_name,
            sort=res.sort
        )
        db.session.add(role)
        db.session.commit()
        return success_api(msg="成功")

    # 更新角色
    @authorize("admin:role:edit", log=True)
    def put(self, role_id):
        parser = reqparse.RequestParser()
        parser.add_argument('roleId', dest='role_id', type=int)
        parser.add_argument('roleCode', dest='role_code', type=str)
        parser.add_argument('roleName', dest='role_name', type=str)
        parser.add_argument('sort', type=int)
        parser.add_argument('enable', type=int)
        parser.add_argument('details', type=str)

        res = parser.parse_args()

        data = {
            "code": res.role_code,
            "name": res.role_name,
            "sort": res.sort,
            "enable": res.enable,
            "details": res.details
        }

        role = RightsRole.query.filter_by(id=role_id).update(data)
        db.session.commit()
        if not role:
            return fail_api(msg="更新角色失败")
        return success_api(msg="更新角色成功")


@role_api.resource('/role/<int:role_id>/status')
class RoleEnable(Resource):
    """启用用户"""

    @authorize("admin:role:edit", log=True)
    def put(self, role_id):
        ret = RightsRole.query.get(role_id)
        ret.enable = not ret.enable
        db.session.commit()

        message = "修改成功"
        if not ret:
            return fail_api(msg="出错啦")
        return success_api(msg=message)


@role_api.resource('/role_power/<int:role_id>')
class RolePower(Resource):

    @authorize("admin:role:main", log=True)
    def get(self, role_id):
        # 获取角色权限
        role = RightsRole.query.filter_by(id=role_id).first()
        # 获取权限列表的 id
        check_powers_list = [rp.id for rp in role.power]
        powers = RightsPower.query.all()  # 获取所有的权限
        # power_schema = PowerSchema2(many=True)  # 用已继承 ma.ModelSchema 类的自定制类生成序列化类
        # 将所有的权限生产可序列化对象 json
        # powers = power_schema.dump(powers)  # 生成可序列化对象
        powers = marshal(powers, power_fields)
        for i in powers:
            if int(i.get("powerId")) in check_powers_list:
                i["checkArr"] = "1"
            else:
                i["checkArr"] = "0"
        res = {
            "data": powers,
            "status": {"code": 200, "message": "默认"}
        }
        return jsonify(res)

    # 保存角色权限
    @authorize("admin:role:edit", log=True)
    def put(self, role_id):
        parser = reqparse.RequestParser()
        parser.add_argument('powerIds', dest='power_ids')
        parser.add_argument('roleId', dest='role_id')

        res = parser.parse_args()
        power_list = res.power_ids.split(',')

        """ 更新角色权限 """
        role = RightsRole.query.filter_by(id=role_id).first()
        power_id_list = []
        for p in role.power:
            power_id_list.append(p.id)
        powers = RightsPower.query.filter(RightsPower.id.in_(power_id_list)).all()
        for p in powers:
            role.power.remove(p)
        powers = RightsPower.query.filter(RightsPower.id.in_(power_list)).all()
        for p in powers:
            role.power.append(p)
        db.session.commit()
        return success_api(msg="授权成功")

    # 角色删除
    @authorize("admin:role:remove", log=True)
    def delete(self, role_id):
        print(role_id)
        res = remove_role(role_id)
        print(res)
        if not res:
            return fail_api(msg="角色删除失败")
        return success_api(msg="角色删除成功")
