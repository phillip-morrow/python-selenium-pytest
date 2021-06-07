from assertpy.assertpy import soft_assertions
import pytest
import requests
from assertpy import assert_that
from dotenv import load_dotenv
from utilities.request_helper import headers

load_dotenv()


@pytest.mark.usefixtures("login")
class TestPublicTransactions:

    def test_get_public_transactions(self):
        response = requests.get(
            f'{pytest.baseUrl}/transactions/public', headers=headers(pytest.cookies))

        response_payload = response.json()

        transactions = response_payload['results']

        print(transactions)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)
            assert_that(transactions).is_not_empty()
