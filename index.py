from flask import Flask, render_template, request

import dao
from dao import load_categories, load_products

app = Flask(__name__)

@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    name = "My N"
    cates = load_categories()
    prods = load_products(q, cate_id)
    return render_template("index.html", name=name, cates=cates, prods=prods)


@app.route("/products/<int:id>")
def details(id):
    product = dao.load_products_by_id(id)
    return render_template("product-details.html", product=product)

if __name__=="__main__":
    with app.app_context():
        app.run(debug=True)
