from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv
import os

load_dotenv()

driver = os.environ.get("DRIVER")

def setdriver() :
    if(driver == 'CHROME'):
        return webdriver.Chrome(ChromeDriverManager().install())
    if(driver == 'FIREFOX'):
        return webdriver.Firefox(GeckoDriverManager().install())
    return webdriver.Remote(os.environ.get('GRID_URL'))
