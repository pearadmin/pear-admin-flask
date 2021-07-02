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
Pear Admin Flask 基于 Flask 生态的后台管理系统，该项目旨在为 python 开发者提供一个快速开发前后端半分离的后台管理系统的模板

在使用本项目之前最好掌握以下知识点

+ html、css、JavaScript
+ jQuery
+ layui
+ flask
+ flask-login
+ flask-sqlalchemy
+ flask-restful


Pear Admin Flask 分为 Common / Simple 两个版本：

[Common 通用版本](https://gitee.com/pear-admin/pear-admin-flask/tree/master/)  
[Simple 简洁版本](https://gitee.com/pear-admin/pear-admin-flask/tree/simple/)

####  内置功能

- [x] 用户管理：用户是系统操作者，该功能主要完成系统用户配置。
- [x] 权限管理：配置系统菜单，操作权限，按钮权限标识等。
- [x] 角色管理：角色菜单权限分配。
- [x] 操作日志：系统正常操作日志记录和查询；系统异常信息日志记录和查询。
- [x] 登录日志：系统登录日志记录查询包含登录异常。
- [x] 文件上传: 图片上传示例

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

#### 项目启动

##### 1. 下载源码
```bash
git clone https://gitee.com/pear-admin/pear-admin-flask

# 切换分支
git checkout mini
```

##### 2. 安装依赖
```bash
# 创建虚拟环境
python -m venv venv

# 然后使虚拟环境生效（windows，Linux自行解决）
venv\Scripts\activate 

# 安装依赖
pip install -r requirement\requirement-dev.txt
```

##### 3. 数据迁移
默认的使用 `sqlite3` 作为开发环境的数据库进行演示，如果需要二次开发，建议改成 `mysql` 。
```bash
flask db init
flask db migrate -m '数据初始化'
flask db upgrade

flask init-db
```


##### 4. 其他事项

如果需要在开发环境使用 mysql 作为数据库，请查看 `applications/configs/config.py` 文件里面的相关配置文件

如果需要修改数据的配置信息，请在 `.flaskenv` 里面调整即可 

#### 预览项目

|  |  |
|---------------------|---------------------|
| ![](docs/assets/1.jpg)  | ![](docs/assets/2.jpg)  |
| ![](docs/assets/3.jpg)|  ![](docs/assets/4.jpg)   |
| ![](docs/assets/5.jpg) |  ![](docs/assets/6.jpg)   |