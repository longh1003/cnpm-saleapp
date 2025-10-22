from flask import Flask, render_template

from dao import load_categories, load_products

app = Flask(__name__)

@app.route("/")
def index():
    name = "My N"
    cates = load_categories()
    prods = load_products()
    return render_template("index.html", name=name, cates=cates, prods=prods)

if __name__=="__main__":
    with app.app_context():
        app.run(debug=True)
