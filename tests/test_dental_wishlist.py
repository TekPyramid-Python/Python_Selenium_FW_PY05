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

class  TestWishList(BaseTest):
    @pytest.mark.dental
    def test_wishlist_page(self,log_in_and_out):
         home_page=HomePage(self.driver)
         search_page=Search(self.driver)
         product_page=Product(self.driver)
         cart=Cart(self.driver)
         wishlist=WishListPage(self.driver)

         with allure.step("removing all the products from cart"):
             home_page.click_cart()
             cart.remove_all_items_from_cart()
             cart.click_home_page()

         with allure.step("Cleaning wishlist before test"):
             sleep(3)
             home_page.open_wishlist()

             wishlist.remove_all_items_if_present()
             wishlist.click_home_button()


         with allure.step("clicking the search box"):
             home_page.click_search()
             sleep(3)
             search_page.enter_item("knife")
             sleep(3)

         with allure.step("adding product and going to cart"):
            if product_page.is_add_present():
                product_page.add_product()
                product_page.click_cart()
                sleep(3)
            else:
                product_page.click_cart()
                sleep(3)

         with allure.step("removing the product"):
            cart.add_product_to_wishlist()
            cart.clicking_wishlist()
            wishlist.click_home_button()












