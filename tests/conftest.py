from typing import Generator

import pytest

from flask import Flask
from flask.testing import FlaskClient
from sqlalchemy_utils import create_database, database_exists, drop_database

from flaskbs import create_app
from flaskbs.db import db


@pytest.fixture(scope="session")
def app() -> Generator:
    test_app = create_app(testing=True)

    yield test_app


@pytest.fixture(scope="session", autouse=True)
def setup_db(app: Flask) -> Generator:
    with app.app_context():
        if db.engine.url.database != "flaskbs_test":
            raise ValueError(f"Unsafe attempt to recreate database: {db.engine.url.database}")

        if database_exists(db.engine.url):
            drop_database(db.engine.url)
        create_database(db.engine.url)

        yield

        # At end of all tests, drop the test db
        drop_database(db.engine.url)


@pytest.fixture(scope="function", autouse=True)
def setup_tables(app: Flask) -> Generator:
    """
    autouse set to True so will be run before each test function, to set up tables
    and tear them down after each test runs
    """
    with app.app_context():
        db.metadata.create_all(bind=db.engine)

    yield

    # # Drop all tables after each test
    with app.app_context():
        db.metadata.drop_all(bind=db.engine)


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()
