from flask import Blueprint, render_template, jsonify, make_response
from flask_restful import marshal, Api, Resource, reqparse

from applications.common.serialization import dept_fields
from applications.common.utils.http import success_api, fail_api
from applications.common.utils.rights import authorize
from applications.extensions import db
from applications.models import Dept, User

# from applications.view.company.department import dept_curd

dept_bp = Blueprint('dept', __name__, url_prefix='/dept')
dept_api = Api(dept_bp)


def register_dept_views(app):
    app.register_blueprint(dept_bp)


@dept_bp.get('/')
@authorize("admin:dept:main", log=True)
def main():
    return render_template('admin/department/main.html')


@dept_bp.get('/data')
@authorize("admin:dept:main", log=True)
def data():
    dept_data = Dept.query.order_by(Dept.sort).all()

    res = {
        "data": marshal(dept_data, dept_fields)
    }
    return jsonify(res)


@dept_api.resource('/add')
class AddDepartment(Resource):
    @authorize("admin:dept:add", log=True)
    def get(self):
        return make_response(render_template('admin/department/add.html'))

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


@dept_bp.get('/tree')
@authorize("admin:dept:main", log=True)
def tree():
    dept_data = Dept.query.order_by(Dept.sort).all()
    res = {
        "status": {"code": 200, "message": "默认"},
        "data": marshal(dept_data, dept_fields)

    }
    return jsonify(res)


# 启用
@dept_bp.put('/enable')
@authorize("admin:dept:edit", log=True)
def enable():
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


@dept_api.resource('/edit/<int:dept_id>')
class DeptURD(Resource):
    @authorize("admin:dept:edit", log=True)
    def get(self, dept_id):
        dept = Dept.query.filter_by(id=dept_id).first()
        return make_response(render_template('admin/department/edit.html', dept=dept))

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
