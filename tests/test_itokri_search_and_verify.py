# tests/test_itokri_product_verify.py
from time import sleep

import allure
import pytest

from config.environment import Environment
from pages.itokri_home_page import ItokriHomePage
from pages.itokri_searched_product_page import ItokriSearchedProductPage
from tests.base_test import BaseTest


@allure.feature("Browse Sarees")
@allure.story("Browse Sarees by Craft Type")
class TestItokriProduct(BaseTest):
    """
    Test class for create account functionality against itokri.com.
    """

    @allure.title("Test successful login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.itokri
    @pytest.mark.parametrize("product_name",["Ikat Silk Saree","Chikankari saree"])
    def test_product_verify(self,product_name):
        homepage=ItokriHomePage(self.driver)
        searched_product_page=ItokriSearchedProductPage(self.driver)
        env = Environment()
        base_url = env.get_base_url()
        email=env.get_username()
        password=env.get_password()
        first_name=product_name.split()[0]
        with allure.step("1. Open homepage"):
            homepage.navigate_to(base_url)
            try:
                homepage.click_cross_button()
            except:
                print("cross button not came")
            self.logger.info("Home page is displayed successfully.")

        with allure.step("2. Searching product with search bar"):
            homepage.search_product(product_name)
            self.logger.info(f"{product_name} page is displayed successfully")

        with allure.step("3. Check the loaded saree matches with searched product or not:"):
            assert first_name in searched_product_page.get_first_product_name(), "Product is not matched with searched product"
            self.logger.info(f"Product is same as {product_name}")

        with allure.step("4. Check the total number of item is >=10 or not "):
            assert 10 <= searched_product_page.get_total_count(), "Product is less than 10"
            self.logger.info("Searched product count is >=10")


