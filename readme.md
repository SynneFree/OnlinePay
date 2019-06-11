# GitHub Readme

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
- [ ]  设立云数据库 - 曾
- [ ]  设置Flask数据库连接 - 曾
- [ ]  初始化Flask环境 - 曾
- [ ]  模块化开发
    - [ ]  周
        - [ ]  product-detail.html
            - [ ]  客户端
            - [ ]  游客端
        - [ ]  verification.html
            - [ ]  管理员端
    - [ ]  赵
        - [ ]  index.html
    - [ ]  王
        - [ ]  商家端
            - [ ]  listofgoods.html
            - [ ]  add.html
            - [ ]  edit.html
            - [ ]  response.html
    - [ ]  廖
        - [ ]  待定?
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

浏览到 flask\Scripts\目录下 （MacOS 是 flask\bin目录下）

    pip install flask
    pip install flask-login
    pip install flask-openid
    pip install flask-mail
    pip install flask-sqlalchemy
    pip install sqlalchemy-migrate
    pip install flask-whooshalchemy
    pip install flask-wtf
    pip install flask-babel
    pip install guess_language
    pip install flipflop
    pip install coverage