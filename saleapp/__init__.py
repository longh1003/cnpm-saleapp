import cloudinary
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.theme import Bootstrap4Theme

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:root@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 2
app.secret_key = "digdigdidgididgidi"

cloudinary.config(cloud_name='dqu2xhiz9',
                  api_key='467684615474232',
                  api_secret='NiQ9l-zlzVYaWR0t2XhfsShAu_o')

db = SQLAlchemy(app)
login = LoginManager(app)

