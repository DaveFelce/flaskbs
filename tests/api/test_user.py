def test_user(client):
    response = client.get("/user/hank")
    assert response.data == b"Hello, hank"
