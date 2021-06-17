from flask import Flask
from flask_apscheduler import APScheduler

scheduler = APScheduler()


def init_scheduler(app: Flask):
    scheduler.init_app(app)
    with app.app_context():
        from applications.common.tasks import tasks
        scheduler.start()
        from applications.common.tasks import events
