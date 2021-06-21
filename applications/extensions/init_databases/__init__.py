from flask import Flask


def add_data(fields, data_list, obj):
    from applications.extensions import db
    for _data in data_list:
        dept = obj()
        for key, value in dict(zip(fields, _data)).items():
            setattr(dept, key, value)
        db.session.add(dept)
    db.session.commit()


def create_dept_data():
    """创建化部门数据"""
    from applications.models import Dept
    _data_list = [
        (1, 0, '总公司', 1, '就眠仪式', '12312345679', '123qq.com', 1, None, '这是总公司', None, '2021-06-01 17:23:20'),
        (4, 1, '济南分公司', 2, '就眠仪式', '12312345678', '1234qq.com', 1, None, '这是济南', '2021-06-01 17:24:33',
         '2021-06-01 17:25:19'),
        (5, 1, '唐山分公司', 4, 'mkg', '12312345678', '123@qq.com', 1, None, '这是唐山', '2021-06-01 17:25:15',
         '2021-06-01 17:25:20'),
        (7, 4, '济南分公司开发部', 5, '就眠仪式', '12312345678', '123@qq.com', 1, None, '测试', '2021-06-01 17:27:39',
         '2021-06-01 17:27:39'),
        (8, 5, '唐山测试部', 6, 'mkg', '12312345678', '123@qq.com', 1, None, '测试部', '2021-06-01 17:28:27',
         '2021-06-01 17:28:27'),
    ]
    _fields = ['id', 'parent_id', 'dept_name', 'sort', 'leader', 'phone', 'email', 'status', 'remark', 'address',
               'create_at', 'update_at']
    add_data(_fields, _data_list, Dept)


def create_admin_dict_data():
    from applications.models import DictData, DictType

    _fields = ['id', 'data_label', 'data_value', 'type_code', 'is_default', 'enable', 'remark', 'create_time',
               'update_time', ]
    _data_list = [
        (8, '男', 'boy', 'user_sex', None, 1, '男 : body', '2021-04-16 13:36:34', '2021-04-16 14:05:06'),
        (9, '女', 'girl', 'user_sex', None, 1, '女 : girl', '2021-04-16 13:36:55', '2021-04-16 13:36:55'),
    ]

    add_data(_fields, _data_list, DictData)
    _fields = ['id', 'type_name', 'type_code', 'description', 'enable', 'create_time', 'update_time', ]
    _data_list = [
        (1, '用户性别', 'user_sex', '用户性别', 1, None, '2021-04-16 13:37:11')
    ]
    add_data(_fields, _data_list, DictType)


def create_admin_photo():
    from applications.models import Photo

    _fields = [
        'id',
        'name',
        'href',
        'mime',
        'size',
        'create_time',
    ]
    _data_list = [
        (3, '6958819_pear-admin_1607443454_1.png',
         'http://127.0.0.1:5000/_uploads/photos/6958819_pear-admin_1607443454_1.png', 'image/png', '2204',
         '2021-03-19 18:53:02'),
        (17, '1617291580000.jpg', 'http://127.0.0.1:5000/_uploads/photos/1617291580000.jpg', 'image/png', '94211',
         '2021-04-01 23:39:41'),
    ]
    add_data(_fields, _data_list, Photo)


def create_admin_power():
    from applications.models import Power

    _data_list = \
        [
            (1, '系统管理', '0', '', None, None, '0', 'layui-icon layui-icon-set-fill', 1, None, None, 1),
            (3, '用户管理', '1', 'admin:user:main', '/admin/user/', '_iframe', '1',
             'layui-icon layui-icon layui-icon layui-icon layui-icon-rate', 1, None, None, 1),
            (4, '权限管理', '1', 'admin:power:main', '/rights/', '_iframe', '1', None, 2, None, None, 1),
            (9, '角色管理', '1', 'admin:role:main', '/admin/role', '_iframe', '1', 'layui-icon layui-icon-username', 2,
             '2021-03-16 22:24:58', '2021-03-25 19:15:24', 1),
            (
                12, '系统监控', '1', 'admin:monitor:main', '/admin/monitor', '_iframe', '1',
                'layui-icon layui-icon-vercode', 5,
                '2021-03-18 22:05:19', '2021-03-25 19:15:27', 1),
            (13, '日志管理', '1', 'admin:log:main', '/admin/log', '_iframe', '1', 'layui-icon layui-icon-read', 4,
             '2021-03-18 22:37:10', '2021-06-03 11:06:25', 1),
            (17, '文件管理', '0', '', '', '', '0', 'layui-icon layui-icon-camera', 2, '2021-03-19 18:56:23',
             '2021-03-25 19:15:08', 1),
            (18, '图片上传', '1', 'admin:file:main', '/admin/file', '_iframe', '17', 'layui-icon layui-icon-camera', 5,
             '2021-03-19 18:57:19', '2021-03-25 19:15:13', 1),
            (21, '权限增加', '2', 'admin:power:add', '', '', '4', 'layui-icon layui-icon-add-circle', 1,
             '2021-03-22 19:43:52',
             '2021-03-25 19:15:22', 1),
            (22, '用户增加', '2', 'admin:user:add', '', '', '3', 'layui-icon layui-icon-add-circle', 1,
             '2021-03-22 19:45:40',
             '2021-03-25 19:15:17', 1),
            (23, '用户编辑', '2', 'admin:user:edit', '', '', '3', 'layui-icon layui-icon-rate', 2, '2021-03-22 19:46:15',
             '2021-03-25 19:15:18', 1),
            (24, '用户删除', '2', 'admin:user:remove', '', '', '3', 'layui-icon None', 3, '2021-03-22 19:46:51',
             '2021-03-25 19:15:18', 1),
            (25, '权限编辑', '2', 'admin:power:edit', '', '', '4', 'layui-icon layui-icon-edit', 2, '2021-03-22 19:47:36',
             '2021-03-25 19:15:22', 1),
            (26, '用户删除', '2', 'admin:power:remove', '', '', '4', 'layui-icon layui-icon-delete', 3,
             '2021-03-22 19:48:17',
             '2021-03-25 19:15:23', 1),
            (27, '用户增加', '2', 'admin:role:add', '', '', '9', 'layui-icon layui-icon-add-circle', 1,
             '2021-03-22 19:49:09',
             '2021-03-25 19:15:24', 1),
            (28, '角色编辑', '2', 'admin:role:edit', '', '', '9', 'layui-icon layui-icon-edit', 2, '2021-03-22 19:49:41',
             '2021-03-25 19:15:25', 1),
            (
                29, '角色删除', '2', 'admin:role:remove', '', '', '9', 'layui-icon layui-icon-delete', 3,
                '2021-03-22 19:50:15',
                '2021-03-25 19:15:26', 1),
            (30, '角色授权', '2', 'admin:role:power', '', '', '9', 'layui-icon layui-icon-component', 4,
             '2021-03-22 19:50:54',
             '2021-03-25 19:15:26', 1),
            (31, '图片增加', '2', 'admin:file:add', '', '', '18', 'layui-icon layui-icon-add-circle', 1,
             '2021-03-22 19:58:05',
             '2021-03-25 19:15:28', 1),
            (32, '图片删除', '2', 'admin:file:delete', '', '', '18', 'layui-icon layui-icon-delete', 2,
             '2021-03-22 19:58:45',
             '2021-03-25 19:15:29', 1),
            (44, '数据字典', '1', 'admin:dict:main', '/admin/dict', '_iframe', '1', 'layui-icon layui-icon-console', 6,
             '2021-04-16 13:59:49', '2021-04-16 13:59:49', 1),
            (45, '字典增加', '2', 'admin:dict:add', '', '', '44', 'layui-icon ', 1,
             '2021-04-16 14:00:59', '2021-04-16 14:00:59', 1),
            (46, '字典修改', '2', 'admin:dict:edit', '', '', '44', 'layui-icon ', 2, '2021-04-16 14:01:33',
             '2021-04-16 14:01:33', 1),
            (47, '字典删除', '2', 'admin:dict:remove', '', '', '44', 'layui-icon ', 3, '2021-04-16 14:02:06',
             '2021-04-16 14:02:06', 1),
            (48, '部门管理', '1', 'admin:dept:main', '/dept', '_iframe', '1', 'layui-icon layui-icon-group', 3,
             '2021-06-01 16:22:11', '2021-06-01 16:22:11', 1),
            (49, '部门增加', '2', 'admin:dept:add', '', '', '48', 'layui-icon None', 1, '2021-06-01 17:35:52',
             '2021-06-01 17:36:15', 1),
            (50, '部门编辑', '2', 'admin:dept:edit', '', '', '48', 'layui-icon ', 2, '2021-06-01 17:36:41',
             '2021-06-01 17:36:41', 1),
            (51, '部门删除', '2', 'admin:dept:remove', '', '', '48', 'layui-icon None', 3, '2021-06-01 17:37:15',
             '2021-06-01 17:37:26', 1),
        ]
    _fields = [
        'id',
        'name',
        'type',
        'code',
        'url',
        'open_type',
        'parent_id',
        'icon',
        'sort',
        'create_time',
        'update_time',
        'enable',
    ]

    add_data(_fields, _data_list, Power)


def create_admin_role():
    from applications.models import Role

    _fields = [
        'id',
        'name',
        'code',
        'remark',
        'details',
        'sort',
        'create_time',
        'update_time',
        'enable',
    ]
    _data_list = [
        (1, '管理员', 'admin', None, '管理员', 1, None, None, 1),
        (2, '普通用户', 'common', None, '只有查看，没有增删改权限', 2, '2021-03-22 20:02:38', '2021-04-01 22:29:56', 1),
    ]

    add_data(_fields, _data_list, Role)


def create_admin_role_power():
    from applications.models import user_role
    from applications.extensions import db

    _data_list = [
        (237, 1, 1),
        (238, 3, 1),
        (239, 4, 1),
        (240, 9, 1),
        (241, 12, 1),
        (242, 13, 1),
        (243, 17, 1),
        (244, 18, 1),
        (245, 21, 1),
        (246, 22, 1),
        (247, 23, 1),
        (248, 24, 1),
        (249, 25, 1),
        (250, 26, 1),
        (251, 27, 1),
        (252, 28, 1),
        (253, 29, 1),
        (254, 30, 1),
        (255, 31, 1),
        (256, 32, 1),
        (257, 44, 1),
        (258, 45, 1),
        (259, 46, 1),
        (260, 47, 1),
        (261, 48, 1),
        (262, 49, 1),
        (263, 50, 1),
        (264, 51, 1),
        (265, 1, 2),
        (266, 3, 2),
        (267, 4, 2),
        (268, 9, 2),
        (269, 12, 2),
        (270, 13, 2),
        (271, 17, 2),
        (272, 18, 2),
        (273, 44, 2),
        (274, 48, 2),
    ]

    # add_data(_fields, _data_list, UserRole)
    for data in _data_list:
        db.session.execute('insert into rt_role_power VALUES (%s, %s, %s);' % data)
    db.session.commit()


def create_admin_user():
    from applications.models import User

    _fields = [
        'id',
        'username',
        'password_hash',
        'create_at',
        'update_at',
        'enable',
        'realname',
        'remark',
        'avatar',
        'dept_id',
    ]
    _data_list = [
        (1, 'admin', 'pbkdf2:sha256:150000$raM7mDSr$58fe069c3eac01531fc8af85e6fc200655dd2588090530084d182e6ec9d52c85',
         None, '2021-06-01 17:28:55', 1, '超级管理', '要是不能把握时机，就要终身蹭蹬，一事无成！',
         'http://127.0.0.1:5000/_uploads/photos/1617291580000.jpg', 1),
        (7, 'test', 'pbkdf2:sha256:150000$cRS8bYNh$adb57e64d929863cf159f924f74d0634f1fecc46dba749f1bfaca03da6d2e3ac',
         '2021-03-22 20:03:42', '2021-06-01 17:29:47', 1, '超级管理', '要是不能把握时机，就要终身蹭蹬，一事无成',
         '/static/admin/admin/images/avatar.jpg', 1),
        (8, 'wind', 'pbkdf2:sha256:150000$skME1obT$6a2c20cd29f89d7d2f21d9e373a7e3445f70ebce3ef1c3a555e42a7d17170b37',
         '2021-06-01 17:30:39', '2021-06-01 17:30:52', 1, '风', None, '/static/admin/admin/images/avatar.jpg', 7),
    ]

    add_data(_fields, _data_list, User)


def create_admin_user_role() -> object:
    from applications.extensions import db

    _data_list = [
        (21, 1, 1),
        (22, 7, 2),
        (24, 8, 2),
    ]

    # add_data(_fields, _data_list, UserRole)
    for data in _data_list:
        db.session.execute('insert into rt_user_role VALUES (%s, %s, %s);' % data)
    db.session.commit()


def create_example():
    from applications.models import DictData

    _fields = []
    _data_list = []

    add_data(_fields, _data_list, DictData)


def register_script(app: Flask):
    @app.cli.command()
    def init_db():
        """数据库初始化"""
        create_dept_data()
        create_admin_dict_data()
        create_admin_photo()
        create_admin_power()
        create_admin_role()
        create_admin_role_power()
        create_admin_user()
        create_admin_user_role()

    @app.cli.command()
    def turn():
        from applications.extensions import db
        db.drop_all()
        db.create_all()
