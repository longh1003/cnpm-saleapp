import json

from saleapp import app,db
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship


class Category(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(150), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(150), nullable=False, unique=True)
    image = Column(String(300), nullable=False, default="https://res.cloudinary.com/dy1unykph/image/upload/v1729091967/419VTYVRD1L._AC__vih8qs.jpg")
    price = Column(Float, default=0.0)
    cate_id = Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__=="__main__":
    with app.app_context():
        # db.create_all()
        # c1 = Category(name="Laptop")
        # c2 = Category(name="Mobile")
        # c3 = Category(name="Tablet")
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()

        # with open("data/products.json", encoding="utf-8") as f:
        #     products = json.load(f)
        # for p in products:
        #     p = Product(
        #         name=p["name"],
        #         image=p["image"],
        #         price=p["price"],
        #         cate_id=p["cate_id"]
        #     )
        #     db.session.add(p)
        #
        # db.session.commit()
        pass
