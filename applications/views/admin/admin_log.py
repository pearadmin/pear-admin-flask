from flask import Blueprint, request, render_template, jsonify
from flask_login import login_required
from flask_marshmallow import Marshmallow
from marshmallow import fields
from sqlalchemy import desc
from applications.models.admin import AdminLog

ma = Marshmallow()
admin_log = Blueprint('adminLog', __name__, url_prefix='/admin/log')


#                               ----------------------------------------------------------
#                               -------------------------  日志管理 --------------------------
#                               ----------------------------------------------------------


@admin_log.route('/')
@login_required
def index():
    return render_template('admin/admin_log/main.html')


class LogSchema(ma.Schema):  # 序列化类
    id = fields.Integer()
    method = fields.Str()
    uid = fields.Str()
    url = fields.Str()
    desc = fields.Str()
    ip = fields.Str()
    user_agent = fields.Str()
    create_time = fields.DateTime()


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
    role_schema = LogSchema(many=True)
    output = role_schema.dump(log.items)
    res = {
        'msg': "",
        'code': 0,
        'data': output,
        'count': count,
        'limit': "10"

    }

    return jsonify(res)


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
    role_schema = LogSchema(many=True)
    output = role_schema.dump(log.items)
    res = {
        'msg': "",
        'code': 0,
        'data': output,
        'count': count,
        'limit': "10"

    }

    return jsonify(res)
