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

>flask 2.x	+	flask-sqlalchemy   +	Flask-restful  +	基于角色的权限管理

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

# 然后使虚拟环境生效（windows）
venv\Scripts\activate 
# source venv/bin/activate  # （Linux激活虚拟环境）

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


## 服务器部署
### wsgi
默认的 flask 程序启动一个应用，一个应用只能用于测试环境下。生成环境采用 gunicorn 开启多进行+多线程启动程序，可以提升程序的并发量。详细配置可以查看 gunicorn 的官方文档，本项目的配置文件请查看 `gunicorn.conf.py` 。

```python
# filename: gunicorn.conf.py
import os
import multiprocessing

bind = '0.0.0.0:8000'  # 默认部署地址，如果用了nginx的反向代理，建议改成 127.0.0.1:8000
backlog = 512
chdir = os.path.dirname(os.path.abspath(__file__))
timeout = 30
worker_class = 'sync'

workers = multiprocessing.cpu_count() * 2 + 1  # 开启进程数为 CPU核心数 * 2 + 1
threads = 2  # 每个进程开启两个线程
loglevel = 'info'  # 日志的等级
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
# 日志存放位置
if not os.path.exists('logs'):
    os.mkdir('logs')

accesslog = os.path.join(chdir, "logs/gunicorn_access.log")
errorlog = os.path.join(chdir, "logs/gunicorn_error.log")

```

因为是在服务器部署，而且一般做服务器部署的时候都会采用虚拟环境 + 命令行启动。为了能在命令行模式下从虚拟环境启动程序，所以需要专门编写一个 shell 文件进行启动。详细看看 `start.sh`

```shell
cd /home/ubuntu/pear-admin-flask  # 进入到项目的根目录
source venv/bin/activate  # 激活虚拟环境
exec gunicorn -c gunicorn.conf.py "applications:create_app('development')"  # 运行 gunicorn 指令启动程序
```

注意：如果使用的是全局环境，就可以不用激活虚拟环境。



### 守护进程

程序在服务器环境下，一般是 7*24 小时不间断运行。有时候服务器会因为一些特殊原因宕机自动重启，或者是晚上定时重启电脑让内存处于最佳状态下。在这种情况下如果想要只要是电脑在正常运行，程序就提供服务，就需要开启守护进程。



使用下面的命令安装Supervisor：
```shell script
$ sudo apt install supervisor
```

编辑配置文件

```shell
$ sudo vim /etc/supervisor/conf.d/pear.conf
```

写入项目配置
```shell script
[program:pear]
command=bash /home/ubuntu/pear-admin-flask/start.sh
user=root
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
```

管理项目进程
```shell script
$ sudo supervisorctl
```



注意：关于 supervisor 的具体功法参考 [官方文档](http://supervisord.org/index.html) 



### Nginx

gunicorn 虽然提供了 Web服务器的功能，但是功能比较局限，拓展性也不强。而 Nginx 就能很好的弥补这部分的不足。所以在服务器一般采用 Nginx + gunicorn 的模式做项目部署。

Nginx 是一个高性能的 HTTP 和 反向代理 web服务器。在后期的项目性能优化中，可以提供非常多的帮助。例如可以对返回的网页、静态文件进行压缩提升页面的加载速度，当性能达到瓶颈之后可以通过负载均衡让后端直接可以通过加机器解决问题。



使用下面的命令安装Nginx

```shell
$ sudo apt install nginx
```

可以直接在 Nginx 的默认配置文件（/etc/nginx/nginx.conf）中写入程序配置，但通常情况下，为了便于组织，我们可以在/etc/nginx/sites-enabled/或是/etc/nginx/conf.d/目录下为我们的Flask程序创建单独的Nginx配置文件。

```shell
$ sudo rm /etc/nginx/sites-enabled/default  # 删除默认的示例
$ sudo vi /etc/nginx/sites-enabled/pear  # 添加自己的示例
```



> /etc/nginx/sites-enabled/pear

```shell
server {
    listen 80 default_server;  # 监听 80 端口
    # server_name example.com;  # 域名解析
    access_log  /var/log/nginx/access.log;
    error_log  /var/log/nginx/error.log;

	location / {
            proxy_pass http://127.0.0.1:8000;  # 转发的地址，即Gunicorn运行的地址
            proxy_redirect     off;

            proxy_set_header   Host                 $host;
            proxy_set_header   X-Real-IP            $remote_addr;
            proxy_set_header   X-Forwarded-For      $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Proto    $scheme;
    }
}
```

更新配置文件后，我们可以通过下面的命令来测试语法正确性：

```shell
$ sudo nginx -t
```

如果一切正常，那么现在可以重启Nginx让配置生效：

```shell
$ sudo service nginx restart
```

当使用反向代理服务器后，Gunicorn不需要再监听外部请求，而是直接监听本地机的某个端口。我们可以使用默认值，即本地机的8000端口，默认绑定 `127.0.0.1:8000` 。

