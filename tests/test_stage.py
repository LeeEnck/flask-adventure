from sheol-adventure import stage
from flask import session

def test_stage(client):
    stages = {
    'response_hell': client.get('/game/hell'),
    'response_lavapit': client.get('/game/lavapit'),
    'response_graveyard': client.get('/game/graveyard'),
    'response_lavafalls': client.get('/game/lavafalls'),
    'response_luciferslair': client.get('/game/luciferslair'),
    'response_holygrail': client.get('/game/holygrail')
    }

    for stage in stage:
        response = stage.get(stage)
        assert response
        assert b'You are currently inside' in response.data
        assert b'My current environment is' in response.data
        assert b'I am compelled to' in response.data
        assert b'<form method="post">' in response.data
