import pytest
import allure
from tests.base_test import BaseTest
from pages.dental_home_page import HomePage
from pages.dental_kart_search_page import Search
from pages.dental_kart_product_page import Product
from pages.dental_cart import Cart
from time import sleep

@allure.feature("Authentication")
@allure.story("User Login")
class TestHomePage(BaseTest):
    @allure.title("Test successful login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.dental
    def test_successful_login(self,log_in_and_out):

        home_page = HomePage(self.driver)
        search_page=Search(self.driver)
        product_page=Product(self.driver)
        cart=Cart(self.driver)


        with allure.step("clicking the search box"):
            home_page.click_search()

        with allure.step("entering the data"):
            sleep(3)
            search_page.enter_item("implant")



        with allure.step("adding product and going to cart"):
            if product_page.is_add_present():
                product_page.add_product()
                product_page.click_cart()
            else:
                product_page.click_cart()

        with allure.step("going to homepage"):
            cart.click_home_page()











