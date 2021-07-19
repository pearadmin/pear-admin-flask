from flask import Flask
from flask_uploads import configure_uploads
from flask_uploads import UploadSet, IMAGES

photos = UploadSet('photos', IMAGES)


def init_upload(app: Flask):
    configure_uploads(app, photos)
