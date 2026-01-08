import allure
import pytest

from config.environment import Environment
from pages.elle_footer_page import FooterEllePage
from tests.base_test import BaseTest


@allure.feature("Authentication")
@allure.story("User Login")
class TestCart(BaseTest):

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
        footer_link=FooterEllePage(self.driver)
        env = Environment("home")  # Uses ENV=demo by default if not set
        base_url = env.get_base_url()
        # username = env.get_username()
        # password = env.get_password()



        with allure.step("Navigate to login page"):
            footer_link.navigate_to(base_url)
            # The is_visible method is inherited from BasePage
            assert footer_link.is_visible(footer_link.Logo), "Login page did not load properly"
    #
        with allure.step("Perform login with valid credentials"):
            footer_link.footer_click()
