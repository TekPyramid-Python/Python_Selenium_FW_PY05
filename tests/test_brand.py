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

class TestBrand(BaseTest):
    @pytest.mark.smoke
    @pytest.mark.dental
    def test_change_profile_name(self,log_in_and_out):
        home_page = HomePage(self.driver)
        search_page=Search(self.driver)
        product_page=Product(self.driver)
        cart=Cart(self.driver)
        profile=ProfilePage(self.driver)
        wishlist=WishListPage(self.driver)
        with allure.step("removing all the products from cart"):
            home_page.click_cart()
            cart.remove_all_items_from_cart()
            cart.click_home_page()

        with allure.step("selecting a product based on brand"):
            home_page.brand_selection()
            product_page.add_product()

        with allure.step("entering feedback"):
            product_page.enter_feedback("iron",250,"good")
            self.driver.refresh()
            product_page.click_profile()


        with allure.step("changing profile name"):
            profile.full_name_change("suraj")
            cart.click_home_page()