from flask import jsonify
from flask_restful import Resource
from flask_restful import marshal, reqparse

from applications.common.serialization import dept_fields
from applications.common.utils.http import success_api, fail_api
from applications.common.utils.rights import authorize
from applications.extensions import db
from applications.models import CompanyDepartment, CompanyUser


class Departments(Resource):

    @authorize("admin:dept:main", log=True)
    def get(self):
        dept_data = CompanyDepartment.query.order_by(CompanyDepartment.sort).all()
        # TODO dtree 需要返回状态信息
        res = {
            "status": {"code": 200, "message": "默认"},
            "data": marshal(dept_data, dept_fields)
        }
        print(dept_data)
        return jsonify(res)

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

        dept = CompanyDepartment(
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


class Department(Resource):
    @authorize("admin:dept:edit", log=True)
    def get(self, dept_id):
        dept = CompanyDepartment.query.filter_by(id=dept_id).first()
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
        res = CompanyDepartment.query.filter_by(id=dept_id).update(data)
        if not res:
            return fail_api(msg="更新失败")
        db.session.commit()
        return success_api(msg="更新成功")

    @authorize("admin:dept:remove", log=True)
    def delete(self, dept_id):
        ret = CompanyDepartment.query.filter_by(id=dept_id).delete()
        CompanyUser.query.filter_by(dept_id=dept_id).update({"dept_id": None})
        db.session.commit()
        if ret:
            return success_api(msg="删除成功")
        return fail_api(msg="删除失败")


class DeptEnable(Resource):
    @authorize("admin:dept:edit", log=True)
    def put(self, dept_id):
        d = CompanyDepartment.query.get(dept_id)
        if d:
            d.status = not d.status
            db.session.commit()
            message = '修改成功'
            return success_api(msg=message)
        return fail_api(msg="出错啦")
