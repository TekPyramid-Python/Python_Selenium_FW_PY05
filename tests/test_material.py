import allure
import pytest

from config.environment import Environment
from pages.material import MaterialFilter
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
        click_material=MaterialFilter(self.driver)
        env = Environment("home")  # Uses ENV=demo by default if not set
        base_url = env.get_base_url()
        # username = env.get_username()
        # password = env.get_password()

        with allure.step("Navigate to home page"):
            click_material.navigate_to(base_url)

        with allure.step("click on material"):
            click_material.hover(click_material.slider)








