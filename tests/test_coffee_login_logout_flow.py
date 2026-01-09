# tests/test_login.py
import allure
import pytest

from config.environment import Environment
from pages.coffee_MyAccount_page import MyAccount
from pages.coffee_home_page import HomePage
from tests.base_test import BaseTest


@allure.feature("Authentication")
@allure.story("User Login")
class TestLogin(BaseTest):
    """
    Test class for login functionality against total.coffee.com.
    """

    @allure.title("Test successful login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.coffee
    def test_successful_login(self):
        """
        Test Case: Verify successful login using credentials from config.yaml.
        """
        # --- Initialize pages and variables ---
        home_page = HomePage(self.driver)
        my_account = MyAccount(self.driver)
        env = Environment('total_coffee')  # Uses ENV=demo by default if not set
        base_url = env.get_base_url()
        username = env.get_username()
        password = env.get_password()

        with allure.step("Navigate to login page"):
            home_page.navigate_to(base_url)
            # The is_visible method is inherited from BasePage
            assert home_page.is_visible(home_page.LOGO), "Login page did not load properly"

        with allure.step("Perform login with valid credentials"):
            home_page.login(username, password)

        with allure.step("Verify successful login and page title"):
            assert my_account.is_login_successful(), "Login step failed before the intended assertion."

            expected_title = "My account - Total.Coffee"  # This is the correct title for My account page
            actual_title = my_account.get_title()  # This method is inherited from BasePage
            assert expected_title == actual_title, f"Expected title '{expected_title}', but got '{actual_title}'"

        with allure.step("Perform login with valid credentials"):
            my_account.logout()