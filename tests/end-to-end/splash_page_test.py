from assertpy.assertpy import assert_that
import pytest
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.usefixtures("driver_get")
class TestSplashPage:

    def test_public_transactions_list(self):
        transactions = json.loads(self.driver.wait_for_request(
            '/transactions/public').response.body)['results']
        for transaction in transactions:
            id = transaction['id']
            assert_that(len(self.driver.find_elements(
                By.XPATH, f'//*[contains(@data-test, "{id}")]'))).is_equal_to(1)

    def test_nav_bar(self):
        wait = WebDriverWait(self.driver, 3)
        navigationLinks = {
            'Home': '//div[text()="Public"]',
            'My Account': '//h2[text()="User Settings"]',
            'Bank Accounts': '//h2[text()="Bank Accounts"]',
            'Notifications': '//h2[text()="Notifications"]'
        }
        for key in navigationLinks:
            self.driver.find_element(By.XPATH, f'//*[text()="{key}"]').click()
            header = wait.until(EC.visibility_of_element_located(
                (By.XPATH, navigationLinks[key])))
            assert_that(header.is_displayed()).is_true()
