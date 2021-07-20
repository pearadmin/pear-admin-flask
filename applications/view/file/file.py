from flask import request, jsonify
from flask_restful import Api, Resource

from applications.common.utils.http import fail_api, success_api
from applications.common.utils.rights import authorize
from applications.view.file import file_bp
from applications.view.file._utils import upload_one, delete_photo_by_id

file_api = Api(file_bp)


@file_api.resource('/upload')
class Upload(Resource):
    # @authorize("admin:file:add", log=True)
    # def get(self):
    #     return make_response(render_template('admin/file/photo_add.html'))

    @authorize("admin:file:add", log=True)
    def post(self):
        if 'file' in request.files:
            photo = request.files['file']
            mime = request.files['file'].content_type
            file_url = upload_one(photo=photo, mime=mime)

            res = {
                "msg": "上传成功",
                "code": 0,
                "success": True,
                "data":
                    {"src": file_url}
            }
            return jsonify(res)
        return fail_api()

    @authorize("admin:file:delete", log=True)
    def delete(self):
        _id = request.form.get('id')
        res = delete_photo_by_id(_id)
        if res:
            return success_api(msg="删除成功")
        else:
            return fail_api(msg="删除失败")


