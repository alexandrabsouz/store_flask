from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SECRET_KEY'] = 'secret357951258654ey'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from store.admin import routes
from store.products import routes
