from enum import unique
from store import db


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullabe=False, unique=True)
    
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullabe=False, unique=True)
    
    
db.create_all()
    