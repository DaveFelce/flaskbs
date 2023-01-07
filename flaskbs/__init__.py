from http import HTTPStatus

from flask import Flask, Response, jsonify
from flask_migrate import Migrate

from flaskbs.api.endpoints import user
from flaskbs.core.config import development_settings, testing_settings
from flaskbs.db import db

migrate = Migrate()


def create_app(testing: bool = False) -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    if testing:
        app.config.from_object(testing_settings)
    else:
        app.config.from_object(development_settings)

    # database
    db.init_app(app)
    migrate.init_app(app, db)

    # blueprints
    app.register_blueprint(user.bp)

    # custom error handlers
    @app.errorhandler(HTTPStatus.NOT_FOUND)
    def resource_not_found(e: Exception) -> tuple[Response, HTTPStatus]:
        return jsonify(error=str(e)), HTTPStatus.NOT_FOUND

    return app
