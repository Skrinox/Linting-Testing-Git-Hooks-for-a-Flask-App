import pytest
from app import app


@pytest.fixture
def client():
    client = app.test_client()
    yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_add_item(client):
    response = client.post('/add', data={'item': 'Test item 1'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Testtttttt item 1' in response.data




