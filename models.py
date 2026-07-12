from extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__="users"  #optional

    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(80), unique=True , nullable =False)
    email = db.Column(db.String(200),unique = True, nullable = False)
    password_hash =db.Column(db.String(255), nullable = False)

    links = db.relationship("Link", backref = "user", lazy = True)


class Link(db.Model):
    __tablename__= "links"

    id = db.Column(db.Integer, primary_key = True)
    original_url = db.Column(db.String(200), unique =True, nullable = False)
    short_code = db.Column(db.String(100), nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    click_count = db.Column(db.Integer, default = 0)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False )
