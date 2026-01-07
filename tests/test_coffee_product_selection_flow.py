# tests/test_coffee_product_selection_flow.py
import allure
import pytest

from config.environment import Environment

from pages.coffee_MyAccount_page import MyAccount
from pages.coffee_home_page import HomePage
from pages.coffee_productlist_page import ProductListPage
from pages.coffee_product_page import ProductPage
from tests.base_test import BaseTest
from pages.coffee_cart_page import CoffeeCartPage
from pages.coffee_checkout_page import CheckoutPage


@allure.feature("Authentication")
@allure.story("Product selection flow")
class TestCoffeeProductSelectionFlow(BaseTest):
    """
    Test class for login functionality against total.coffee.com.
    """

    @allure.title("Test successful product selection with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.coffee
    def test_search_product(self):
        """
        Test Case: Verify successful login using credentials from config.yaml.
        """
        # --- Initialize pages and variables ---
        my_account = MyAccount(self.driver)
        home_page = HomePage(self.driver)
        productlist_page = ProductListPage(self.driver)
        product_page = ProductPage(self.driver)
        cart_page = CoffeeCartPage(self.driver)
        checkout_page =CheckoutPage(self.driver)
        env = Environment('total_coffee')  # Uses ENV=demo by default if not set
        base_url = env.get_base_url()
        username = env.get_username()
        password = env.get_password()
        product = "coffee bag"

        with allure.step("Navigate to login page"):
            home_page.navigate_to(base_url)
            # The is_visible method is inherited from BasePage
            assert home_page.is_visible(home_page.LOGO), "Login page did not load properly"

        with allure.step("Perform login with valid credentials"):
            home_page.login(username, password)

        with allure.step("Verify successful login and page title"):
            assert my_account.is_login_successful(), "Login step failed before the intended assertion."

        with allure.step("Verify successful product search"):
            assert home_page.click_search(), "Search Icon failed to click"

        with allure.step("Searching the expected product"):
            assert home_page.search_product(product), "Expected product failed to search"

        # with allure.step("validating the searched product listings"):
        #     assert home_page.validate_searched_product_listed(product), "Expected product failed to display"

        with allure.step("Searching the expected product"):
            assert productlist_page.click_searched_product(), "Expected product failed to click"

        with allure.step("Selecting the size and Clicking the add to basket button and Clicking the View basket"):
            assert product_page.add_to_basket(), "Add to basket failed to click"

        with allure.step("Clicking the Proceed to checkout"):
            assert cart_page.proceed_to_checkout(), "Proceed to checkout failed to click"

        with allure.step("Filling the billing details"):
             checkout_page.billing_details()
             expected_title="Checkout - Total.Coffee"
             actual_title= checkout_page.get_title()
             assert expected_title == actual_title