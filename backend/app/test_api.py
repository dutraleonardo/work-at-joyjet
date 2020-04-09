import json

import pytest

from api import create_app


@pytest.fixture()
def testing_client():
    app_instance = create_app(config='TEST')
    test_client = app_instance.test_client()
    context = app_instance.app_context()
    context.push()
    yield test_client


def load_data(filepath):
    with open(filepath) as f:
        data = json.load(f)
    return data


def test_level1(testing_client):

    data = load_data('../level1/data.json')
    response = testing_client.post('/cart_checkout', json=data)
    output = load_data('../level1/output.json')
    assert response.status_code == 200
    assert output == response.get_json()


def test_level2(testing_client):

    data = load_data('../level2/data.json')
    response = testing_client.post('/cart_checkout', json=data)
    output = load_data('../level2/output.json')
    assert response.status_code == 200
    assert output == response.get_json()


def test_level3(testing_client):

    data = load_data('../level3/data.json')
    response = testing_client.post('/cart_checkout', json=data)
    output = load_data('../level3/output.json')
    assert response.status_code == 200
    assert output == response.get_json()
