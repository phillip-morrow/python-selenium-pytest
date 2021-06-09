import os
import pytest
import requests

from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="class")
def login():
    domain = os.getenv('BASE_URL')
    port = os.getenv('BACK_END_PORT')
    pytest.baseUrl = f'{domain}:{port}'
    payload = {
        'username': os.getenv('TEST_USER'),
        'password': os.getenv('TEST_PASS')
    }
    response = requests.post(f'{pytest.baseUrl}/login', data=payload)
    pytest.cookies = response.cookies
    yield
