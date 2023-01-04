from flask.testing import FlaskClient


def test_user(client: FlaskClient) -> None:
    response = client.get("/user/hank")
    assert response.data == b"Hello, hank"
