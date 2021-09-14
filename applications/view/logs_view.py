from flask import Blueprint, request, render_template
from sqlalchemy import desc
from flask_restful import marshal

from applications.common.utils.http import table_api
from applications.common.utils.rights import authorize, permission_required
from applications.models import LoggingModel

logs_bp = Blueprint('logs', __name__, url_prefix='/logs')


@logs_bp.get('/')
@permission_required("admin:log:main")
def index():
    return render_template('admin/logs_temp/main.html')


@logs_bp.get('/login_log')
@permission_required("admin:log:main")
def login_log():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    log_paginate = LoggingModel.query.filter_by(
        url='/api/v1/passport/login').order_by(
        desc(LoggingModel.create_at)).paginate(
        page=page, per_page=limit, error_out=False)
    data = marshal(log_paginate.items, LoggingModel.fields())

    return table_api(result={'items': data,
                             'total': log_paginate.total, },
                     code=0)


@logs_bp.get('/access_log')
@permission_required("admin:log:main")
def operate_log():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    log_paginate = LoggingModel.query.filter(
        LoggingModel.url != '/api/v1/passport/login').order_by(
        desc(LoggingModel.create_at)).paginate(
        page=page, per_page=limit, error_out=False)
    data = marshal(log_paginate.items, LoggingModel.fields())
    return table_api(result={'items': data,
                             'total': log_paginate.total, },
                     code=0)
