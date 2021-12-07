from flask import jsonify
from flask_restful import Resource, reqparse

from applications.common.utils.http import success_api, fail_api
from applications.extensions import db
from applications.models import CompanyDepartment, CompanyUser


class DepartmentsResource(Resource):

    def get(self):
        dept_data = CompanyDepartment.query.order_by(CompanyDepartment.sort).all()
        # TODO dtree 需要返回状态信息
        res = {
            "status": {"code": 200, "message": "默认"},
            "data": [

                {
                    'deptId': item.id,
                    'parentId': item.parent_id,
                    'deptName': item.dept_name,
                    'sort': item.sort,
                    'leader': item.leader,
                    'phone': item.phone,
                    'email': item.email,
                    'status': item.status,
                    'comment': item.comment,
                    'address': item.address,
                    'create_at': item.create_at.strftime('%Y-%m-%d %H:%M:%S')
                } for item in dept_data
            ]
        }
        return jsonify(res)

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

        return success_api(message="成功")


class DepartmentResource(Resource):
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
        return dict(success=True, message='ok', dept=dept_data)

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
            return fail_api(message="更新失败")
        db.session.commit()
        return success_api(message="更新成功")

    def delete(self, dept_id):
        ret = CompanyDepartment.query.filter_by(id=dept_id).delete()
        CompanyUser.query.filter_by(dept_id=dept_id).update({"dept_id": None})
        db.session.commit()
        if ret:
            return success_api(message="删除成功")
        return fail_api(message="删除失败")


class DeptEnableResource(Resource):
    def put(self, dept_id):
        d = CompanyDepartment.query.get(dept_id)
        if d:
            d.status = not d.status
            db.session.commit()
            message = '修改成功'
            return success_api(message=message)
        return fail_api(message="出错啦")
