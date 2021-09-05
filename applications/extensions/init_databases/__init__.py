from flask import Flask
import re
from datetime import datetime

date_str = re.compile('\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d$')


def add_data(data_list, obj):
    from applications.extensions import db

    for _data in data_list:
        dept = obj()
        for key, value in _data.items():

            if isinstance(value, str) and date_str.match(value):
                value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

            setattr(dept, key, value)
        db.session.add(dept)
    db.session.commit()


def register_script(app: Flask):
    @app.cli.command()
    def init_db():
        """数据库初始化"""

        # 创建化部门数据
        from applications.models import CompanyDepartment
        from applications.configs.init_data import cp_dept_data_list
        add_data(cp_dept_data_list, CompanyDepartment)

        # 图片数据
        from applications.models import FilePhoto
        from applications.configs.init_data import file_photo_data_list

        add_data(file_photo_data_list, FilePhoto)

        # 初始化权限表数据
        from applications.models import RightsPower
        from applications.configs.init_data import rt_power_data_list

        add_data(rt_power_data_list, RightsPower)
        # 初始化角色表
        from applications.models import RightsRole
        from applications.configs.init_data import rt_role_data_list

        # 角色权限关系表
        from applications.extensions import db
        from applications.configs.init_data import rt_role_power_data_list
        for data in rt_role_power_data_list:
            db.session.execute('insert into rt_role_power VALUES (%s, %s, %s);' % tuple(data))
        db.session.commit()

        add_data(rt_role_data_list, RightsRole)

        # 管理员用户
        from applications.models import CompanyUser
        from applications.configs.init_data import cp_user_data_list

        add_data(cp_user_data_list, CompanyUser)

        # 用户角色表
        from applications.extensions import db
        from applications.configs.init_data import rt_user_role_data_list

        for data in rt_user_role_data_list:
            db.session.execute('insert into rt_user_role VALUES (%s, %s, %s);' % tuple(data))
        db.session.commit()

    @app.cli.command()
    def turn():
        """清空数据库"""
        from applications.extensions import db
        db.drop_all()
        db.create_all()
