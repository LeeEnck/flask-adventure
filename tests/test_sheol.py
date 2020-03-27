import sheol-adventure
from sheol-adventure import create_app

def test_import():
    assert sheol-adventure

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'sheol-adventure'
