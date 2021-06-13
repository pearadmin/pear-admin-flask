from flask import Blueprint

index_bp = Blueprint('Index', __name__, url_prefix='/')

from . import index


def init_index_views(app):
    """
    初始化蓝图

    """

    app.register_blueprint(index_bp)
