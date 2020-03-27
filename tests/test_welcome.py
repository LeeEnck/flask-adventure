import sheol-adventure

def test_welcome(client):
    response = client.get('/')
    assert response
    assert b'href="/game/hell"' in response.data
