from selenium.webdriver.support.ui import WebDriverWait

def wait(driver):
    return WebDriverWait(driver, 3)