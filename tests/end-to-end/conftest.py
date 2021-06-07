import os
import pytest
from pytest_html_reporter import attach
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities.webdriver_config import setdriver
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def driver_get(request):
    driver = setdriver()
    wait = WebDriverWait(driver, 3)
    domain = os.environ.get('BASE_URL')
    port = os.environ.get('FRONT_END_PORT')
    baseUrl = f'{domain}:{port}'
    driver.get(baseUrl)
    wait.until(EC.visibility_of_element_located(
        (By.ID, "username"))).send_keys(os.environ.get("TEST_USER"))
    driver.find_element(By.ID, "password").send_keys(
        os.environ.get("TEST_PASS"))
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[contains(text(), 'Sign In')][not(@disabled)]"))).click()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    yield
    attach(data=driver.get_screenshot_as_png())
    driver.find_element_by_xpath("//*[text()='Logout']")
    driver.close()
