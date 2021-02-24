from flask import Blueprint, request, render_template, jsonify, current_app
from flask_marshmallow import Marshmallow

ma = Marshmallow()
admin_Monitor = Blueprint('adminMonitor', __name__, url_prefix='/admin/monitor')


@admin_Monitor.route('/')
def index():
    return render_template('admin/monitor.html')
