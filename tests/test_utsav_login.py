import pytest
import allure

from config.environment import Environment
from pages.utsav_login_page import UtsavLogin
from pages.utsav_home_page import UtsavHomePage
from tests.base_test import BaseTest
@pytest.mark.utsav
class TestLoginUtsav(BaseTest):
    @pytest.mark.sanity(allure.severity_level.MINOR)
    @allure.title("Test successful login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)

    def test_successful_login1(self):
        login_utsav = UtsavLogin(self.driver)
        homepage_utsav=UtsavHomePage(self.driver)

        env = Environment('utsav')

        base_url = env.get_base_url()
        username = env.get_username()
        password = env.get_password()

        with allure.step("Navigate and perform a successful login"):
            login_utsav.navigate_to(base_url)
            assert homepage_utsav.is_visible(homepage_utsav.UTSAV_ICON)

        with allure.step('Mouse hover'):
            login_utsav.mouse_hover_to_account()

        with allure.step("Navigate to login page"):
             login_utsav.click_on_login()
             assert login_utsav.is_visible(login_utsav.EMAIL_TEXT)

        with allure.step("giving credentials"):
            login_utsav.login( username, password)
            # login_utsav.login("safira123", "12345")

        user_text1=login_utsav.get_email_text()

        with allure.step('Mouse hover'):
            login_utsav.mouse_hover_to_account()

        with allure.step('click on account'):
            login_utsav.click_on_account_dashboard()

        content_box=login_utsav.get_box_content()

        assert user_text1 in content_box,"email doesn't match"
        print("EMAIL matched")





