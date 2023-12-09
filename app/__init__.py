from flask import Flask
from flask_migrate import Migrate

from app.config import Config
from app.crypt import bcrypt
from app.db import db
from app.routes.user_routes import user_route


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(user_route)

    db.init_app(app)
    bcrypt.init_app(app)
    Migrate(app, db)

    return app
