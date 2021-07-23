import os

from flask import request, jsonify, current_app
from flask_restful import Api, Resource, marshal
from sqlalchemy import desc

from applications.api import api_bp
from applications.common.serialization import photo_fields
from applications.common.utils.http import fail_api, success_api, table_api
from applications.common.utils.rights import authorize
from applications.common.utils.upload import upload_one, delete_photo_by_id
from applications.extensions import db
from applications.models import Photo

file_api = Api(api_bp, prefix='/file')


@file_api.resource('/upload')
class Upload(Resource):
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


@file_api.resource('/table')
class FileTable(Resource):
    """图片数据"""

    @authorize("admin:file:main", log=True)
    def get(self):
        page = request.args.get('page', type=int)
        limit = request.args.get('limit', type=int)
        photo_paginate = Photo.query.order_by(desc(Photo.create_time)).paginate(page=page, per_page=limit,
                                                                                error_out=False)
        data = marshal(photo_paginate.items, photo_fields)
        return table_api(data=data, count=photo_paginate.total, code=0)


@file_api.resource('/batch_remove')
class FileBatchRemove(Resource):
    """图片批量删除"""

    @authorize("admin:file:delete", log=True)
    def post(self):
        ids = request.form.getlist('ids[]')
        photo_name = Photo.query.filter(Photo.id.in_(ids)).all()
        upload_url = current_app.config.get("UPLOADED_PHOTOS_DEST")
        for p in photo_name:
            os.remove(upload_url + '/' + p.name)
        photo = Photo.query.filter(Photo.id.in_(ids)).delete(synchronize_session=False)
        db.session.commit()
        if photo:
            return success_api(msg="删除成功")
        else:
            return fail_api(msg="删除失败")
