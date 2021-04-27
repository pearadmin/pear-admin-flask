from flask import Blueprint, request, render_template, jsonify
from flask_login import login_required
from flask_marshmallow import Marshmallow

from applications.models import db

ma = Marshmallow()
admin_curd = Blueprint('adminCurd', __name__, url_prefix='/admin/curd')

@admin_curd.route('/')
def index():
    colums=[]
    colums.append("table_name")
    colums.append(db.Column('id',db.Integer))
    colums.append(db.Column('id', db.Integer, primary_key=True, comment="ID"))
    colums.append(db.Column('url', db.String(255), comment=u"来源"))
    colums.append(db.Column('date', db.DateTime, comment=u"记录时间"))
    colums.append(db.Column('status', db.Integer, comment=u"是否回访"))
    re = db.Table(*colums).columns
    db.create_all()
    return str(re)
