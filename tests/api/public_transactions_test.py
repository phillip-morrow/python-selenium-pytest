import os
from types import resolve_bases
from assertpy.assertpy import soft_assertions
import dotenv
import pytest
import requests
from assertpy import assert_that
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.usefixtures("login")
class TestPublicTransactions:
    domain = os.environ.get('BASE_URL')
    port = os.environ.get('BACK_END_PORT')
    baseUrl = f'{domain}:{port}'

    def test_get_public_transactions(self):
        response = requests.get(f'{self.baseUrl}/public')

        response_payload = response.json()

        transactions = [results['results'] for results in response_payload]
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)
            assert_that(transactions).is_not_empty()
