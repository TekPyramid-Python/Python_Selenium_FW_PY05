# tests/test_login.py
import allure
import pytest

from config.environment import Environment
from pages.contact_us_page import ContactUsPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from tests.base_test import BaseTest


@allure.feature("Authentication")
@allure.story("User Login")
class TestLogin(BaseTest):
    """
    Test class for login functionality against saucedemo.com.
    """

    @allure.title("Test successful login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_successful_login(self):
        """
        Test Case: Verify successful login using credentials from config.yaml.
        """
        # --- Initialize pages and variables ---
        contact_page = ContactUsPage(self.driver)
        env = Environment()  # Uses ENV=demo by default if not set
        base_url = env.get_base_url()
        username = env.get_username()
        password = env.get_password()

        with allure.step("Navigate to contact us page"):
            contact_page.navigate_to(base_url)
            # The is_visible method is inherited from BasePage
            assert contact_page.is_visible(contact_page.FIRST_NAME_INPUT), "contact page did not load properly"

        with allure.step("Perform login with valid credentials"):
            contact_page.FIRST_NAME_INPUT()

        with allure.step("Verify successful contact_us_page and page title"):
            assert contact_page.is_contact_us_page_successful(), "contact us page was not successful, inventory page not found."

            expected_title = "Swag Labs"  # This is the correct title for saucedemo
            actual_title = contact_page.get_title()  # This method is inherited from BasePage
            assert expected_title == actual_title, f"Expected title '{expected_title}', but got '{actual_title}'"

    @allure.title("Test login failure with invalid credentials")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression  # <-- This is a detailed case, so it's regression
    def test_invalid_login(self):
        """
        Test Case: Verify login failure with deliberately incorrect credentials.
        """
        contact_page = ContactUsPage(self.driver)
        env = Environment()
        base_url = env.get_base_url()

        with allure.step("Navigate to login page"):
            contact_page.navigate_to(base_url)
            assert contact_page.is_visible(contact_page.EMAIL_INPUT), "Login page did not load properly"

        with allure.step("Attempt login with invalid credentials"):
             contact_page.FIRST_NAME_INPUT("invalid_user", "invalid_password")

        with allure.step("Verify error message is displayed and correct"):
            error_message = contact_page.get_error_message()
            expected_error_text = "Username and password do not match"  # Specific error from saucedemo

            assert expected_error_text in error_message, f"Incorrect error message. Expected to see '{expected_error_text}'"
            assert not contact_page.is_login_successful(), "User should not be logged in with invalid credentials"

    # Add this new test method inside the TestLogin class in tests/test_login.py

    @allure.title("Test login page to verify screenshot on failure")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.framework_check  # We can mark this as a framework check
    def test_login_failure_for_screenshot(self):
        """
        This test purposefully fails after a successful login to verify
        that the screenshot-on-failure mechanism is working correctly.
        """
        contact_page= ContactUsPage(self.driver)
        env = Environment()
        base_url = env.get_base_url()

        with allure.step("Navigate and perform a successful login"):
            contact_page.navigate_to(base_url)
            username = env.get_username()
            password = env.get_password()
            contact_page.FIRST_NAME_INPUT(username, password)
            assert contact_page.is_Contact_successful(), "Login step failed before the intended assertion."

        with allure.step("Intentionally fail the test with a bad assertion"):
            self.logger.info("Now asserting for an incorrect title to trigger a failure.")

            expected_title = "An Incorrect Title"  # This is wrong on purpose
            actual_title = contact_page.get_title()

            assert expected_title == actual_title, "This assertion is designed to fail to test screenshot capture."