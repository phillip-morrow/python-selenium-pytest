import os
import pytest
from pytest_html_reporter import attach
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities.webdriver_config import setdriver
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="class")
def driver_get(request):
    driver = setdriver()
    wait = WebDriverWait(driver, 3)
    domain = os.getenv('BASE_URL')
    port = os.getenv('FRONT_END_PORT')
    baseUrl = f'{domain}:{port}'
    driver.get(baseUrl)
    wait.until(EC.visibility_of_element_located(
        (By.ID, "username"))).send_keys(os.getenv("TEST_USER"))
    driver.find_element(By.ID, "password").send_keys(
        os.getenv("TEST_PASS"))
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[contains(text(), 'Sign In')][not(@disabled)]"))).click()
    request.cls.driver = driver
    yield
    attach(data=driver.get_screenshot_as_png())
    driver.find_element_by_xpath("//*[text()='Logout']").click()
    driver.close()
