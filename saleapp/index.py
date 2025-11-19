import math

from flask import Flask, render_template, request, redirect
from saleapp import app, login
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
