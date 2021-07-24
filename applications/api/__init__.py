from flask import Blueprint, Flask

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

from . import department
from . import file
from . import roles
from . import rights
from . import passport
from . import users


def init_api(app: Flask):
    app.register_blueprint(api_bp)
