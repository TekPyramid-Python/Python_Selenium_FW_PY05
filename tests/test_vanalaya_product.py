

import allure
import pytest

from config.environment import Environment
from pages.vanalaya_product_page import ProductPage
from tests.base_test import BaseTest


# @allure.feature("Authentication")
# @allure.story("User Login")
class TestVanalayaBlog(BaseTest):
    """
    Test class for login functionality against saucedemo.com.
    """

    @allure.title("Test successful login with valid credentials")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_product_add_to_cart(self):
        """
        Test Case: Verify successful login using credentials from config.yaml.
        """
        # --- Initialize pages and variables ---
        product_page = ProductPage(self.driver)
        env = Environment("test")  # Uses ENV=demo by default if not set
        base_url = env.get_base_url()
        # username = env.get_username()


        with allure.step("Navigate to Blog page"):
            product_page.navigate_to(base_url)
            # The is_visible method is inherited from BasePage
            assert product_page.is_visible(product_page.CLICK_CART), "Blog page did not load properly"

        with allure.step("Clicking Cart button"):
            product_page.click_cart_button()
            # assert product_page.is_visible(product_page.),"Blog Button is visible or not"

        with allure.step("Click Product Image"):
            product_page.click_product_button()
            # assert product_page.is_visible(product_page.LOGO),"Blog Button is not visible"

        with allure.step("Scroll to Add to Cart page"):
            product_page.scroll_to_add_to_cart_button()

        with allure.step("Click add to cart button"):
            product_page.click_add_to_cart_button()
            # assert product_page.is_visible(product_page.SCROLL_DOWN,20),"Not scrolling down properly"

        with allure.step("Click checkout button"):
            product_page.click_checkout_button()
            # assert product_page.is_visible(product_page.ENTER_EMAIL_ID),"Email Id is not visible"



        # with allure.step("Verify Payment Page"):
            # assert product_page.is_payment_page_open_successful(), "Payment page not opened"

            # expected_title = '5 Everyday Organic Swaps That Can Transform Your Health Naturally – Vanalaya'# This is the correct title for saucedemo
            # actual_title = product_page.get_title()  # This method is inherited from BasePage
            # assert expected_title == actual_title, f"Expected title '{expected_title}', but got '{actual_title}'"

