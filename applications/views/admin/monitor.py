import os
import platform
import re
from datetime import datetime
import psutil
from flask import Blueprint, request, render_template
from flask_login import login_required
from flask_marshmallow import Marshmallow
from applications.service.admin_log import admin_log

ma = Marshmallow()
admin_Monitor = Blueprint('adminMonitor', __name__, url_prefix='/admin/monitor')


# @admin_Monitor.before_request
# @login_required
# def Monitor_log():
#     admin_log(request)


#                               ----------------------------------------------------------
#                               -------------------------  系统监控 --------------------------
#                               ----------------------------------------------------------


@admin_Monitor.route('/')
@login_required
def index():
    # 主机名称
    hostname = platform.node()
    # 系统版本
    system_version = platform.platform()
    # python版本
    python_version = platform.python_version()
    # 逻辑cpu数量
    cpu_count = psutil.cpu_count()
    # cup使用率
    cpus_percent = psutil.cpu_percent(interval=0.1)
    # 内存
    memory_information = psutil.virtual_memory()
    # 内存使用率
    memory_usage = memory_information.percent
    memory_used = str(round(memory_information.used / 1024 / 1024))
    memory_total = str(round(memory_information.total / 1024 / 1024))
    memory_free = str(round(memory_information.free / 1024 / 1024))
    # 磁盘信息

    disk_partitions_list = []
    # 判断是否在容器中
    if not os.path.exists('/.dockerenv'):
        disk_partitions = psutil.disk_partitions()
        for i in disk_partitions:
            a = psutil.disk_usage(i.device)
            disk_partitions_dict = {
                'device': i.device,
                'fstype': i.fstype,
                'total': str(round(a.total / 1024 / 1024)),
                'used': str(round(a.used / 1024 / 1024)),
                'free': str(round(a.free / 1024 / 1024)),
                'percent': a.percent
            }
            disk_partitions_list.append(disk_partitions_dict)

    # 开机时间
    boot_time = datetime.fromtimestamp(psutil.boot_time()).replace(microsecond=0)
    up_time = datetime.now().replace(microsecond=0) - boot_time
    up_time_list = re.split(r':', str(up_time))
    up_time_format = " {} 小时{} 分钟{} 秒".format(up_time_list[0], up_time_list[1], up_time_list[2])

    return render_template('admin/monitor.html',
                           hostname=hostname,
                           system_version=system_version,
                           python_version=python_version,
                           cpus_percent=cpus_percent,
                           memory_usage=memory_usage,
                           cpu_count=cpu_count,
                           memory_used=memory_used,
                           memory_total=memory_total,
                           memory_free=memory_free,
                           boot_time=boot_time,
                           up_time_format=up_time_format,
                           disk_partitions_list=disk_partitions_list

                           )
