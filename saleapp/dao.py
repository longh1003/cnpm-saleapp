import json

def load_categories():
    with open("data/categories.json", encoding="utf-8") as f:
        cate = json.load(f)
        return cate

def load_products(q=None, id=None):
    with open("data/products.json", encoding="utf-8") as f:
        products = json.load(f)

        if q:
            products = [ p for p in products if p["name"].find(q) >= 0]

        if id:
            products = [ p for p in products if p["cate_id"].__eq__(int(id))]
        return products

def load_products_by_id(id):
    with open("data/products.json", encoding="utf-8") as f:
        products = json.load(f)
    if id:
        products = [ p for p in products if p["id"].__eq__(int(id))]
        print(products)

    # fix this
    return products

if __name__=="__main__":
    print(load_products_by_id(1))
    pass
