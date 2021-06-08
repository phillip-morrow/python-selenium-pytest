from utilities.request_helper import headers
import pytest
import requests
from assertpy.assertpy import assert_that, soft_assertions


@pytest.mark.usefixtures("login")
class TestUsers:

    def test_get_users(self):
        response = requests.get(
            f'{pytest.baseUrl}/users', headers=headers(pytest.cookies))

        response_payload = response.json()

        users = response_payload['results']

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)
            assert_that(users).is_not_empty()
