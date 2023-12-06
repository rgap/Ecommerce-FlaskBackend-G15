from app.config import Config
from app.db import db
from app.routes.product_routes import product_route
from flask import Flask
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(product_route)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
