import datetime
import json

import pymysql
from applications.config.database import HOST, USERNAME, PASSWORD, DATABASE, PORT

DB_CONFIG = {
    "host": HOST,
    "port": int(PORT),
    "user": USERNAME,
    "password": PASSWORD,
    "db": DATABASE,
    "charset": "utf8"
}


class SQLManager(object):

    # 初始化实例方法
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect()

    # 连接数据库
    def connect(self):
        self.conn = pymysql.connect(
            host=DB_CONFIG.get('host'),
            port=DB_CONFIG.get('port'),
            user=DB_CONFIG.get('user'),
            passwd=DB_CONFIG.get('password'),
            db=DB_CONFIG.get('db'),
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 查询多条数据

    def get_list(self, sql, args=None):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        return result

    # 查询多条数据后关闭
    def get_list_close(self, sql, args=None):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        self.close()
        return result

    # 查询单条数据
    def get_one(self, sql, args=None):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        return result

    # 查询单条数据后关闭
    def get_one_close(self, sql, args=None):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        self.close()
        return result

    # 执行单条SQL语句
    def moddify(self, sql, args=None):
        self.cursor.execute(sql, args)
        self.conn.commit()

    # 执行多条SQL语句
    def multi_modify(self, sql, args=None):
        self.cursor.executemany(sql, args)
        self.conn.commit()

    # 创建单条记录的语句
    def create(self, sql, args=None):
        self.cursor.execute(sql, args)
        self.conn.commit()
        last_id = self.cursor.lastrowid
        return last_id

    # 关闭数据库cursor和连接
    def close(self):
        self.cursor.close()
        self.conn.close()

    # 进入with语句自动执行
    def __enter__(self):
        return self

    # 退出with语句块自动执行
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


"""
原生查询dict的datetime解析器
用法
json.dumps(dictxxx, cls=DateEncoder)
"""


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)
