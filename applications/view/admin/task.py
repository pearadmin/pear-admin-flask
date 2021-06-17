from flask import Blueprint, request, jsonify
from applications.common.tasks.tasks import task4
from applications.extensions.init_apscheduler import scheduler
from flask_apscheduler.utils import job_to_dict

admin_task = Blueprint('adminTask', __name__, url_prefix='/admin/task')


# 暂停任务
# scheduler.pause_job('third')
# 恢复任务
# time.sleep(10)
# scheduler.resume_job('third')
# 删除任务
# scheduler.remove_job('first')

@admin_task.route('/pause', methods=['GET'])
def pause_job():  # 暂停
    job_id = request.args.get('id')
    scheduler.pause_job(str(job_id))
    return "pause success!"


@admin_task.route('/resume', methods=['GET'])
def resume_job():  # 恢复
    job_id = request.args.get('id')
    scheduler.resume_job(str(job_id))
    return "Success!"


@admin_task.route('/get_jobs', methods=['GET'])
def get_task():  # 获取
    jobs = scheduler.get_jobs()
    jobs_list = []
    for job in jobs:
        jobs_list.append(job_to_dict(job))
    return jsonify(jobs_list)


@admin_task.route('/remove_job', methods=['GET'])
def remove_job():  # 移除
    job_id = request.args.get('id')
    scheduler.remove_job(str(job_id))
    return 'remove success'


@admin_task.route('/add_job', methods=['GET'])
def add_task():
    scheduler.add_job(func=task4, id='4', args=(1, 1), trigger='interval', seconds=3,
                      replace_existing=True)
    return '6'

    #     scheduler.add_job(func=task1, id='2', args=(1, 1), trigger='cron', day_of_week='0-6', hour=18, minute=24,
    #                       second=10, replace_existing=True)

    #     scheduler.add_job(func=task4, id='4', args=(2, 2), trigger='interval', seconds=3,
    #                       replace_existing=True, misfire_grace_time=3)

    #     # trigger='interval' 表示是一个循环任务，每隔多久执行一次
    #     scheduler.add_job(func=task2, id='3', args=(2, 2), trigger='interval', seconds=3,
    #                       replace_existing=True)
