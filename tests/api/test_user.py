from flask.testing import FlaskClient


def test_user(client: FlaskClient) -> None:
    response = client.get("/user/hank")

    assert response
    assert response.json == {"greeting": "hello, hank"}
