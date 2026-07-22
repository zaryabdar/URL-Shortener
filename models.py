from extensions import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from itsdangerous import URLSafeTimedSerializer
from flask import current_app


class User(UserMixin, db.Model):
    __tablename__="users"  #optional

    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(80), unique=True , nullable =False)
    email = db.Column(db.String(200),unique = True, nullable = False)
    password_hash =db.Column(db.String(255), nullable = False)

    links = db.relationship("Link", backref = "user", lazy = True)

    def get_reset_token(self):
        serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
        return serializer.dumps(self.email)

    @staticmethod
    def verify_reset_token(token, expires_sec=1800):
        serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])

        try:
            email = serializer.loads(token, max_age=expires_sec)
        except Exception:
            return None

        return User.query.filter_by(email=email).first()


class Link(db.Model):
    __tablename__= "links"

    id = db.Column(db.Integer, primary_key = True)
    original_url = db.Column(db.String(200), unique =True, nullable = False)
    short_code = db.Column(db.String(100), nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.now)
    click_count = db.Column(db.Integer, default = 0)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False )

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))