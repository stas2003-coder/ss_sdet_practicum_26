import allure
import time
from selenium import webdriver
from selenium.common import NoAlertPresentException #for negative alert exception
from selenium.webdriver.chrome.service import Service   #for chrome webdriver fix problem with closing
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from tools.loger import get_logger

loger = get_logger("MAKE_STEP")

class FormPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    msg_data = []
    title = "Form Fields | Practice Automation"
    head = "Form Fields"
    success_msg = "Message received!"

    #Locators
    head_title = "[itemprop='headline']"  #ByCSS
    name_input = "name-input" #ByID
    password_input = "//input[@type='password']"
    email_input = "email" #ByID
    msg_input = "//textarea[@id='message']"
    drink_set1 = "//input[@id='drink2']"
    drink_set2 = "//input[@id='drink3']"
    color_set = "//input[@id='color3']"
    select1 = "//select[@id='automation']"
    submit_bt = ".custom_btn.btn_hover"  #ByCSS
    tools_mass = "//*[@id='feedbackForm']/ul/li"


    #Getters
    def get_head_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.head_title)))

    def get_name_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.name_input)))

    def get_password_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_input)))

    def get_email_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.email_input)))

    def get_msg_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.msg_input)))

    def get_drink_set1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.drink_set1)))

    def get_drink_set2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.drink_set2)))

    def get_color_set(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.color_set)))

    def get_select1(self):
        return Select(self.driver.find_element(By.XPATH, self.select1))

    def get_submit_bt(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.submit_bt)))

    def get_tools_mass(self):
        return self.driver.find_elements(By.XPATH, self.tools_mass)


    #Actions
    def set_name(self, name_data):
        with allure.step(f"enter name: '{name_data}'"):
            self.get_name_input().send_keys(name_data)
            time.sleep(1)
            loger.info(f"name {name_data} has entered")

    def set_password(self, pass_data):
        with allure.step(f"enter password: '{pass_data}'"):
            self.get_password_input().send_keys(pass_data)
            time.sleep(1)
            loger.info(f"password {pass_data} has entered")

    def set_drink_1(self):
        with allure.step("enter drink - Milk"):
            self.get_drink_set1().click()
            time.sleep(1)
            loger.info("Drink 'Milk' has been selected")

    def set_drink_2(self):
        with allure.step("enter drink - Coffee"):
            self.get_drink_set2().click()
            time.sleep(1)
            loger.info("Drink 'Coffee' has been selected")

    def set_color(self):
        with allure.step("set color - Yellow"):
            self.driver.execute_script("arguments[0].click();", self.color_set)
            time.sleep(1)
            loger.info("Color 'Yellow' has been selected")

    def set_automation(self, automation):
        with allure.step(f"Do you like automation? => '{automation}'"):
            self.get_select1().select_by_visible_text(automation)
            loger.info(f"automation variant: {automation} has entered")

    def set_email(self, email_data):
        with allure.step(f"enter email: '{email_data}'"):
            self.get_email_input().send_keys(email_data)
            time.sleep(1)
            loger.info(f"email {email_data} has entered")

    def set_message(self):
        with allure.step("enter parsing message"):
            self.get_msg_input().send_keys(self.msg_data[0])
            self.get_msg_input().send_keys('\n')
            self.get_msg_input().send_keys(self.msg_data[1])
            time.sleep(2)
            loger.info(f"message has entered")

    def click_submit(self):
        with allure.step("submit form"):
            self.driver.execute_script("arguments[0].click();", self.submit_bt)
            time.sleep(1)
            loger.info(f"form has been submitted")


    #Methods
    def check_current_location(self):
        with allure.step(f"Check current location: {self.title}"):
            assert self.driver.title == self.title, "Title of page is not correct"
            loger.info(f"Title: {self.driver.title} is correct")

            assert self.get_head_title().text == self.head, "Head of page is not correct"
            loger.info("We are located into right page!")


    def check_submit_form(self):
        with allure.step("Check alert pop up"):
            result_text = self.driver.switch_to.alert.text
            loger.info(f"Result text: {result_text}")
            time.sleep(2)
            assert result_text == self.success_msg, "Message of success form submitting is not correct"
            self.driver.switch_to.alert.accept()
            time.sleep(1)


    def list_parsing(self):
        with allure.step("Parsing information with automation tools"):
            tool_mass = self.get_tools_mass()
            temp_mass = []
            result_list = []
            result_1 = f"Automation tool list has {len(tool_mass)} instruments"
            result_2 = ""
            loger.info(result_1)
            for tool in tool_mass:
                loger.info(f"Tool: {tool.text} has next namelength: {len(tool.text)}")
                temp_mass.append(len(tool.text))

            temp_mass = sorted(temp_mass, reverse=True)
            for tool in tool_mass:
                if len(tool.text) == temp_mass[0]:
                    result_2 = f"Tool: {tool.text} has the most quantity of symbols: {len(tool.text)}"
                    loger.info(result_2)

            result_list.append(result_1)
            result_list.append(result_2)
            self.msg_data = result_list
            return  result_list


    def except_for_negative(self):
        with allure.step("Check error exception"):
            elem = self.driver.switch_to.active_element
            assert elem == self.get_name_input(), "Warning message is not correct"
            loger.info("Field 'Name' is not filled out")
            loger.info("Negative scenario is proceed")

