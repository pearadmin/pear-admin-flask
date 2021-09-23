from flask import Blueprint, request, render_template
from sqlalchemy import desc
from applications.common.utils.http import table_api
from applications.common.utils.rights import authorize
from applications.models import AdminLog
from applications.schemas import LogSchema
from applications.common.curd import model_to_dicts

admin_log = Blueprint('adminLog', __name__, url_prefix='/admin/log')


# 日志管理
@admin_log.get('/')
@authorize("admin:log:main")
def index():
    return render_template('admin/admin_log/main.html')


# 登录日志
@admin_log.get('/loginLog')
@authorize("admin:log:main")
def login_log():
    # orm查询
    # 使用分页获取data需要.items
    log = AdminLog.query.filter_by(url='/passport/login').order_by(desc(AdminLog.create_time)).layui_paginate()
    count = log.total
    return table_api(data= model_to_dicts(schema=LogSchema, data=log.items), count=count)


# 操作日志
@admin_log.get('/operateLog')
@authorize("admin:log:main")
def operate_log():
    # orm查询
    # 使用分页获取data需要.items
    log = AdminLog.query.filter(
        AdminLog.url != '/passport/login').order_by(
        desc(AdminLog.create_time)).layui_paginate()
    count = log.total
    return table_api(data=model_to_dicts(schema=LogSchema, data=log.items), count=count)
