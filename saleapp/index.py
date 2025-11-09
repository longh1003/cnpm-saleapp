import math

from flask import Flask, render_template, request
from saleapp import app
import dao
from dao import load_categories, load_products


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


@app.route("/products/<int:id>")
def details(id):
    product = dao.load_products_by_id(id)
    return render_template("product-details.html", product=product)

@app.context_processor
def common_attribute():
    return {
        "cates": dao.load_categories()
    }

if __name__=="__main__":
    with app.app_context():
        app.run(debug=True)
