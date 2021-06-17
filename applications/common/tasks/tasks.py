import datetime
from flask import current_app

from applications.extensions import db
from applications.extensions.init_apscheduler import scheduler
from applications.models import Dept


# @scheduler.task(
#     "interval",
#     id="job_sync",
#     seconds=10,
#     max_instances=1,
#     start_date="2000-01-01 12:19:00",
# )
# def task1():
#     # oh, do you need something from config?
#     with scheduler.app.app_context():
#         print(scheduler.app.config)  # noqa: T001
#         address = "ces"
#         deptName = "测试"
#         email = "123@qq.com"
#         leader = "测试的"
#         parentId = "1"
#         phone = "123456"
#         sort = "5"
#         status = 1
#         dept = Dept(
#             parent_id=parentId,
#             dept_name=deptName,
#             sort=sort,
#             leader=leader,
#             phone=phone,
#             email=email,
#             status=status,
#             address=address
#         )
#         r = db.session.add(dept)
#         db.session.commit()


def task2(a, b):
    print(f'定时任务_1_{a},{b},{datetime.datetime.now()}')


def task3(a, b):
    print(f'定时任务_2_{a}{b}{datetime.datetime.now()}')


def task4(a, b):
    print(f'定时任务_4_{a}{b}{datetime.datetime.now()}')
