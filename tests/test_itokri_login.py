# tests/test_itokri_login.py
from time import sleep

import allure
import pytest

from config.environment import Environment
from pages.itokri_home_page import ItokriHomePage
from pages.itokri_login_page import ItokriLoginPage
from tests.base_test import BaseTest


@allure.feature("Login")
@allure.story("User Login With valid login credential")
class TestLogin(BaseTest):
    """
    Test class for create account functionality against itokri.com.
    """

    @allure.title("Test successful login with valid credentials")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_login_account(self):
        homepage=ItokriHomePage(self.driver)
        loginpage = ItokriLoginPage(self.driver)
        env = Environment("itokri")
        base_url = env.get_base_url()
        email=env.get_username()
        password=env.get_password()
        with allure.step("1. Click on Account icon"):
            homepage.navigate_to(base_url)
            try:
                homepage.click_cross_button()
            except:
                print("cross button not came")
            self.logger.info("Home page is displayed successfully.")
            homepage.login_icon()
        with allure.step("2. Click on login with email and enter valid email and password"):
            loginpage.login(email,password)
            # assert homepage.is_home_page_visible(), "Home page not visible"
            # self.logger.info("Login page is displayed successfully and entered email and password")

    # def test_logout(self):



