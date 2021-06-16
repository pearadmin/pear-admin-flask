from flask import Flask
from flask_mail import Mail

mail = Mail()


def init_mail(app: Flask):
    mail.init_app(app)
