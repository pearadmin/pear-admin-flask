from flask import Blueprint

admin_curd = Blueprint('adminCurd', __name__, url_prefix='/admin/curd')


@admin_curd.route('/')
def index():
    return "功能开发中"
