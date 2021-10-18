from flask_sqlalchemy import SQLAlchemy
from api import *

class Details1(db.Model):
    __tablename__ = 'details'
    id=db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(80))
    user_email = db.Column(db.String(80))
    status= db.Column(db.Boolean)