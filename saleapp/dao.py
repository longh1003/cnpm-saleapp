import hashlib
import json

from saleapp import app, db
from saleapp.models import Category, Product, User


def load_categories():
    # with open("data/categories.json", encoding="utf-8") as f:
    #     cate = json.load(f)
    #     return cate
    return Category.query.all()

def load_products(q=None, cate_id=None, page=None):
    # with open("data/products.json", encoding="utf-8") as f:
    #     products = json.load(f)
    #
    #     if q:
    #         products = [ p for p in products if p["name"].find(q) >= 0]
    #
    #     if id:
    #         products = [ p for p in products if p["cate_id"].__eq__(int(id))]
    #     return products
    query = Product.query

    if q:
        query = query.filter(Product.name.contains(q))
    if cate_id:
        query = query.filter(Product.cate_id.__eq__(cate_id))
    if page:
        size = app.config["PAGE_SIZE"]
        start = (int(page)-1)*size
        end = start+size
        query = query.slice(start, end)

    return query.all()

def count_product():
    return Product.query.count()


def auth_user(username, password):
    password = hashlib.md5(password.encode("utf-8")).hexdigest()
    return User.query.filter(User.username.__eq__(username), User.password.__eq__(password)).first()


def add_user(name, username, password):
    password = hashlib.md5(password.encode("utf-8")).hexdigest()
    user = User(name=name, username=username, password=password)

    db.session.add(user)
    db.session.commit()
    return user


def get_user_by_id(user_id):
    return User.query.get(user_id)


def load_products_by_id(id):
    # with open("data/products.json", encoding="utf-8") as f:
    #     products = json.load(f)
    # if id:
    #     products = [ p for p in products if p["id"].__eq__(int(id))]
    #     print(products)
    #
    # return products
    query = Product.query
    query = query.get(id)
    return query


if __name__=="__main__":
    with app.app_context():
        print(auth_user(username="user", password="123"))
        pass

