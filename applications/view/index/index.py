from flask import render_template, Blueprint

index_bp = Blueprint('Index', __name__, url_prefix='/')


@index_bp.route('/')
def index():
    return render_template('index/index.html')
