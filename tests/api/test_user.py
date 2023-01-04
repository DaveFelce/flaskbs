def test_user(client) -> None:
    response = client.get("/user/hank")
    assert response.data == b"Hello, hank"
