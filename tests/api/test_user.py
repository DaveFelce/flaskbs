from flask.testing import FlaskClient

from flaskbs.models import User


def test_user(client: FlaskClient, user: User) -> None:
    response = client.get(f"/user/{user.username}")

    assert response
    assert response.json == {"greeting": f"hello, {user.email}"}
