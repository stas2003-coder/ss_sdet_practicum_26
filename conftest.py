import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService

from tools.fake_data import fake
from tools.loger import get_logger

loger = get_logger("INIT_STEP")


@pytest.fixture(scope="function")
def init_driver():
    loger.info("driver starting...")
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))
    driver.maximize_window()

    yield driver

    driver.close()
    driver.quit()
    loger.info("driver closed")


@pytest.fixture(scope="function")
def init_data():
    loger.info("Test data initialisation")
    dict_data = {}
    dict_data["name_data"] = fake.full_name()
    dict_data["pass_data"] = fake.password()
    dict_data["email_data"] = fake.email()
    dict_data["automation"] = fake.random_choice()
    return dict_data