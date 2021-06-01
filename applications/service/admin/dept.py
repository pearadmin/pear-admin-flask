from markupsafe import escape, Markup

from applications.models import db
from applications.models.admin_dept import Dept, DeptSchema
from applications.models.admin_user import User
from applications.service.common.curd import model_to_dicts


def get_dept_dict():
    dept = Dept.query.order_by(Dept.sort).all()
    res = model_to_dicts(Schema=DeptSchema, model=dept)
    return res


def save_dept(req):
    address = req.get("address")
    deptName = req.get("deptName")
    email = req.get("email")
    leader = req.get("leader")
    parentId = req.get("parentId")
    parentName = req.get("parentName")
    phone = req.get("phone")
    selectParent_select_input = req.get("selectParent_select_input")
    sort = req.get("sort")
    status = req.get("status")
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
    print('0')
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
    print(str(Markup(json.get("leader"))))
    data = {
        "dept_name": json.get("deptName"),
        "sort": json.get("sort"),
        "leader": json.get("leader"),
        "phone": json.get("phone"),
        "email": json.get("email"),
        "status": json.get("status"),
        "address": json.get("address")
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
