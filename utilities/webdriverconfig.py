from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import FirefoxDriverManager
from dotenv import load_dotenv
import os

driver = os.environ.get("driver")

def setdriver() :
    if (driver == "CHROME"):
        return webdriver.Chrome(ChromeDriverManager().install())
    if (driver == "FIREFOX"):
        return webdriver.Firefox(FirefoxDriverManager().install())
    return webdriver.Remote('127.0.0.1:4444')
