from time import sleep

import allure
import pytest

from .furniture_page import Furniture_Module
from ..config.environment import Environment
from ..pages.base_page import BasePage

LOGIN_BUTTON = ("css selector", "button.rm-login__btn")
PHONE_FIELD = ("css selector", "div.rm-auth__user-input>div>input")
CONTINUE_BTN = ("css selector", "form.rm-auth__form>div:nth-child(2)>button")
PROFILE_ICON = ("css selector", "a.rm-user__fullName")
LOGOUT_BTN = ("css selector", "ul.nav-arrow.rm-user__loggedIn>li:nth-child(4)")


@pytest.fixture(scope="function")
def rentomojo_login(request):
    driver=request.cls.driver
    base=BasePage(driver)
    with allure.step("Navigating to website"):
            env = Environment('rent')
            base_url = env.get_base_url()
            base.navigate_to(base_url)
    with allure.step("Navigate and perform a successful login"):
        try:
            base.click(LOGIN_BUTTON)
            base.send_keys(PHONE_FIELD, 8431926335)
            base.click(CONTINUE_BTN)
            base.wait_till_pageload()
            sleep(15)
            base.click(CONTINUE_BTN)

        except Exception as e:
            base.logger.info("userr already logined")

    yield

    with allure.step("Navigate and perform a successful logout"):
        try:
            base.hover_over_element(PROFILE_ICON)
            sleep(5)
            base.click(LOGOUT_BTN)
            sleep(15)
        except Exception as e:
            base.logger.info("user not logged in")