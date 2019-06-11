from app import app
from flask import render_template

@app.route('/')
@app.route('/tourist_index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("tourist_index.html",title = 'Home',user = user)


@app.route('/tourist_product_detail')
def tourist_product_detail():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template('tourist_product_detail.html',title = 'Product detail',user = user)


@app.route('/admin_comment_review')
def admin_comment_review():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template('admin_comment_review.html',title = 'Product detail',user = user)


@app.route('/admin_verification')
def admin_verification():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template('admin_verification.html',title = 'Product detail',user = user)


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
