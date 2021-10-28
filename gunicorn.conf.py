import os
import multiprocessing

bind = '0.0.0.0:8000'
backlog = 512
chdir = os.path.dirname(os.path.abspath(__file__))
timeout = 30
worker_class = 'sync'

workers = multiprocessing.cpu_count() * 2 + 1
threads = 2
loglevel = 'info'
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'

if not os.path.exists('logs'):
    os.mkdir('logs')

accesslog = os.path.join(chdir, "logs/gunicorn_access.log")
errorlog = os.path.join(chdir, "logs/gunicorn_error.log")
