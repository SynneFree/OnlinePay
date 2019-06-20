from app import app
from flask import render_template, request, url_for, redirect, session
from .models import *
# from .models import buyer_valid_login, seller_valid_login, administrator_valid_login
# from .models import buyer_register, seller_register, manager_register,user_info_query
# from .models import username_valid_register
import pymysql
# from .models import recharge_value, return_balance, recharge_valid, search_by_name, search_by_type
# from .models import manager_query, manager_delete, manager_maintain, username_valid_register,verify_user_register
# from .models import search_bill, info_modify,loginpswd_modify,paypswd_modify, add_blacklists,delete_blacklists
from .forms import *
from .forms import LoginForm, RegistrationForm, RechargeForm, AddManagerForm, DeleteManagerForm, MaintainManagerForm
from .forms import MaintainUserForm, BillForm, ModifyForm, loginpswdmodifyform, paypswdmodifyform,AddBlacklistsForm,DeleteBlacklistsForm
# from __init__ import app


@app.route('/', methods=['POST', 'GET'])
@app.route('/tourist_index', methods=['POST', 'GET'])
def index():
    if request.method == "GET":
        form = LoginForm()
        hotels = show_good()
        planes = show_good(good_type='plane')
        return render_template("tourist_index.html", form=form, hotels = hotels, planes=planes)
    else:
        form = LoginForm(formdata=request.form)
        if form.validate():
            username = form.data['username']
            password = form.data['password']
            session['username'] = username
            if buyer_valid_login(username, password):
                session['type'] = 1
                return redirect(url_for('index'))
            elif seller_valid_login(username, password):
                session['type'] = 0
                return redirect(url_for('index'))
            elif administrator_valid_login(username, password):
                session['type'] = 2
                return redirect(url_for('add_manager'))
        is_login = 1
        return render_template("tourist_index.html", form=form, is_login=is_login)


@app.route('/logout',methods=['POST', "GET"])
def logout():
    session.pop('username', None)
    session.pop('type', None)
    return redirect(url_for('index'))


@app.route('/account', methods=['POST', 'GET'])
def account():
    messages = user_info_query(session['username'])
    if session['type'] == 1:
        usertype = "buyer"
    else:
        usertype = "seller"

    if request.method == 'GET':
        form_recharge = RechargeForm()
        value = return_balance(session['username'], session['type'])
        return render_template('recharge.html', form_recharge=form_recharge, value=value,
                               username=session['username'], messages=messages, usertype=usertype)
    else:
        form_recharge = RechargeForm(formdata=request.form)
        value = return_balance(session['username'], session['type'])
        if form_recharge.validate():
            revalue = recharge_valid(form_recharge.data['cardnumber'], form_recharge.data['password'])
            if revalue:
                recharge_value(session['username'], revalue)
                return redirect(url_for('account'))
            else:
                    return redirect(url_for('account'))
        else:
            print(form_recharge.errors, "错误信息")
    return render_template('recharge.html', form_recharge=form_recharge, value=value,
                           username=session['username'], messages=messages, usertape=usertype)


@app.route('/maintain/user', methods=['POST', 'GET'])
def maintain_user():
    if request.method == 'GET':
        form = MaintainUserForm()
        return render_template('users.html', form=form)
    else:
        form = MaintainUserForm(formdata=request.form)
        if form.validate():
            if form.data['username']:
                users = search_by_name(form.data['username'])
            else:
                users = search_by_type(form.data['type'])
        else:
            print(form.errors, "错误信息")
    return render_template('users.html', form=form, users=users)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        form_register = RegistrationForm()
        return render_template('register.html',form_register=form_register)
    else:
        form_register = RegistrationForm(formdata=request.form)
        if form_register.validate():
            if form_register.data['typeid'] == 1:
                if username_valid_register(form_register.data['username']):
                    buyer_register(form_register.data)
                    return redirect(url_for('index'))
            else:
                if username_valid_register(form_register.data['username']):
                    seller_register(form_register.data)
                    return redirect(url_for('index'))
    return render_template('register.html',form_register=form_register)


@app.route('/delete/manager', methods=['POST', 'GET'])
def delete_manager():
    if 'username' in session and session['username'] == 'software':
        print("success")
        if request.method == "GET":
            form = DeleteManagerForm()
            return render_template("delete-manager.html", form=form)
        else:
            form = DeleteManagerForm(formdata=request.form)
            if form.validate():
                username = form.data['username']
                if request.form['key'] == "query":
                    print("query")
                    query = manager_query(username)
                    return render_template('delete-manager.html', form=form, query=query)
                if request.form['key'] == "submit":
                    print("submit")
                    message = manager_delete(username)
                    return render_template('delete-manager.html', form=form, message=message)
    else:
        return redirect(url_for("index"))


@app.route('/maintain/manager', methods=['POST', 'GET'])
def maintain_manager():
    if 'username' in session and session['username'] == 'software':
        if request.method == "GET":
            form = MaintainManagerForm()
            return render_template("maintain-manager.html", form=form)
        else:
            form = MaintainManagerForm(formdata=request.form)
            if form.validate():
                username = form.data['username']
                if request.form['key'] == "query":
                    query = manager_query(username)
                    return render_template('maintain-manager.html', form=form, query=query)
                if request.form['key'] == "submit":
                    permission = 0
                    if form.data['deleteright']:
                        permission += 16
                    if form.data['addright']:
                        permission += 8
                    if form.data['arbitrationright']:
                        permission += 4
                    if form.data['blacklistright']:
                        permission += 2
                    if form.data['viewright']:
                        permission += 1
                    message = manager_maintain(username, permission)
                    return render_template('maintain-manager.html', form=form, message=message)
    else:
        return redirect(url_for("index"))


@app.route('/add/manager',methods = ['POST', 'GET'])
def add_manager():
    if 'username' in session and session['username'] == 'software' or 'type' in session and session['type'] == 2:
        if request.method == "GET":
            form = AddManagerForm()
            return render_template("add-manager.html", form=form)
        else:
            form = AddManagerForm(formdata=request.form)
            if form.validate():
                data = form.data
                if data['checker']:
                    typeid = 0
                    permission = 0
                elif data['Super_admin']:
                    typeid = 2
                    permission = 31
                else:
                    typeid = 1
                    permission = 0
                if username_valid_register(data['username']):
                    manager_register(data['username'], data['password'], data['AuthenticationPassword'], typeid, permission)
                    return redirect(url_for('add_manager'))
            return redirect(url_for('add_manager'))
    return redirect(url_for('index'))


@app.route('/bill', methods=['POST', 'GET'])
def bill():
    if request.method == 'GET':
        form = BillForm()
        return render_template('bill.html', form=form, flag=0)
    else:
        form = BillForm(formdata=request.form)
        if form.validate():
            print(form.data)
            year = form.data['year']
            month = form.data['month']
            print(year)
            print(month)
            # username = session['username']
            username = "Zhang"
            data = search_bill(year, month, username)
            return render_template("bill.html", form=form, flag=1, bills=data)
        else:
            print(form.errors)
            return render_template("bill.html", form=form, flag=0)


@app.route('/manager/blacklists', methods=['POST','GET'])  #黑名单显示界面 blacklists.html界面展示
def blacklists():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='lyx09241021/?', db='onlinepayment', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM blacklists"  #idtype 1为买家 0为卖家
    cursor.execute(sql)
    u = cursor.fetchall()
    conn.close()
    return render_template('blacklists.html',u=u)  #u为传递信息


@app.route('/manager/addblacklists', methods=['POST','GET'])  #黑名单显示界面 blacklists.html界面展示
def addblacklists():
    if request.method == "GET":
        form = AddBlacklistsForm()
        print("add1")
        return render_template("add_blacklists.html", form=form)
    else:
        form = AddBlacklistsForm(formdata=request.form)
        if form.validate():
            print("add2")
            #if form.validate():
            data=form.data
            print(data)
            print("!")
            add_blacklists(data)
            return redirect(url_for('blacklists'))
    return render_template('add_blacklists.html.html')

@app.route('/manager/deleteblacklists', methods=['POST','GET'])  #黑名单显示界面 blacklists.html界面展示
def deleteblacklists():
        if request.method == "GET":

            form = DeleteBlacklistsForm()
            print("in")
            return render_template("delete_blacklists.html", form=form)
        else:
            print("else")
            form = DeleteBlacklistsForm(formdata=request.form)
            if form.validate():
                print("delete?")
                data = form.data
                delete_blacklists(data)
                return redirect(url_for('blacklists'))
        return render_template('delete_blacklists.html')



@app.route('/info/forloginpswd', methods=['POST','GET'])
def loginpswdmodify():
    if request.method == "GET":
        print("get")
        form = loginpswdmodifyform()
        return render_template("loginpwdmodify.html", form=form)
    else:
        form =  loginpswdmodifyform(formdata=request.form)
        if form.validate():
            print("loginpswd")
            if loginpswd_modify(session['username'], form.data):
                print("success!")
                return redirect(url_for('account'))
            else:
                print("wrongpassword")

        else:
            print("错误")
            print(form.errors, "错误信息")
        return render_template("loginpwdmodify.html", form=form)


@app.route('/info/forpaypswd', methods=['POST','GET'])
def paypswdmodify():
    if request.method == "GET":
        print("get")
        form = paypswdmodifyform()
        return render_template("paypwdmodify.html", form=form)
    else:
        form = paypswdmodifyform(formdata=request.form)
        if form.validate():
            print("success")
            print(form.data)
            print(session['username'])
            if paypswd_modify(session['username'], form.data):
                print("success!")
                return redirect(url_for('account'))
            else:
                print("wrongpassword")
        else:
            print(form.errors, "错误信息")
        return render_template("paypwdmodify.html", form=form)





@app.route('/info/modify', methods=['POST','GET'])
def infomodify():
    if request.method == "GET":
        form = ModifyForm()
        return render_template("infomodify.html", form=form)
    else:
        form = ModifyForm(formdata=request.form)
        if form.validate():
            print("success")
            print(form.data)
            print(session['username'])
            info_modify(session['username'], form.data)
            if form.data['username']:
                session['username'] = form.data['username']
                print("changed")
            print("notchanged")
            return redirect(url_for('account'))
        else:
            print(form.errors, "错误信息")
        return render_template("infomodify.html", form=form)


# **********************************************************
# *********************** Group 3 **************************
# **********************************************************

@app.route('/QueryGood', methods=['POST', 'GET'])
def querygoods():
    if True or 'username' in session:
        if request.method == "GET":
            form = QueryGoodsForm()
            return render_template("query_good.html", form=form)
        else:
            form = QueryGoodsForm(formdata=request.form)
            if form.validate():
                goodname = form.data['goodname']
                query = good_info_query(goodname)
                return render_template("query_good.html", form=form, query=query)
    else:
        return redirect(url_for("index"))

@app.route('/tourist_product_detail/<int:id>')
def tourist_product_detail(id):
    hotel = select_good(id)
    return render_template('tourist_product_detail.html', title='Product detail', good=good)

@app.route('/admin_comment_review')
def admin_comment_review():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template('admin_comment_review.html',title = 'Product detail',user = user)


@app.route('/admin_verification', methods=['POST', 'GET'])
def admin_verification():
    if request.method == 'GET':
        goods = select_all()
        return render_template('admin_verification.html', title='Product detail', goods=goods)
    elif request.method == 'POST':
        good_id = request.form['good_id']
        is_pass(good_id)
        return json.dumps({'ok': 1})



@app.route('/buyer_comment')
def buyer_comment():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template('buyer_comment.html',title = 'Product detail',user = user)


@app.route('/buyer_index')
def buyer_index():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template('buyer_index.html',title = 'Product detail',user = user)


@app.route('/buyer_product_detail')
def buyer_product_detail():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template('buyer_product_detail.html',title = 'Product detail',user = user)


@app.route('/seller_add')
def seller_add():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template('seller_add.html',title = 'Product detail',user = user)


@app.route('/seller_edit')
def seller_edit():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template('seller_edit.html',title = 'Product detail',user = user)


@app.route('/seller_listofgoods')
def seller_listofgoods():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template('seller_listofgoods.html',title = 'Product detail',user = user)


@app.route('/seller_response')
def seller_response():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template('seller_response.html',title = 'Product detail',user = user)

