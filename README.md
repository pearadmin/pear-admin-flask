<div align="center">
<br/>
<br/>
<img src="https://gitee.com/pear-admin/Pear-Admin-Layui/raw/master/admin/images/logo.png" width="90px" style="margin-top:30px;"/>
  <h1 align="center">
    Pear Admin Flask
  </h1>


  [预 览](http://flask.pearadmin.com)   |   [官 网](http://www.pearadmin.com/)   |   [群聊](https://jq.qq.com/?_wv=1027&k=5OdSmve)   |   [社区](http://forum.pearadmin.com/)



<p align="center">
    <a href="#">
        <img src="https://img.shields.io/badge/pear%20admin%20flask-0.1-green" alt="Pear Admin Layui Version">
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/JQuery-2.0+-green.svg" alt="Jquery Version">
    </a>
      <a href="#">
        <img src="https://img.shields.io/badge/Layui-2.5.6+-green.svg" alt="Layui Version">
    </a>
</p>
</div>
<div align="center">
  <img  width="92%" style="border-radius:10px;margin-top:20px;margin-bottom:20px;box-shadow: 2px 0 6px gray;" src="https://images.gitee.com/uploads/images/2020/1019/104805_042b888c_4835367.png" />
</div>

#### 项目简介
>Pear Admin Flask 基于 Flask  的后台管理系统，拥抱应用广泛的python语言，通过使用本系统，即可快速构建你的功能业务
>
>项目旨在为python开发者提供一个后台管理系统的模板，成为您构建信息管理系统，物联网后台....等等应用时灵活，简单的工具
>
>众人拾柴火焰高，欢迎pythoner参与项目~

Pear Admin Flask 有以下几个版本：					

[master分支版本 ](https://gitee.com/pear-admin/pear-admin-flask/tree/master/)  

>	flask 2.1	+	flask-sqlalchemy	+	mysql	+	权限验证	+	Flask-APScheduler	定时任务	+	marshmallow 序列化与数据验证

[Mini 分支版本 ](https://gitee.com/pear-admin/pear-admin-flask/tree/mini/)

>flask 2.1	+	flask-sqlalchemy	+	sqllite	+	权限验证	+	Flask-RESTful	 序列化与数据验证

[v1 分支版本(不再更新，仅供参考) ](https://gitee.com/pear-admin/pear-admin-flask/tree/v1/)

>flask 1.12	+	flask-sqlalchemy	+ mysql		+	权限验证	+	marshmallow 序列化与数据验证

[simple 分支版本(不再更新，仅供参考) ](https://gitee.com/pear-admin/pear-admin-flask/tree/simple/)

>flask 1.12	+	flask-sqlalchemy	+ mysql	+	极简权限	+	marshmallow 序列化与数据验证
>
>项目最简版本

#### 环境要求

* python >= 3.6
* mysql>=5.7

#### 安装配置

```bash
#下载项目
git clone https://gitee.com/pear-admin/pear-admin-flask
#安装依赖
pip install -r requirement.txt
#修改数据库连接配置文件
applications\config\database.py
```

```python
#修改数据库连接配置文件applications\config\database.py
#修改成你自己的
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'PearAdminFlask'
USERNAME = 'root'
PASSWORD = 'root'
```

>推荐使用虚拟环境 venv
>
>```bash
>python -m venv venv
>```
>

```bash
#进入开发目录
cd dev
#执行初始化数据库脚本
python initDb.py

#如果报模块路径错误
python dev/initDb.py
```

然后，你可以使用 flask run 命令启动项目了



