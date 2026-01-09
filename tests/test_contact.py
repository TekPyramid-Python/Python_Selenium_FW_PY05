import allure
import pytest

from config.environment import Environment
from pages.contact_page import ContactPage
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








