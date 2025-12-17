import math

import cloudinary.uploader
from flask import Flask, render_template, request, redirect, session, jsonify
from saleapp import app, login, admin ,db, utils
import dao
from dao import load_categories, load_products
from flask_login import login_user, current_user, logout_user


@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    page = request.args.get("page")
    name = "My N"
    cates = load_categories()
    prods = load_products(q=q, cate_id=cate_id, page=page)
    pages = math.ceil(dao.count_product()/app.config["PAGE_SIZE"])
    return render_template("index.html", name=name, cates=cates, prods=prods, pages=pages)

@app.route("/login", methods=['get', 'post'])
def login_my_user():
    if current_user.is_authenticated:
        return redirect("/")

    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        user = dao.auth_user(username, password)

        if user:
            login_user(user)
            return redirect("/")

    return render_template("login.html")

@app.route('/admin-login', methods=['post'])
def admin_login_process():
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.auth_user(username, password)

    if user:
        login_user(user)
        return redirect('/admin')
    else:
        err_msg = "Tài khoản hoặc mật khẩu không đúng!"


@app.route("/register", methods=['get','post'])
def register():
    err_msg = None

    if request.method.__eq__('POST'):
        password = request.form.get('password')
        confirm = request.form.get('confirm')

        if password != confirm:
            err_msg = "Mật khẩu không khớp!"
        else:
            name = request.form.get('name')
            username = request.form.get('username')
            avatar = request.files.get('avatar')
            file_path = None
            if avatar:
                res = cloudinary.uploader.upload(avatar)
                file_path = res['secure_url']
            try:
                dao.add_user(name, username, password, avatar=file_path)
                return redirect('/login')
            except:
                db.session.rollback()
                err_msg = "Hệ thống đang bị lỗi! Vui lòng quay lại sau!"
    return render_template('register.html', err_msg=err_msg)

@app.route('/cart')
def cart():

    # session['cart'] = {
    #     "1": {
    #         "id": "1",
    #         "name": "Iphone 15 ProMax",
    #         "price": 1500,
    #         "quantity": 2
    #     },
    #     "2": {
    #         "id": "2",
    #         "name": "Samsung Galaxy",
    #         "price": 1000,
    #         "quantity": 1
    #     },
    # }

    return render_template('cart.html')

@app.route('/api/carts', methods=['post'])
def add_to_cart():
    cart = session.get('cart')

    if not cart:
        cart = {}

    id = str(request.json.get('id'))

    if id in cart:
        cart[id]['quantity'] += 1
    else:
        cart[id] = {
            "id": id,
            'name': request.json.get('name'),
            'price': request.json.get('price'),
            'quantity': 1
        }

    session['cart'] = cart

    print(session['cart'])

    return jsonify(utils.count_cart(cart))


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)


@app.route("/products/<int:id>")
def details(id):
    product = dao.load_products_by_id(id)
    return render_template("product-details.html", product=product)


@app.route('/logout')
def logout_my_user():
    logout_user()
    return redirect("/login")


@app.context_processor
def common_attribute():
    return {
        "cates": dao.load_categories()
    }

if __name__=="__main__":
    with app.app_context():
        app.run(debug=True)
