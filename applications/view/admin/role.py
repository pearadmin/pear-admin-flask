from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from applications.common.curd import model_to_dicts, enable_status, disable_status, get_one_by_id
from applications.common.helper import ModelFilter
from applications.common.utils.http import table_api, success_api, fail_api
from applications.common.utils.rights import authorize
from applications.common.utils.validate import xss_escape
from applications.extensions import db
from applications.models import Role, Power, User
from applications.schemas import RoleSchema, PowerSchema2

admin_role = Blueprint('adminRole', __name__, url_prefix='/admin/role')


# 用户管理
@admin_role.get('/')
@authorize("admin:role:main", log=True)
def main():
    return render_template('admin/role/main.html')


# 表格数据
@admin_role.get('/data')
@authorize("admin:role:main", log=True)
def table():
    # 获取请求参数
    role_name = xss_escape(request.args.get('roleName', type=str))
    role_code = xss_escape(request.args.get('roleCode', type=str))
    # 查询参数构造
    mf = ModelFilter()
    if role_name:
        mf.vague(field_name="name", value=role_name)
    if role_code:
        mf.vague(field_name="code", value=role_code)
    # orm查询
    # 使用分页获取data需要.items
    role = Role.query.filter(mf.get_filter(Role)).layui_paginate()
    count = role.total
    # 返回api
    return table_api(data=model_to_dicts(schema=RoleSchema, data=role.items), count=count)


# 角色增加
@admin_role.get('/add')
@authorize("admin:role:add", log=True)
def add():
    return render_template('admin/role/add.html')


# 角色增加
@admin_role.post('/save')
@authorize("admin:role:add", log=True)
def save():
    req = request.json
    details = xss_escape(req.get("details"))
    enable = xss_escape(req.get("enable"))
    roleCode = xss_escape(req.get("roleCode"))
    roleName = xss_escape(req.get("roleName"))
    sort = xss_escape(req.get("sort"))
    role = Role(
        details=details,
        enable=enable,
        code=roleCode,
        name=roleName,
        sort=sort
    )
    db.session.add(role)
    db.session.commit()
    return success_api(msg="成功")


# 角色授权
@admin_role.get('/power/<int:_id>')
@authorize("admin:role:power", log=True)
def power(_id):
    return render_template('admin/role/power.html', id=_id)


# 获取角色权限
@admin_role.get('/getRolePower/<int:id>')
@authorize("admin:role:main", log=True)
def get_role_power(id):
    role = Role.query.filter_by(id=id).first()
    check_powers = role.power
    check_powers_list = []
    for cp in check_powers:
        check_powers_list.append(cp.id)
    powers = Power.query.all()
    power_schema = PowerSchema2(many=True)  # 用已继承ma.ModelSchema类的自定制类生成序列化类
    output = power_schema.dump(powers)  # 生成可序列化对象
    for i in output:
        if int(i.get("powerId")) in check_powers_list:
            i["checkArr"] = "1"
        else:
            i["checkArr"] = "0"
    res = {
        "data": output,
        "status": {"code": 200, "message": "默认"}
    }
    return jsonify(res)


# 保存角色权限
@admin_role.put('/saveRolePower')
@authorize("admin:role:edit", log=True)
def save_role_power():
    req_form = request.form
    power_ids = req_form.get("powerIds")
    power_list = power_ids.split(',')
    role_id = req_form.get("roleId")
    role = Role.query.filter_by(id=role_id).first()
    
    powers = Power.query.filter(Power.id.in_(power_list)).all()
    role.power = powers
    
    db.session.commit()
    return success_api(msg="授权成功")


# 角色编辑
@admin_role.get('/edit/<int:id>')
@authorize("admin:role:edit", log=True)
def edit(id):
    r = get_one_by_id(model=Role, id=id)
    return render_template('admin/role/edit.html', role=r)


# 更新角色
@admin_role.put('/update')
@authorize("admin:role:edit", log=True)
def update():
    req_json = request.json
    id = req_json.get("roleId")
    data = {
        "code": xss_escape(req_json.get("roleCode")),
        "name": xss_escape(req_json.get("roleName")),
        "sort": xss_escape(req_json.get("sort")),
        "enable": xss_escape(req_json.get("enable")),
        "details": xss_escape(req_json.get("details"))
    }
    role = Role.query.filter_by(id=id).update(data)
    db.session.commit()
    if not role:
        return fail_api(msg="更新角色失败")
    return success_api(msg="更新角色成功")


# 启用用户
@admin_role.put('/enable')
@authorize("admin:role:edit", log=True)
def enable():
    id = request.json.get('roleId')
    if id:
        res = enable_status(Role, id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="启动成功")
    return fail_api(msg="数据错误")


# 禁用用户
@admin_role.put('/disable')
@authorize("admin:role:edit", log=True)
def dis_enable():
    _id = request.json.get('roleId')
    if _id:
        res = disable_status(Role, _id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="禁用成功")
    return fail_api(msg="数据错误")


# 角色删除
@admin_role.delete('/remove/<int:id>')
@authorize("admin:role:remove", log=True)
def remove(id):
    role = Role.query.filter_by(id=id).first()
    # 删除该角色的权限和用户
    role.power = []
    role.user = []
    
    r = Role.query.filter_by(id=id).delete()
    db.session.commit()
    if not r:
        return fail_api(msg="角色删除失败")
    return success_api(msg="角色删除成功")


# 批量删除
@admin_role.delete('/batchRemove')
@authorize("admin:role:remove", log=True)
@login_required
def batch_remove():
    ids = request.form.getlist('ids[]')
    for id in ids:
        role = Role.query.filter_by(id=id).first()
        # 删除该角色的权限和用户
        role.power = []
        role.user = []
        
        r = Role.query.filter_by(id=id).delete()
        db.session.commit()
    return success_api(msg="批量删除成功")
