import pytest
from assertpy.assertpy import assert_that
from utilities.webdriver_waits import wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("driver_get")
class TestNavLinks:

    def test_nav_bar(self):
        navigationLinks = {
            'Home': '//div[text()="Public"]',
            'My Account': '//h2[text()="User Settings"]',
            'Bank Accounts': '//h2[text()="Bank Accounts"]',
            'Notifications': '//h2[text()="Notifications"]'
        }
        for key in navigationLinks:
            wait(self.driver).until(EC.visibility_of_element_located(
                (By.XPATH, f'//*[text()="{key}"]'))).click()
            header = wait(self.driver).until(EC.visibility_of_element_located(
                (By.XPATH, navigationLinks[key])))
            assert_that(header.is_displayed()).is_true()
