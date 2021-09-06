from flask import Blueprint, Flask

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

from .rights import register_rights_api
from .system import register_system_api
from .users import register_users_api

register_rights_api(api_bp)
register_users_api(api_bp)
register_system_api(api_bp)


def init_api(app: Flask):
    app.register_blueprint(api_bp)
