from flask import Blueprint,render_template

index_index = Blueprint('Index', __name__, url_prefix='/')
from flask_marshmallow import Marshmallow

ma = Marshmallow()


@index_index.route('/')
def index():
    return render_template('index/index.html')
