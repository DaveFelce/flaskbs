from typing import Generator

import pytest

from sqlalchemy_utils import create_database, database_exists, drop_database

from flaskbs import create_app
from flaskbs.db import db


@pytest.fixture(scope="session")
def app():
    app = create_app(testing=True)

    yield app


@pytest.fixture(scope="session", autouse=True)
def setup_db(app) -> Generator:
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
def setup_tables(app) -> Generator:
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
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
