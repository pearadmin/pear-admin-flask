from flask import Blueprint, render_template
from flask_restful import Api

from ...common.utils.rights import authorize

rights_bp = Blueprint('rights', __name__, url_prefix='/rights')
rights_api = Api(rights_bp)


@rights_bp.get('/')
@authorize("admin:power:main", log=True)
def index():
    return render_template('rights/main.html')


from . import routes
from . import right
