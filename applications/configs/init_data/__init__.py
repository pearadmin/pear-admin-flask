import json
import os

path = os.path.dirname(os.path.abspath(__file__))
cp_dept_data_list = json.loads(open(os.path.join(path, 'cp_dept.json'), encoding='utf-8').read())
cp_user_data_list = json.loads(open(os.path.join(path, 'cp_user.json'), encoding='utf-8').read())
file_photo_data_list = json.loads(open(os.path.join(path, 'file_photo.json'), encoding='utf-8').read())
rt_power_data_list = json.loads(open(os.path.join(path, 'rt_power.json'), encoding='utf-8').read())
rt_role_data_list = json.loads(open(os.path.join(path, 'rt_role.json'), encoding='utf-8').read())
rt_role_power_data_list = json.loads(open(os.path.join(path, 'rt_role_power.json'), encoding='utf-8').read())
rt_user_role_data_list = json.loads(open(os.path.join(path, 'rt_user_role.json'), encoding='utf-8').read())
