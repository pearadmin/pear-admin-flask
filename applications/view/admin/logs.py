from flask import Blueprint, request, render_template
from sqlalchemy import desc

from applications.common.utils.http import table_api
from applications.common.utils.rights import authorize
from applications.models import AdminLog, LogSchema
from applications.common.curd import model_to_dicts

admin_log = Blueprint('logs', __name__, url_prefix='/logs')


@admin_log.get('/')
@authorize("admin:log:main")
def index():
    return render_template('admin/admin_log/main.html')


@admin_log.get('/login_log')
@authorize("admin:log:main")
def login_log():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    log_paginate = AdminLog.query.filter_by(
        url='/passport/login').order_by(
        desc(AdminLog.create_time)).paginate(
        page=page, per_page=limit, error_out=False)
    data = model_to_dicts(Schema=LogSchema, model=log_paginate.items)

    return table_api(data=data, count=log_paginate.total)


@admin_log.get('/access_log')
@authorize("admin:log:main")
def operate_log():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    log = AdminLog.query.filter(
        AdminLog.url != '/passport/login').order_by(
        desc(AdminLog.create_time)).paginate(
        page=page, per_page=limit, error_out=False)
    count = AdminLog.query.filter(AdminLog.url != '/admin/login').count()
    data = model_to_dicts(Schema=LogSchema, model=log.items)
    return table_api(data=data, count=count)
