from applications.models import db
from applications.models.admin_dept import Dept, DeptSchema
from applications.models.admin_user import User
from applications.service.common.curd import model_to_dicts
from applications.service.common.validate import xss_escape


def get_dept_dict():
    dept = Dept.query.order_by(Dept.sort).all()
    res = model_to_dicts(Schema=DeptSchema, model=dept)
    return res


def save_dept(req):

    address = xss_escape(req.get("address"))
    deptName = xss_escape(req.get("deptName"))
    email = xss_escape(req.get("email"))
    leader = xss_escape(req.get("leader"))
    parentId = xss_escape(req.get("parentId"))
    phone = xss_escape(req.get("phone"))
    sort = xss_escape(req.get("sort"))
    status = xss_escape(req.get("status"))
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


def get_dept_by_id(id):
    d = Dept.query.filter_by(id=id).first()
    return d


# 启动权限
def enable_status(id):
    enable = 1
    d = Dept.query.filter_by(id=id).update({"status": enable})
    if d:
        db.session.commit()
        return True
    return False


# 停用权限
def disable_status(id):
    enable = 0
    d = Dept.query.filter_by(id=id).update({"status": enable})
    if d:
        db.session.commit()
        return True
    return False


def update_dept(json):
    id = json.get("deptId"),
    data = {
        "dept_name": xss_escape(json.get("deptName")),
        "sort": xss_escape(json.get("sort")),
        "leader": xss_escape(json.get("leader")),
        "phone": xss_escape(json.get("phone")),
        "email": xss_escape(json.get("email")),
        "status": xss_escape(json.get("status")),
        "address": xss_escape(json.get("address"))
    }
    d = Dept.query.filter_by(id=id).update(data)
    if not d:
        return False
    db.session.commit()
    return True


def remove_dept(id):
    d = Dept.query.filter_by(id=id).delete()
    if not d:
        return False
    User.query.filter_by(dept_id=id).update({"dept_id": None})
    db.session.commit()
    return True
