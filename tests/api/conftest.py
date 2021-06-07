import os
import pytest
import requests

from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def login():
    domain = os.environ.get('BASE_URL')
    port = os.environ.get('BACK_END_PORT')
    pytest.baseUrl = f'{domain}:{port}'
    payload = {
        'username': os.environ.get('TEST_USER'),
        'password': os.environ.get('TEST_PASS')
    }
    response = requests.post(f'{pytest.baseUrl}/login', data=payload)
    pytest.cookies = response.cookies
    yield
