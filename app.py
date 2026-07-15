from flask import Flask, render_template
from config import Config
from extensions import db,login_manager
from flask_migrate import Migrate
from models import User, Link
from routes.auth import auth
from routes.main import main

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

login_manager.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)