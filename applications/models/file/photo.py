from flask_restful import fields

from applications.extensions import db

from ..base import BaseModel


class FilePhoto(db.Model, BaseModel):
    __tablename__ = 'file_photo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    href = db.Column(db.String(255))
    mime = db.Column(db.CHAR(50), nullable=False)
    size = db.Column(db.CHAR(30), nullable=False)

    @staticmethod
    def fields():
        return {
            'id': fields.Integer,
            'name': fields.String,
            'href': fields.String,
            'mime': fields.String,
            'size': fields.String,
            'ext': fields.String,
            'create_at': fields.DateTime,
        }
