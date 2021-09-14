import os

from flask import request, jsonify, current_app
from flask_restful import Resource, marshal
from sqlalchemy import desc

from applications.common.utils.http import fail_api, success_api, table_api
from applications.common.utils.rights import authorize
from applications.common.utils.upload import upload_one, delete_photo_by_id
from applications.extensions import db
from applications.models import FilePhoto


class FilePhotosResource(Resource):

    @authorize("admin:file:main", log=True)
    def get(self):
        page = request.args.get('page', type=int)
        limit = request.args.get('limit', type=int)
        photo_paginate = FilePhoto.query.order_by(desc(FilePhoto.create_at)
                                                  ).paginate(page=page,
                                                             per_page=limit,
                                                             error_out=False)
        data = marshal(photo_paginate.items, FilePhoto.fields())
        return table_api(result={'items': data,
                                 'total': photo_paginate.total, },
                         code=0)

    @authorize("admin:file:add", log=True)
    def post(self):
        if 'file' in request.files:
            photo = request.files['file']
            mime = request.files['file'].content_type
            file_url = upload_one(photo=photo, mime=mime)

            res = {
                "message": "上传成功",
                "code": 0,
                "success": True,
                "data":
                    {"src": file_url}
            }
            return jsonify(res)
        return fail_api()

    @authorize("admin:file:delete", log=True)
    def delete(self):
        """图片批量删除"""
        # TODO bugs 图片删除失败
        ids = request.form.getlist('ids[]')
        photo_name = FilePhoto.query.filter(FilePhoto.id.in_(ids)).all()
        upload_url = current_app.config.get("UPLOADED_PHOTOS_DEST")
        for p in photo_name:
            os.remove(upload_url + '/' + p.name)
        photo = FilePhoto.query.filter(FilePhoto.id.in_(ids)).delete(synchronize_session=False)
        db.session.commit()
        if photo:
            return success_api(message="删除成功")
        else:
            return fail_api(message="删除失败")


class FilePhotoResource(Resource):
    """图片数据"""

    @authorize("admin:file:delete", log=True)
    def delete(self, photo_id):
        res = delete_photo_by_id(photo_id)
        if res:
            return success_api(message="删除成功")
        else:
            return fail_api(message="删除失败")
