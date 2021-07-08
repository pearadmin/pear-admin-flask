cd /home/ubuntu/pear-admin-flask
source venv/bin/activate
exec gunicorn -c gunicorn.conf.py "applications:create_app('development')"
