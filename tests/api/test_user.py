from http import HTTPStatus

from flask.testing import FlaskClient
from sqlalchemy.future import select
from sqlalchemy.orm.scoping import scoped_session

from flaskbs.models import User


def test_get_user(client: FlaskClient, user: User) -> None:
    resp = client.get(f"/user/{user.username}")

    assert resp
    assert resp.json == {"greeting": f"hello, {user.email}"}


def test_post_user(client: FlaskClient, db_session: scoped_session) -> None:
    username = "test-person"
    email = "testperson@test.com"
    payload = {
        "username": username,
        "email": email,
    }

    resp = client.post(
        "/user",
        json=payload,
    )

    user = db_session.execute(select(User).where(User.username == username)).scalar_one()
    assert user.email == email

    assert resp.status_code == HTTPStatus.OK
