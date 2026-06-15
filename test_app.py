import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"AWS CodePipeline Practice App!" in response.data

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
