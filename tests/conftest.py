import pytest
from appium import webdriver
#from utils.config import CONFIG

@pytest.fixture
def driver():
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub")
    yield driver
    driver.quit()
