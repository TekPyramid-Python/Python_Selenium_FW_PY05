import allure
import pytest

from config.environment import Environment
from pages.himadri_cart_page import HimadriCartPage
from pages.validation_shop_all_page import ShopAll_Validation
from tests.base_test import BaseTest
from pages.himadri_login_page import HimadriLoginPage
from pages.himadri_filter_conditions import HimadriProductPage

class TestHimadriCartPage(BaseTest):
    def test_successful_login(self):
        login_page = HimadriLoginPage(self.driver)
        shopall_valid = ShopAll_Validation(self.driver)
        cart_page = HimadriCartPage(self.driver)
        product_page = HimadriProductPage(self.driver)
        env = Environment()
        base_url = env.get_base_url()
        email = env.get_email()
        password = env.get_password()

        with allure.step("Navigate to login page"):
            login_page.navigate_to(base_url)
            assert login_page.is_visible(login_page.LOGIN_CLICK), "Login page did not load properly"

        with allure.step("Perform login with valid credentials"):
            login_page.login(email, password)

        with allure.step('click on the shop all button on the account page'):
            shopall_valid.click_shopall()

        with allure.step("Checking Click on Shop All is successful"):
            shopall_valid.is_clickon_shopall_successful()

        with allure.step("Click on Aquarium Accessories"):
            cart_page.click_on_aquarium_accessories()

        with allure.step("Sort products by price low to high"):
            product_page.sort_by_price_low_to_high()

        with allure.step("Fetch first two product prices"):
            first_price = product_page.get_first_product_price()
            second_price = product_page.get_second_product_price()

        with allure.step("Verify products are sorted correctly"):
            assert first_price <= second_price, \
                f"Sorting failed! First: {first_price}, Second: {second_price}"