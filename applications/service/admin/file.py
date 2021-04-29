import os
from flask import current_app
from sqlalchemy import desc
from applications.models import db
from applications.models.admin_photo import Photo, PhotoSchema
from applications.service.common.curd import model_to_dicts
from applications.service.upload import photos


def get_photo(page, limit):
    photo = Photo.query.order_by(desc(Photo.create_time)).paginate(page=page, per_page=limit, error_out=False)
    count = Photo.query.count()
    data = model_to_dicts(Schema=PhotoSchema,model=photo.items)
    return data, count


def upload_one(photo, mime):
    filename = photos.save(photo)
    file_url = photos.url(filename)

    upload_url = current_app.config.get("UPLOADED_PHOTOS_DEST")
    size = os.path.getsize(upload_url + '/' + filename)
    photo = Photo(name=filename, href=file_url, mime=mime, size=size)
    db.session.add(photo)
    db.session.commit()
    return file_url


def delete_photo_by_id(id):
    photo_name = Photo.query.filter_by(id=id).first().name
    photo = Photo.query.filter_by(id=id).delete()
    db.session.commit()
    upload_url = current_app.config.get("UPLOADED_PHOTOS_DEST")
    os.remove(upload_url + '/' + photo_name)
    return photo
