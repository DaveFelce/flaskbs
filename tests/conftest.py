from typing import Generator

import pytest

from flask import Flask
from flask.testing import FlaskClient
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy_utils import create_database, database_exists, drop_database

from flaskbs import create_app
from flaskbs.db import db
from flaskbs.models import User


@pytest.fixture(scope="module")
def main_db_session() -> Generator[scoped_session, None, None]:
    yield db.session


@pytest.fixture(scope="session")
def test_app() -> Flask:
    app = create_app(testing=True)

    return app


@pytest.fixture(scope="session", autouse=True)
def setup_db(test_app: Flask) -> Generator:  # pylint: disable=redefined-outer-name
    with test_app.app_context():
        if db.engine.url.database != "flaskbs_test":
            raise ValueError(f"Unsafe attempt to recreate database: {db.engine.url.database}")

        if database_exists(db.engine.url):
            drop_database(db.engine.url)
        create_database(db.engine.url)

        yield db

        # At end of all tests, drop the test db
        drop_database(db.engine.url)


@pytest.fixture(scope="function", autouse=True)
def setup_tables(test_app: Flask) -> Generator:  # pylint: disable=redefined-outer-name
    """
    autouse set to True so will be run before each test function, to set up tables
    and tear them down after each test runs
    """
    with test_app.app_context():
        db.metadata.create_all(bind=db.engine)

    yield

    # # Drop all tables after each test
    with test_app.app_context():
        db.metadata.drop_all(bind=db.engine)


@pytest.fixture(scope="function")
def db_session(main_db_session: scoped_session) -> Generator[scoped_session, None, None]:
    yield main_db_session
    main_db_session.rollback()
    main_db_session.expunge_all()


@pytest.fixture()
def client(test_app: Flask) -> FlaskClient:  # pylint: disable=redefined-outer-name
    return test_app.test_client()


@pytest.fixture(scope="function")
def user(db_session: scoped_session) -> User:
    test_user = User(username="test-user", email="testuser@test.com")
    db_session.add(test_user)
    db_session.commit()

    return test_user
