from flask import Blueprint, request, render_template, jsonify
from flask_login import login_required
from sqlalchemy import desc
from applications.models.admin_log import AdminLog, LogSchema
from applications.service.common.curd import model_to_dicts
from applications.service.common.response import table_api

admin_log = Blueprint('adminLog', __name__, url_prefix='/admin/log')


#                               ----------------------------------------------------------
#                               -------------------------  日志管理 --------------------------
#                               ----------------------------------------------------------


@admin_log.route('/')
@login_required
def index():
    return render_template('admin/admin_log/main.html')


#                               ==========================================================
#                                                            登录日志
#                               ==========================================================


@admin_log.route('/loginLog')
@login_required
def loginLog():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    log = AdminLog.query.filter_by(url='/admin/login').order_by(desc(AdminLog.create_time)).paginate(page=page,
                                                                                                     per_page=limit,
                                                                                                     error_out=False)
    count = AdminLog.query.filter_by(url='/admin/login').count()
    data = model_to_dicts(Schema=LogSchema, model=log.items)

    return table_api(data=data, count=count)


#                               ==========================================================
#                                                            操作日志
#                               ==========================================================


@admin_log.route('/operateLog')
@login_required
def operateLog():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    log = AdminLog.query.filter(AdminLog.url != '/admin/login').order_by(desc(AdminLog.create_time)).paginate(page=page,
                                                                                                              per_page=limit,
                                                                                                              error_out=False)
    count = AdminLog.query.filter(AdminLog.url != '/admin/login').count()
    data = model_to_dicts(Schema=LogSchema,model=log.items)
    return table_api(data=data,count=count)
