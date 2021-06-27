from flask import Blueprint, Flask
from flask_restful import Api

rights_bp = Blueprint('rights', __name__, url_prefix='/rights')
rights_api = Api(rights_bp)

from . import routes
from . import right


def register_rights_view(app: Flask):
    app.register_blueprint(rights_bp)
