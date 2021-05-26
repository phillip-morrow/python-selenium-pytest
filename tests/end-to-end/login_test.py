import pytest
import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.usefixtures("driver_get")
class TestLogin:

    def test_user_login(self):
        wait = WebDriverWait(self.driver, 3)
        self.driver.get(os.environ.get('BASE_URL'))
        wait.until(EC.visibility_of_element_located(
            (By.ID, "username"))).send_keys(os.environ.get("TEST_USER"))
        self.driver.find_element(By.ID, "password").send_keys(
            os.environ.get("TEST_PASS"))
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(text(), 'Sign In')][not(@disabled)]"))).click()
        transactions = json.loads(self.driver.wait_for_request('/transactions/public').response.body)['results']
        for transaction in transactions:
            id = transaction['id']
            assert(self.driver.find_element(By.XPATH, f'//li[contains(@data-test, "{id}")]'))
