<div align="center">
<br/>
<br/>
<img src="https://gitee.com/pear-admin/Pear-Admin-Layui/raw/master/admin/images/logo.png" width="90px" style="margin-top:30px;"/>
  <h1 align="center">
    Pear Admin Flask
  </h1>
  <h4 align="center">
    开 箱 即 用 的 Flask 快 速 开 发 平 台
  </h4> 

  [预 览](http://flask.pearadmin.com)   |   [官 网](http://www.pearadmin.com/)   |   [群聊](https://jq.qq.com/?_wv=1027&k=5OdSmve)   |   [社区](http://forum.pearadmin.com/)


<p align="center">
    <a href="#">
        <img src="https://img.shields.io/badge/pear%20admin%20flask-1.0.0-green" alt="Pear Admin Layui Version">
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/Python-3.6+-green.svg" alt="Python Version">
    </a>
      <a href="#">
        <img src="https://img.shields.io/badge/Mysql-5.3.2+-green.svg" alt="Mysql Version">
    </a>
</p>
</div>

<div align="center">
  <img  width="92%" style="border-radius:10px;margin-top:20px;margin-bottom:20px;box-shadow: 2px 0 6px gray;" src="https://images.gitee.com/uploads/images/2020/1019/104805_042b888c_4835367.png" />
</div>

## 项目简介
Pear Admin Flask 基于 Flask 生态的后台管理系统，该项目旨在为 python 开发者提供一个快速开发前后端半分离的后台管理系统的模板

在使用本项目之前最好掌握以下知识点

+ [html、css、JavaScript](https://developer.mozilla.org/zh-CN/docs/Learn/HTML)
+ [jQuery](https://www.w3school.com.cn/jquery/index.asp)
+ [layui](https://www.layui.com/)
+ [flask](https://dormousehole.readthedocs.io/en/latest/)
+ [flask-login](https://flask-login.readthedocs.io/en/latest/)
+ [flask-sqlalchemy](http://www.pythondoc.com/flask-sqlalchemy/quickstart.html)
+ [flask-restful](https://flask-restful.readthedocs.io/en/latest/)


## 预览
Pear Admin Flask 有以下几个版本：					

[master分支版本 ](https://gitee.com/pear-admin/pear-admin-flask/tree/master/)  

>flask 2.x	+	flask-sqlalchemy	+	权限验证	+	Flask-APScheduler	定时任务	+	marshmallow 序列化与数据验证

[Mini 分支版本 ](https://gitee.com/pear-admin/pear-admin-flask/tree/mini/)

>flask 2.x	+	flask-sqlalchemy    +	权限验证	+	Flask-restful	 序列化与数据验证

|  |  |
|---------------------|---------------------|
| ![](docs/assets/1.jpg)  | ![](docs/assets/2.jpg)  |
| ![](docs/assets/3.jpg)|  ![](docs/assets/4.jpg)   |
| ![](docs/assets/5.jpg) |  ![](docs/assets/6.jpg)   |

##  内置功能

- [x] 用户管理：用户是系统操作者，该功能主要完成系统用户配置。
- [x] 权限管理：配置系统菜单，操作权限，按钮权限标识等。
- [x] 角色管理：角色菜单权限分配。
- [x] 操作日志：系统正常操作日志记录和查询；系统异常信息日志记录和查询。
- [x] 登录日志：系统登录日志记录查询包含登录异常。
- [x] 文件上传: 图片上传示例


## 文档
正在编写


## 安装使用

+ 下载源码
```bash
git clone https://gitee.com/pear-admin/pear-admin-flask

# 切换分支
git checkout mini
```

+ 安装依赖
```bash
# 创建虚拟环境
python -m venv venv

# 然后使虚拟环境生效（windows，Linux自行解决）
venv\Scripts\activate 

# 安装依赖
pip install -r requirement\requirement-dev.txt
```

+ 数据迁移

默认的使用 `sqlite3` 作为测试环境的数据库进行演示,不需要按照mysql即可查看演示。如果需要二次开发，建议改成 `mysql` 。

如果需要在开发环境使用 mysql 作为数据库，请查看 `applications/configs/config.py` 文件里面的相关配置文件, 注释掉 sqlite 的配置即可

如果需要修改数据的配置信息，请在 `.flaskenv` 里面调整即可 

```bash
flask db init
flask db migrate -m '数据初始化'
flask db upgrade

flask init-db
```