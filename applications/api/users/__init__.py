from flask_restful import Api

from applications.api import api_bp

users_api = Api(api_bp, prefix='/users')

from . import user, profile
