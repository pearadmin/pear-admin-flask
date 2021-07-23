from flask import jsonify
from flask_restful import Api, Resource
from applications.api import api_bp
from applications.common.utils.http import success_api, fail_api
from applications.common.utils.rights import authorize
from applications.extensions import db
from applications.models import Dept, User
from flask_restful import marshal, reqparse
from applications.common.serialization import dept_fields

dept_api = Api(api_bp, prefix='/dept')


@dept_api.resource('/add')
class AddDepartment(Resource):

    @authorize("admin:dept:add", log=True)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('address', type=str)
        parser.add_argument('deptName', type=str, dest='dept_name')
        parser.add_argument('email', type=str)
        parser.add_argument('leader', type=str)
        parser.add_argument('parentId', type=int, dest='parent_id')
        parser.add_argument('phone', type=str)
        parser.add_argument('sort', type=int)
        parser.add_argument('status', type=int)

        res = parser.parse_args()

        dept = Dept(
            parent_id=res.parent_id,
            dept_name=res.dept_name,
            sort=res.sort,
            leader=res.leader,
            phone=res.phone,
            email=res.email,
            status=res.status,
            address=res.address
        )
        db.session.add(dept)
        db.session.commit()

        return success_api(msg="成功")


@dept_api.resource('/edit/<int:dept_id>')
class DeptURD(Resource):
    @authorize("admin:dept:edit", log=True)
    def get(self, dept_id):
        dept = Dept.query.filter_by(id=dept_id).first()
        dept_data = {
            'id': dept.id,
            'dept_name': dept.dept_name,
            'leader': dept.leader,
            'email': dept.email,
            'phone': dept.phone,
            'status': dept.status,
            'sort': dept.sort,
            'address': dept.address,
        }
        # return make_response(render_template('department/edit.html', dept=dept))
        return jsonify(success=True, msg='ok', dept=dept_data)

    @authorize("admin:dept:edit", log=True)
    def put(self, dept_id):
        parser = reqparse.RequestParser()
        parser.add_argument('address', type=str)
        parser.add_argument('deptName', type=str, dest='dept_name')
        parser.add_argument('email', type=str)
        parser.add_argument('leader', type=str)
        parser.add_argument('phone', type=str)
        parser.add_argument('sort', type=int)
        parser.add_argument('status', type=int)

        res = parser.parse_args()
        data = {
            "dept_name": res.dept_name,
            "sort": res.sort,
            "leader": res.leader,
            "phone": res.phone,
            "email": res.email,
            "status": res.status,
            "address": res.address
        }
        res = Dept.query.filter_by(id=dept_id).update(data)
        if not res:
            return fail_api(msg="更新失败")
        db.session.commit()
        return success_api(msg="更新成功")

    @authorize("admin:dept:remove", log=True)
    def delete(self, dept_id):
        ret = Dept.query.filter_by(id=dept_id).delete()
        User.query.filter_by(dept_id=dept_id).update({"dept_id": None})
        db.session.commit()
        if ret:
            return success_api(msg="删除成功")
        return fail_api(msg="删除失败")


@dept_api.resource('/data')
class DeptData(Resource):

    @authorize("admin:dept:main", log=True)
    def get(self):
        dept_data = Dept.query.order_by(Dept.sort).all()
        res = {
            "data": marshal(dept_data, dept_fields)
        }
        return jsonify(res)


@dept_api.resource('/tree')
class DeptTree(Resource):

    @authorize("admin:dept:main", log=True)
    def get(self):
        dept_data = Dept.query.order_by(Dept.sort).all()
        res = {
            "status": {"code": 200, "message": "默认"},
            "data": marshal(dept_data, dept_fields)
        }
        return jsonify(res)


@dept_api.resource('/enable')
class DeptEnable(Resource):
    @authorize("admin:dept:edit", log=True)
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('deptId', type=int, dest='dept_id', required=True)
        parser.add_argument('operate', type=int, choices=[0, 1], required=True)

        res = parser.parse_args()
        d = Dept.query.filter_by(id=res.dept_id).update({"status": res.operate})
        if d:
            db.session.commit()
            message = '启用成功' if res.operate else '禁用成功'
            return success_api(msg=message)
        return fail_api(msg="出错啦")
