# tests/test_login.py
import allure
import pytest

from config.environment import Environment
from pages.himadri_login_page import HimadriLoginPage
from tests.base_test import BaseTest


@allure.feature("Authentication")
@allure.story("User Login")
class TestLogin(BaseTest):

    @allure.title("Test successful login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_successful_login(self):
        login_page = HimadriLoginPage(self.driver)
        env = Environment("himadri")
        base_url = env.get_base_url()
        email = env.get_email()
        password = env.get_password()

        with allure.step("Navigate to login page"):
            login_page.navigate_to(base_url)
            assert login_page.is_visible(login_page.LOGIN_CLICK), "Login page did not load properly"

        with allure.step("Perform login with valid credentials"):
            login_page.login(email, password)

        with allure.step("Verify successful login and page title"):
            assert login_page.is_login_successful(), "Login was not successful, Account page not found."

            expected_url = "https://himadrigardens.com/my-account/"
            actual_url = login_page.get_current_page_url()
            assert expected_url == actual_url, f"Expected url '{expected_url}', but got '{actual_url}'"

    @allure.title("Test login failure with invalid credentials")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression  # <-- This is a detailed case, so it's regression
    def test_invalid_login(self):
        """
        Test Case: Verify login failure with deliberately incorrect credentials.
        """
        login_page = HimadriLoginPage(self.driver)
        env = Environment()
        base_url = env.get_base_url()

        with allure.step("Navigate to login page"):
            login_page.navigate_to(base_url)
            assert login_page.is_visible(login_page.LOGIN_CLICK), "Login page did not load properly"

        with allure.step("Attempt login with invalid credentials"):
            login_page.login("arsha@gmail.com", "invalid_password")

        with allure.step("Verify error message is displayed and correct"):
            error_message = login_page.get_error_message()
            expected_error_text = f"Unknown email address. Check again or try your username."

            assert expected_error_text in error_message, f"Incorrect error message. Expected to see '{expected_error_text}'"
            assert not login_page.is_login_successful(), "User should not be logged in with invalid credentials"