import allure
import pytest
from selenium.common import NoAlertPresentException #for negative alert exception

from pages.form_page import FormPage
from tools.loger import get_logger
import config

loger = get_logger("TEST_SCENARIO")


@pytest.mark.main
@pytest.mark.negative
@allure.title("Incorrect filling the application form")
@allure.description("Negative scenario. Application form")
@allure.tag("MAIN", "NEGATIVE")
def test_scenario_negative_1(init_driver, init_data):
    dict_data = init_data

    init_driver.get(config.BASE_URL)

    loger.info("Start negative scenario with form filling")

    fp = FormPage(init_driver)

    try:
        fp.check_current_location()

        #ffp.set_name()
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

    except NoAlertPresentException as exception:
        fp.except_for_negative()

    loger.info("Negative scenario with form filling is completed")
