import os

from flask import Blueprint, request, render_template, jsonify, current_app
from flask_marshmallow import Marshmallow
from marshmallow import fields
from sqlalchemy import desc

from applications.models import db
from applications.models.admin import Photo
from applications.service.upload import photos

ma = Marshmallow()
admin_Monitor = Blueprint('adminMonitor', __name__, url_prefix='/admin/monitor')

@admin_Monitor.route('/')
def index():
    return render_template('admin/monitor.html')

