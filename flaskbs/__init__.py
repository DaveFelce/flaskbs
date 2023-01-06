import os

from typing import Any

from flask import Flask
from flask_migrate import Migrate

from flaskbs.api.endpoints import user
from flaskbs.core.config import DevelopmentConfig, TestingConfig
from flaskbs.db import db

migrate = Migrate()


def create_app(testing: bool = False) -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    if testing:
        app.config.from_object(TestingConfig())
    else:
        app.config.from_object(DevelopmentConfig())

    # database
    db.init_app(app)
    migrate.init_app(app, db)

    # blueprints
    app.register_blueprint(user.bp)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello/<name>")
    def hello(name: str) -> Any:
        return f"Hello, {name}"

    return app
