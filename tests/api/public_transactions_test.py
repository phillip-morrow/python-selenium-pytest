from assertpy.assertpy import soft_assertions
import pytest
import requests
from assertpy import assert_that
from dotenv import load_dotenv
from utilities.request_helper import headers

load_dotenv()


@pytest.mark.usefixtures("login")
class TestPublicTransactions:

    def test_get_public_transactions_with_token(self):
        response = requests.get(
            f'{pytest.baseUrl}/transactions/public', headers=headers(pytest.cookies))

        response_payload = response.json()

        transactions = response_payload['results']

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)
            assert_that(transactions).is_not_empty()

    def test_get_public_transactions_without_token(self):
        response = requests.get(
            f'{pytest.baseUrl}/transactions/public')

        response_payload = response.json()

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(401)
            assert_that(response_payload).is_equal_to({'error': 'Unauthorized'})

    def test_transaction_post(self):
        request_payload = {"transactionType": "payment", "amount": "5000",
                           "description": "lot o money", "senderId": "Hk_RyxBFd", "receiverId": "t45AiwidW"}

        response = requests.post(f'{pytest.baseUrl}/transactions',
                                 headers=headers(pytest.cookies), data=request_payload)

        response_payload = response.json()

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)
            assert_that(response_payload['transaction']
                        ['status']).is_equal_to('complete')
