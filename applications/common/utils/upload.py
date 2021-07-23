import os

from flask import current_app

from applications.common.flask_uploads import UploadSet, IMAGES
from applications.extensions import db
from applications.models import Photo

photos = UploadSet('photos', IMAGES)


def upload_one(photo, mime):
    filename = photos.save(photo)
    file_url = photos.url(filename)

    upload_url = current_app.config.get("UPLOADED_PHOTOS_DEST")
    size = os.path.getsize(upload_url + '/' + filename)
    photo = Photo(name=filename, href=file_url, mime=mime, size=size)
    db.session.add(photo)
    db.session.commit()
    return file_url


def delete_photo_by_id(_id):
    photo_name = Photo.query.filter_by(id=_id).first().name
    photo = Photo.query.filter_by(id=_id).delete()
    db.session.commit()
    upload_url = current_app.config.get("UPLOADED_PHOTOS_DEST")
    os.remove(upload_url + '/' + photo_name)
    return photo
