import pytest
import allure
from tests.test_login_and_logout import log_in_and_out
from pages.dental_wishlist_page import WishListPage
from pages.dental_kart_profile import ProfilePage
from pages.dental_home_page import HomePage
from pages.dental_kart_search_page import Search
from pages.dental_kart_product_page import Product
from pages.dental_cart import Cart
from tests.base_test import BaseTest
from time import sleep

class TestSort(BaseTest):
    @pytest.mark.dental
    def test_sorting_of_products(self,log_in_and_out):
        home_page = HomePage(self.driver)
        search_page=Search(self.driver)
        product_page=Product(self.driver)

        with allure.step("sorting the products"):
            home_page.click_best_seller()
            sleep(4)

        with allure.step("Verifying products are sorted high to low"):
            actual_prices = product_page.get_all_product_prices()
            expected_prices = sorted(actual_prices, reverse=True)

            assert actual_prices == expected_prices,f"Sorting failed. Actual: {actual_prices}"
            print(f"sorting passed.{actual_prices}")