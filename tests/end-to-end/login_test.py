import pytest
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import dotenv_values

config = dotenv_values('../.env')

@pytest.mark.usefixtures("driver_init")
class TestLogin():

    def testUserLogin(self):
        self.driver.get(os.environ.get('BASE_URL'))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.ID, 'username')).send_keys(config['USERNAME'])
        self.driver.find_element_by_id('password').send_keys(config['PASSWORD'])