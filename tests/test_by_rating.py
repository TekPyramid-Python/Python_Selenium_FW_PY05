import pytest
import allure

from pages.dental_wishlist_page import WishListPage
from pages.dental_kart_profile import ProfilePage
from pages.dental_home_page import HomePage
from pages.dental_kart_search_page import Search
from pages.dental_kart_product_page import Product
from pages.dental_cart import Cart
from tests.base_test import BaseTest
from time import sleep
1

class TestByRating(BaseTest):
    @pytest.mark.dental
    def test_selection_by_rating(self,log_in_and_out):
        home_page = HomePage(self.driver)
        search_page = Search(self.driver)
        product_page = Product(self.driver)
        cart = Cart(self.driver)
        wishlist = WishListPage(self.driver)

        with allure.step("removing all the products from cart"):
            home_page.click_cart()

            cart.remove_all_items_from_cart()
            cart.click_home_page()

        with allure.step("finding the product based on rating"):
            home_page.selection_by_category()

        with allure.step("adding product to cart"):
            product_page.add_product()
            sleep(3)
            product_page.click_cart()
            sleep(3)