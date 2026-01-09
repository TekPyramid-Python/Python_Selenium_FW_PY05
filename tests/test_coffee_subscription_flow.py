# tests/test_coffee_subscription_flow.py
import allure
import pytest

from config.environment import Environment
from pages.coffee_subscription_page import SubscriptionPage
from tests.base_test import BaseTest
from pages.coffee_home_page import HomePage


@allure.feature("Authentication")
@allure.story("Coffee Subscription")
class TestSubscriptionFlow(BaseTest):
    """
    Test class for login functionality against total.coffee.com.
    """

    @allure.title("Test successful to Subscribe the Coffee")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.coffee
    def test_select_subscription_options(self):
        sub_page = SubscriptionPage(self.driver)
        home_page = HomePage(self.driver)

        env = Environment('total_coffee')  # Uses ENV=demo by default if not set
        base_url = env.get_base_url()

        with allure.step("Navigate to login page"):
            home_page.navigate_to(base_url)
            # The is_visible method is inherited from BasePage
            assert home_page.is_visible(home_page.COFFEE_SUBSCRIPTION), "Login page did not load properly"

        with allure.step("Click vendor Vendor Button"):
            home_page.click_coffee_subscription()

        with allure.step("Click COFFEE_SUBSCRIPTION Button"):
            sub_page.coffee_preparation()
            EXPECTED_TITLE="Cart - Total.Coffee"
            ACTUAL_TITLE = sub_page.get_title()
            assert EXPECTED_TITLE==ACTUAL_TITLE,"succesfully added to cart"

