from flask_restful import Api

from .profile import UserStatus, UserAvatar, UserInfo, UserPassword
from .user import UserUsers, UserUser, UserRole


def register_users_api(api_bp):
    users_api = Api(api_bp, prefix='/users')

    users_api.add_resource(UserInfo, '/user/<int:user_id>/info')
    users_api.add_resource(UserStatus, '/user/<int:user_id>/status')
    users_api.add_resource(UserAvatar, '/user/<int:user_id>/avatar')
    users_api.add_resource(UserPassword, '/user/<int:user_id>/password')
    users_api.add_resource(UserUsers, '/users')
    users_api.add_resource(UserUser, '/user/<int:user_id>')
    users_api.add_resource(UserRole, '/user/<int:user_id>/role')
