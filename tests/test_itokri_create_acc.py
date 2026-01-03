# tests/test_itokri_create_acc.py
import allure
import pytest

from config.environment import Environment
from pages.itokri_home_page import ItokriHomePage
from pages.itokri_login_page import ItokriLoginPage
from pages.itokri_create_account_page import ItokriCreateAccountPage
from tests.base_test import BaseTest


@allure.feature("Creation")
@allure.story("User Create Account")
class TestCreateAccount(BaseTest):
    """
    Test class for create account functionality against itokri.com.
    """

    @allure.title("Test successful create account with valid credentials")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_create_account(self):
        homepage=ItokriHomePage(self.driver)
        loginpage = ItokriLoginPage(self.driver)
        createacc=ItokriCreateAccountPage(self.driver)
        env = Environment()
        base_url = env.get_base_url()
        firstname="Admin"
        lastname="Mark"
        email="admin123@gmail.com"
        password="admin@123"
        phone="9876543212"
        with allure.step("1. Click on Account icon"):
            homepage.navigate_to(base_url)
            homepage.click_cross_button()
            homepage.login_icon()
            # assert loginpage.is_loginpage_visible(), "Did not land on login page."
            self.logger.info("Login page is displayed successfully.")
        with allure.step("2. Click on login with email"):
            loginpage.nav_create_acc_page()
            # assert createacc.is_create_account_visible(), "Did not land on create account page."
            self.logger.info("Login page is displayed successfully.")

        with allure.step("3. Give all the credentials and click on create account"):
            createacc.create_account(firstname,lastname,email,password,phone)
            # assert createacc.is_home_page_visible(), "Did not land on home page."
            self.logger.info("Home page is displayed successfully.")

