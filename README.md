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
>Pear Admin Flask 基于 Flask 1.12 的后台管理系统模板，得益于Python 的生态广泛应用，通过使用本系统，即可快速构建你的功能业务，努力成为最顺手的工具。
>
>目前Flask后台管理系统几乎处于空白状态，本项目希望获得各位Python爱好者的改正与指点

#### 版本说明

Pear Admin Flask 分为 Common / Simple 两个版本：					

[** Common 通用版本 **](https://gitee.com/pear-admin/pear-admin-flask/tree/master/)  

[** Simple 简单版本 **](https://gitee.com/pear-admin/pear-admin-flask/tree/simple/)

#### 项目安装

```bash

# 下 载
git clone https://gitee.com/pear-admin/pear-admin-flask

# 安 装
pip install -r requirement.txt

# 配 置
applications\config\database.py

```

#### 修改配置

```python

# 主 机
HOST = '127.0.0.1'

# 端 口
PORT = '3306'

# 数 据 库
DATABASE = 'PearAdminFlask'

# 账 户
USERNAME = 'root'

# 密 码
PASSWORD = 'root'

```

#### Venv 安装

```bash

python -m venv venv

```

```bash

# 进 入 目 录
cd dev

# 初 始 化 数 据 库 脚 本
python initDb.py

# 如 果 报 模 块 路 径 错 误
python dev/initDb.py

```

执行 flask run 命令启动项目


#### 预览项目

|  |  |
|---------------------|---------------------|
| ![](readme/1.jpg)  | ![](readme/2.jpg)  |
| ![](readme/3.jpg)|  ![](readme/4.jpg)   |