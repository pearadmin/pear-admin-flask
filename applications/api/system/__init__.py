from flask_restful import Api

from .file import FilePhotosResource, FilePhotoResource
from .passport import LoginResource


def register_system_api(api_bp):
    sys_api = Api(api_bp)

    sys_api.add_resource(FilePhotosResource, '/file/photos')
    sys_api.add_resource(FilePhotoResource, '/file/photo/<int:photo_id>')
    sys_api.add_resource(LoginResource, '/passport/login')
