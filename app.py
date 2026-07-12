from flask import Flask, render_template
from config import Config
from extensions import db 
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

from models import User, Link

if __name__ == "__main__":
    app.run(debug=True)