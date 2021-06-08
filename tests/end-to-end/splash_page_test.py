from assertpy.assertpy import assert_that, soft_assertions
import pytest
import json
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from utilities.webdriver_waits import wait

load_dotenv()


@pytest.mark.usefixtures("driver_get")
class TestSplashPage:

    def test_public_transactions_list(self):
        transactions = json.loads(self.driver.wait_for_request(
            '/transactions/public').response.body)['results']
        for transaction in transactions:
            id = transaction['id']
            assert_that(len(self.driver.find_elements(
                By.XPATH, f'//li[contains(@data-test, "{id}")]'))).is_equal_to(1)
