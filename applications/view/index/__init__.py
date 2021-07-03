from flask import Blueprint

index_bp = Blueprint('index', __name__, url_prefix='/')

from . import index


def register_index_views(app):
    """
    初始化蓝图

    """

    app.register_blueprint(index_bp)
