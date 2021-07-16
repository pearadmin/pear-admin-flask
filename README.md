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

#### 项目简介
>Pear Admin Flask 基于 Flask  的后台管理系统，拥抱应用广泛的python语言，通过使用本系统，即可快速构建你的功能业务
>
>项目旨在为python开发者提供一个后台管理系统的模板，成为您构建信息管理系统，物联网后台....等等应用时灵活，简单的工具
>
>众人拾柴火焰高，欢迎pythoner参与项目~

Pear Admin Flask 有以下几个版本：					

[master分支版本 ](https://gitee.com/pear-admin/pear-admin-flask/tree/master/)  

>	flask 2.0.1	+	flask-sqlalchemy	+	mysql	+	权限验证	+	Flask-APScheduler	定时任务	+	marshmallow 序列化与数据验证

[Mini 分支版本 ](https://gitee.com/pear-admin/pear-admin-flask/tree/mini/)

>flask 2.0.1	+	flask-sqlalchemy	+	sqllite	+	权限验证	+	Flask-RESTful	 序列化与数据验证

[v1 分支版本(不再更新，仅供参考) ](https://gitee.com/pear-admin/pear-admin-flask/tree/v1/)

>flask 1.12	+	flask-sqlalchemy	+ mysql		+	权限验证	+	marshmallow 序列化与数据验证

[simple 分支版本(不再更新，仅供参考) ](https://gitee.com/pear-admin/pear-admin-flask/tree/simple/)

>flask 1.12	+	flask-sqlalchemy	+ mysql	+	极简权限	+	marshmallow 序列化与数据验证
>
>项目最简版本

####  内置功能

- [x] 用户管理：用户是系统操作者，该功能主要完成系统用户配置。
- [x] 权限管理：配置系统菜单，操作权限，按钮权限标识等。
- [x] 角色管理：角色菜单权限分配。
- [x] 操作日志：系统正常操作日志记录和查询；系统异常信息日志记录和查询。
- [x] 登录日志：系统登录日志记录查询包含登录异常。
- [x] 服务监控：监视当前系统CPU、内存、磁盘、python版本,运行时长等相关信息。
- [x] 文件上传:   图片上传示例
- [x] 定时任务:   简单的定时任务
- [ ] 代码生成:   构想中....

####  项目结构

```
Pear Admin Flask
├─applications  # 应用
│  ├─configs  # 配置文件
│  │  ├─ common.py  # 普通配置
│  │  └─ config.py  # 配置文件对象
│  ├─extensions  # 注册插件
│  ├─models  # 数据模型
│  ├─static  # 静态资源文件
│  ├─templates  # 静态模板文件
│  └─views  # 视图部分
│     ├─admin  # 后台管理视图模块
│     └─index  # 前台视图模块
├─docs  # 文档说明（占坑）
├─migrations  # 迁移文件记录
├─requirement  # 依赖文件
├─test # 测试文件夹（占坑）
└─.env # 项目的配置文件

```



#### 项目安装

```bash
# 下 载
git clone https://gitee.com/pear-admin/pear-admin-flask

# 安 装
pip install -r requirement\requirement-dev.txt

# 配 置
.env

```

#### 修改配置

```python
.env
# MySql配置信息
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
MYSQL_DATABASE=PearAdminFlask
MYSQL_USERNAME=root
MYSQL_PASSWORD=root

# Redis 配置
REDIS_HOST=127.0.0.1
REDIS_PORT=6379

# 密钥配置
SECRET_KEY='pear-admin-flask'

# 邮箱配置
MAIL_SERVER='smtp.qq.com'
MAIL_USERNAME='123@qq.com'
MAIL_PASSWORD='XXXXX' # 生成的授权码
```

#### Venv 安装

```bash
python -m venv venv
```

#### 运行项目

```bash
# 初 始 化 数 据 库

flask init
```

执行 flask run 命令启动项目

#### 命令行创建视图

```bash
# 示例

flask new --type view --name test/a

# 自动注册蓝图
# 访问http://127.0.0.1:5000/test/a/
```

#### 预览项目

|  |  |
|---------------------|---------------------|
| ![](docs/assets/1.jpg)  | ![](docs/assets/2.jpg)  |
| ![](docs/assets/3.jpg)|  ![](docs/assets/4.jpg)   |
| ![](docs/assets/5.jpg) |  ![](docs/assets/6.jpg)   |