import time
import pytest
import allure

from pages.form_page import FormPage
from tools.loger import get_logger
import config

loger = get_logger("TEST_SCENARIO")

@pytest.mark.main
@pytest.mark.positive
@allure.title("Correct filling the application form")
@allure.description("Positive scenario. Application form")
@allure.tag("MAIN", "POSITIVE")
def test_scenario_positive_1(init_driver, init_data):
    dict_data = init_data

    init_driver.get(config.BASE_URL)

    loger.info("Start positive scenario with form filling")

    fp = FormPage(init_driver)

    fp.check_current_location()

    fp.set_name(dict_data["name_data"])
    fp.set_password(dict_data["pass_data"])
    fp.set_drink_1()
    fp.set_drink_2()

    #ffp.set_color()
    color = fp.get_color_set()
    init_driver.execute_script("arguments[0].click();", color)

    fp.set_automation(dict_data["automation"])
    fp.set_email(dict_data["email_data"])

    fp.list_parsing()
    fp.set_message()

    #ffp.click_submit()
    submit = fp.get_submit_bt()
    init_driver.execute_script("arguments[0].click();", submit)

    fp.check_submit_form()

    time.sleep(3)

    loger.info("Positive scenario with form filling is completed")


