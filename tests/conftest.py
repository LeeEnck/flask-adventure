import os
import tempfile

import pytest
from sheol-adventure import create_app


@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
    })


    yield app


@pytest.fixture
def client(app):
    return app.test_client()

def runner(app):
    return app.test_cli_runner()
