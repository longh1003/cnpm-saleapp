import json

from saleapp import app,db
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Boolean, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as EnumRole
from flask_login import UserMixin

class Base(db.Model):
    __abstract__=True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False, unique=True)
    created_date = Column(DateTime, default=datetime.now())
    active = Column(Boolean, default=True)

    def __str__(self):
        return self.name


class Category(Base):
    products = relationship('Product', backref='category', lazy=True)

class UserRole(EnumRole):
    USER = 1
    ADMIN = 2

class Product(Base):
    image = Column(String(300), nullable=False, default="https://res.cloudinary.com/dy1unykph/image/upload/v1729091967/419VTYVRD1L._AC__vih8qs.jpg")
    price = Column(Float, default=0.0)
    cate_id = Column(Integer, ForeignKey(Category.id), nullable=False)


class User(Base, UserMixin):
    username = Column(String(20), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(300), default="https://res.cloudinary.com/dy1unykph/image/upload/v1729091967/419VTYVRD1L._AC__vih8qs.jpg")
    role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.name


if __name__=="__main__":
    with app.app_context():
        # db.create_all()
        # c1 = Category(name="Laptop")
        # c2 = Category(name="Mobile")
        # c3 = Category(name="Tablet")
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()
        #
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
        import hashlib

        password = hashlib.md5("123".encode("utf-8")).hexdigest()

        u1 = User(name="test user",username="user", password=password)
        db.session.add(u1)
        db.session.commit()
        pass
