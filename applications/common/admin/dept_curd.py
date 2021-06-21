from applications.extensions import db
from applications.models import Dept, DeptSchema
from applications.models import User
from applications.common.curd import model_to_dicts
from flask import escape


def get_dept_dict():
    dept = Dept.query.order_by(Dept.sort).all()
    res = model_to_dicts(Schema=DeptSchema, model=dept)
    return res


def save_dept(req):
    address = escape(req.get("address"))
    deptName = escape(req.get("deptName"))
    email = escape(req.get("email"))
    leader = escape(req.get("leader"))
    parentId = escape(req.get("parentId"))
    phone = escape(req.get("phone"))
    sort = escape(req.get("sort"))
    status = escape(req.get("status"))
    dept = Dept(
        parent_id=parentId,
        dept_name=deptName,
        sort=sort,
        leader=leader,
        phone=phone,
        email=email,
        status=status,
        address=address
    )
    r = db.session.add(dept)
    db.session.commit()
    return r


def get_dept_by_id(_id):
    """根据 id 获取部门"""
    d = Dept.query.filter_by(id=_id).first()
    return d


def enable_status(_id):
    """ 启用权限 """
    enable = 1
    d = Dept.query.filter_by(id=_id).update({"status": enable})
    if d:
        db.session.commit()
        return True
    return False


def disable_status(_id):
    """ 停用权限 """
    enable = 0
    d = Dept.query.filter_by(id=_id).update({"status": enable})
    if d:
        db.session.commit()
        return True
    return False


def update_dept(json):
    """ 更新部门信息 """
    _id = json.get("deptId"),
    data = {
        "dept_name": escape(json.get("deptName")),
        "sort": escape(json.get("sort")),
        "leader": escape(json.get("leader")),
        "phone": escape(json.get("phone")),
        "email": escape(json.get("email")),
        "status": escape(json.get("status")),
        "address": escape(json.get("address"))
    }
    d = Dept.query.filter_by(id=_id).update(data)
    if not d:
        return False
    db.session.commit()
    return True


def remove_dept(_id):
    d = Dept.query.filter_by(id=_id).delete()
    if not d:
        return False
    User.query.filter_by(dept_id=_id).update({"dept_id": None})
    db.session.commit()
    return True
