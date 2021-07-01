from flask import Blueprint, request, render_template
from sqlalchemy import desc
from flask_restful import marshal
from applications.common.serialization import log_fields

from applications.common.utils.http import table_api
from applications.common.utils.rights import authorize
from applications.models import AdminLog

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
    data = marshal(log_paginate.items, log_fields)

    return table_api(data=data, count=log_paginate.total)


@admin_log.get('/access_log')
@authorize("admin:log:main")
def operate_log():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    log_paginate = AdminLog.query.filter(
        AdminLog.url != '/passport/login').order_by(
        desc(AdminLog.create_time)).paginate(
        page=page, per_page=limit, error_out=False)
    data = marshal(log_paginate.items, log_fields)
    return table_api(data=data, count=log_paginate.total)
