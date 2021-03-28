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
>各位Python爱好者多多指教

Pear Admin Flask 分为 Common / Simple 两个版本：					

[** Common 通用版本 **](https://gitee.com/pear-admin/pear-admin-flask/tree/master/)  

[** Simple 简洁版本 **](https://gitee.com/pear-admin/pear-admin-flask/tree/simple/)

####  内置功能

- [x] 用户管理：用户是系统操作者，该功能主要完成系统用户配置。
- [x] 权限管理：配置系统菜单，操作权限，按钮权限标识等。
- [x] 角色管理：角色菜单权限分配。
- [x] 操作日志：系统正常操作日志记录和查询；系统异常信息日志记录和查询。
- [x] 登录日志：系统登录日志记录查询包含登录异常。
- [x] 服务监控：监视当前系统CPU、内存、磁盘、python版本,运行时长等相关信息。
- [x] 文件上传:   图片上传示例
- [ ] 代码生成:   构想中....

####  项目结构

```
Pear Admin Flask
│
├─applications
│  │
│  ├─config
│  │  │  
│  │  ├─ common.py #普通配置
│  │  │  
│  │  └─ database.py #数据库配置
│  │
│  ├─models
│  │  │  
│  │  └─admin.py #基本模型
│  │
│  ├─service
│  │  │  
│  │  ├─admin
│  │  │  │
│  │  │  ├─ file.py #file视图的数据操作
│  │  │  │		 		   	
│  │  │  ├─ index.py #index视图的数据操作
│  │  │  │				
│  │  │  ├─ power.py #power视图的数据操作
│  │  │  │				
│  │  │  ├─ role.py #role视图的数据操作
│  │  │  │					
│  │  │  └─ user.py #user视图的数据操作
│  │  │  					
│  │  ├─ admin_log.py #存储日志
│  │  │  
│  │  ├─ deBug.py #deBug工具栏初始化
│  │  │  
│  │  ├─ login.py #flask_login初始化					
│  │  │  
│  │  ├─ CaptchaTool.py	#验证码
│  │  │  
│  │  ├─ OriginalDb.py #原生sql查询封装
│  │  │  
│  │  ├─ route_auth.py #权限
│  │  │  
│  │  └─ upload.py #上传
│  │
│  └─views
│     │
│     ├─admin #前台视图
│     │	 │     					
│     │  ├─index.py #主视图
│     │  │     
│     │  ├─user.py #用户视图
│     │  │     
│     │  ├─role.py #角色视图
│     │  │     
│     │  ├─power.py #权限视图
│     │  │     
│     │  ├─monitor.py #系统监控
│     │  │     
│     │  ├─file.py #文件上传
│     │  │     
│     │  ├─admin_log.py #系统日志
│     │  │     
│     │  ├─context_processor.py	#全局模板函数注册
│     │  │     
│     │  ├─error.py #错误处理
│     │  │     
│     │  └─init.py #蓝图注册
│     │
│     └─index #前台视图
│ 
├─dev #数据库初始化
│
├─migrations	
│					
├─readmes
│
├─static #静态资源
│  │
│  └─upload #文件上传地址
│
└─templates
    │
    ├─admin #前台模板
    │
    ├─errors #错误模板
    │ 
    └─index #前台模板
```



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

#### 运行项目

```bash
# 进 入 目 录
cd dev

# 初 始 化 数 据 库
python initDb.py

# 如 果 报 模 块 路 径 错 误
python dev/initDb.py

```

执行 flask run 命令启动项目


#### 预览项目

|  |  |
|---------------------|---------------------|
| ![](readmes/1.jpg)  | ![](readmes/2.jpg)  |
| ![](readmes/3.jpg)|  ![](readmes/4.jpg)   |
| ![](readmes/5.jpg) |  ![](readmes/6.jpg)   |