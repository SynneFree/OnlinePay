# Online Payment System
![](/structure.png)
其中checkout.html 页面已取消改成弹窗显示预定状态。

# 任务表

- [x]  数据库设计、写SQL代码 - 王
- [x]  画html文件结构图 - 曾
- [x]  分配任务 - 曾
- [x]  UI设计 - 廖
    - [x]  各网页跳转修复
    - [x]  游客端
        - [x]  product-detail.html
        - [x]  index.html
    - [x]  客户端
        - [x]  product-detail.html
        - [x]  index.html
        - [x]  comment.html
    - [x]  商家端
        - [x]  add.html
        - [x]  edit.html
        - [x]  listofgoods.html
        - [x]  response.html
    - [x]  管理员端
        - [x]  verification.html
        - [x]  comment_review.html
- [x]  翻译网页
    - [x]  英转繁 - 廖
    - [x]  繁转简 - 曾
- [x]  设立GitHub Repo -曾
- [ ]  设置Flask数据库连接 - 曾
- [ ]  初始化Flask环境 - 曾
- [ ]  模块化开发
    - [x]  周
        - [x]  product-detail.html
            - [ ]  客户端
            - [ ]  游客端
        - [x]  verification.html
            - [ ]  管理员端
    - [ ]  赵
        - [ ]  index.html
    - [ ]  王
        - [ ]  商家端
            - [ ]  listofgoods.html
            - [ ]  add.html
            - [ ]  edit.html
            - [ ]  response.html
       - [ ] 客户端
       	  - [ ]  搜索.html 
    - [ ]  廖
        - [ ]  预定下单
    - [ ]  曾
        - [ ]  comment_review.html
- [ ]  测试报告
    - [ ]  下周再定

---

# 参考教程

## Flask :

[http://www.pythondoc.com/flask-mega-tutorial](http://www.pythondoc.com/flask-mega-tutorial)

## GitHub Fork & Clone:

> 从master那里复制一份代码，然后修改代码，最后和master 合并起来

[https://www.cnblogs.com/dky20155212/p/6821634.html?utm_source=itdadao&utm_medium=referral](https://www.cnblogs.com/dky20155212/p/6821634.html?utm_source=itdadao&utm_medium=referral)

## GitHub Fork 保持同步更新的方法：

> 如果master那里更新了，但是我fork的是旧版本，我怎么确保我的Fork repository 和master 同步更新

[https://blog.csdn.net/csm201314/article/details/83045605](https://blog.csdn.net/csm201314/article/details/83045605)

---

# 开发环境

- 安装好Git
- 安装好Flask
- 安装好Virtualenv

---

# 初始化环境  - 重要

（以下内容均取自 Flask 教程，URL 在上面的**参考教程**里附上。）

在开始之前， 你需要提前安装好virtualenv ,方法如下：

    pip install virtualenv

在git clone 这个repository 到你的计算机后，通过终端浏览到此文件夹，然后创建一个虚拟环境virtual env，输入代码 (Windows 版本)

    virtualenv flask

上面的命令行在 flask 文件夹中创建一个完整的 Python 环境。  
（如果出现问题，可以尝试把OnlinePay里的 flask文件夹删掉再重试）

然后通过以下命令安装Flask扩展：(Windows版本)

浏览到 flask.Scripts/目录下 （MacOS 是 flask/bin目录下）  
用 ```pip install xxx``` 来安装插件  
下列为需要安装的插件

```
alembic==0.9.6
Babel==2.5.1
blinker==1.4
certifi==2017.7.27.1
chardet==3.0.4
click==6.7
dominate==2.3.1
elasticsearch==6.1.1
Flask==1.0.2
Flask-Babel==0.11.2
Flask-Bootstrap==3.3.7.1
Flask-HTTPAuth==3.2.3
Flask-Login==0.4.0
Flask-Mail==0.9.1
Flask-Migrate==2.1.1
Flask-Moment==0.5.2
Flask-MySQL==1.4.0
Flask-Script==2.0.6
Flask-SQLAlchemy==2.3.2
Flask-WTF==0.14.2
guess-language-spirit==0.5.3
idna==2.6
itsdangerous==0.24
Jinja2==2.10
Mako==1.0.7
MarkupSafe==1.0
mysql==0.0.2
mysqlclient==1.4.2.post1
PyJWT==1.5.3
PyMySQL==0.9.3
python-dateutil==2.6.1
python-dotenv==0.7.1
python-editor==1.0.3
pytz==2017.2
redis==2.10.6
requests==2.18.4
rq==0.9.2
six==1.11.0
SQLAlchemy==1.1.14
urllib3==1.22
visitor==0.1.3
Werkzeug==0.14.1
WTForms==2.1

```
    
#运行Flask 服务器访问网站
打开终端，在目录下 ，运行

```
./run.py
```

然后浏览器访问 127.0.0.1:5000/

