from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def init_databases(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
