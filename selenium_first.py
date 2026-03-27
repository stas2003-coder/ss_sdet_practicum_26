import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService

with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as browser:
    browser.get("https://stepik.org/course/104774")
    time.sleep(5)