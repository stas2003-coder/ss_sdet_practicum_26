import pytest

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService


@pytest.fixture(scope="function")
def init_driver():
    print("driver starting...")
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))
    driver.maximize_window()

    yield driver

    driver.quit()
    #driver.close()
    print("driver closed")