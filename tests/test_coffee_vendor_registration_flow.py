# tests/test_coffee_vendor_registration_flow.py
import allure
import pytest

from config.environment import Environment

from pages.coffee_home_page import HomePage
from pages.coffee_vendor_page import VendorRegistrationPage
from tests.base_test import BaseTest


@allure.feature("Authentication")
@allure.story("Vendor Registration")
class TestVendorRegistration(BaseTest):
    """
    Test class for login functionality against total.coffee.com.
    """

    @allure.title("Test successful login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.coffee
    def test_coffee_vendor_registration(self):
        """
        Test Case: Verify successful login using credentials from config.yaml.
        """
        home_page = HomePage(self.driver)
        vendor_page = VendorRegistrationPage(self.driver)

        env = Environment('total_coffee')  # Uses ENV=demo by default if not set
        base_url = env.get_base_url()

        with allure.step("Navigate to login page"):
            home_page.navigate_to(base_url)
            # The is_visible method is inherited from BasePage
            assert home_page.is_visible(home_page.LOGO), "Login page did not load properly"

        with allure.step("Navigate to vendor Registration option"):
            assert home_page.scroll_to_element(home_page.VENDOR_REGISTRATION), "Vendor Registration did not displayed"

        with allure.step("Click vendor Vendor Button"):
            home_page.click_vendor_registration()
            #assert "Vendor Registration - Total.Coffee" in vendor_page.get_title

    # def test_select_state_from_dropdown(self):
    #     vendor_page = VendorRegistrationPage(self.driver)
    #     # Arrange
    #     registration_page = VendorRegistrationPage(self)
    #     registration_page.select_state("Karnataka")
    #     selected_state = registration_page.get_selected_state()
    #     assert selected_state == "Karnataka"

        with allure.step("Click vendor Registration option"):
            vendor_page.fill_vendor_registration()
            #assert 'Vendor Registration - Total.Coffee' in vendor_page.get_title

