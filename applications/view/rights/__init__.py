from flask import Blueprint, Flask

rights_bp = Blueprint('rights', __name__, url_prefix='/rights')

from . import routes


def register_rights_view(app: Flask):
    app.register_blueprint(rights_bp)
