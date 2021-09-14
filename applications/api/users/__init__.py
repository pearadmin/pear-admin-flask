from flask_restful import Api

from .profile import UserStatusResource, UserAvatarResource, UserInfoResource, UserPasswordResource
from .user import UserUsersResource, UserUserResource, UserRoleResource


def register_users_api(api_bp):
    users_api = Api(api_bp, prefix='/users')

    users_api.add_resource(UserInfoResource, '/user/<int:user_id>/info')
    users_api.add_resource(UserStatusResource, '/user/<int:user_id>/status')
    users_api.add_resource(UserAvatarResource, '/user/<int:user_id>/avatar')
    users_api.add_resource(UserPasswordResource, '/user/<int:user_id>/password')
    users_api.add_resource(UserUsersResource, '/users')
    users_api.add_resource(UserUserResource, '/user/<int:user_id>')
    users_api.add_resource(UserRoleResource, '/user/<int:user_id>/role')
