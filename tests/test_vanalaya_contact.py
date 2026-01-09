# tests/test_login.py
import allure
import pytest

from config.environment import Environment
from pages.vanalaya_contact_page import ContactPage
from tests.base_test import BaseTest


# @allure.feature("Authentication")
# @allure.story("User Login")
class TestContact(BaseTest):
    """
    Test class for login functionality against saucedemo.com.
    """

    @allure.title("Test successful login with valid credentials")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_enter_contact_successful(self):
        """
        Test Case: Verify successful login using credentials from config.yaml.
        """
        # --- Initialize pages and variables ---
        contact_page = ContactPage(self.driver)
        env = Environment("test")  # Uses ENV=demo by default if not set
        base_url = env.get_base_url()
        username = env.get_username()


        with allure.step("Navigate to Blog page"):
            contact_page.navigate_to(base_url)
            # The is_visible method is inherited from BasePage
            assert contact_page.is_visible(contact_page.CONTACT_TITLE), "Contact page did not load properly"

        with allure.step("click_contact_button"):
            contact_page.click_contact_button()
            assert contact_page.is_visible(contact_page.CONTACT_CLICK),"Contact Button is not clicking"

        with allure.step("Enter all details"):
            contact_page.enter_details('Prathesh','abcd@gmail.com','987654321','testing','Iam a tester')
            assert contact_page.is_visible(contact_page.ENTER_NAME),"Enter name input field is not visible"

        with allure.step("Scroll to element"):
            contact_page.scroll_to_submit()
            assert contact_page.is_visible(contact_page.SCROLL_TO_SUBMIT),"Not scrolling towards the element"

        with allure.step("click to submit"):
            contact_page.click_submit()
            assert contact_page.is_visible(contact_page.CLICK_SUBMIT),"Click submit button is not displayed"

        with allure.step("Verify successful blog and page title"):
            assert contact_page.is_query_successful(), "Subscribe was not successful, inventory page not found."

            expected_title = "Contact – Vanalaya"  # This is the correct title for saucedemo
            actual_title = contact_page.get_title()  # This method is inherited from BasePage
            assert expected_title == actual_title, f"Expected title '{expected_title}', but got '{actual_title}'"

