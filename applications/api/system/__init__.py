from flask_restful import Api

from .file import FilePhotos, FileTable
from .passport import Login


def register_system_api(api_bp):
    sys_api = Api(api_bp)

    sys_api.add_resource(FilePhotos, '/file/photos')
    sys_api.add_resource(FileTable, '/file/photo/<int:photo_id>')
    sys_api.add_resource(Login, '/passport/login')
