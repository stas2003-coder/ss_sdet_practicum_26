import time
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService



# def test_smoke_1():
#     with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as browser:
#         browser.get("https://practice-automation.com/form-fields/")
#         time.sleep(5)
#         assert browser.title == "Form Fields | Practice Automation"


# def test_smoke_2():
#     driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))
#     driver.get("https://practice-automation.com/form-fields/")
#     driver.maximize_window()
#     time.sleep(5)
#     assert driver.title == "Form Fields | Practice Automation"



def test_smoke_3(init_driver):
    init_driver.get("https://practice-automation.com/form-fields/")
    time.sleep(5)
    assert init_driver.title == "Form Fields | Practice Automation"


def test_smoke_4(init_driver):
    init_driver.get("https://practice-automation.com/form-fields/")
    time.sleep(5)
    assert init_driver.title == "Form Fields | Practice Automation"


def test_smoke_5(init_driver):
    init_driver.get("https://practice-automation.com/form-fields/")
    time.sleep(5)
    assert init_driver.title == "Form Fields | Practice Automation"


#pytest -v -s