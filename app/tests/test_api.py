import pytest
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"BMI Calculator" in response.data

def test_predict_api_valid(client):
    test_data = {'height': 175, 'weight': 70}
    response = client.post('/predict', 
                          data=json.dumps(test_data),
                          content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'bmi' in data
    assert 'category' in data
    assert isinstance(data['bmi'], float)
    assert isinstance(data['category'], str)

def test_predict_api_invalid(client):
    # Test missing weight
    test_data = {'height': 175}
    response = client.post('/predict', 
                          data=json.dumps(test_data),
                          content_type='application/json')
    assert response.status_code == 400
    assert 'error' in json.loads(response.data)

    # Test invalid data types
    test_data = {'height': 'not_a_number', 'weight': 70}
    response = client.post('/predict', 
                          data=json.dumps(test_data),
                          content_type='application/json')
    assert response.status_code == 400
