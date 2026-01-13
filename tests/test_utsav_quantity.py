import pytest
import allure

from tests.base_test import BaseTest
from config.environment import Environment
from pages.utsav_home_page import UtsavHomePage
from pages.utsav_product_list_page import UtsavProductList
from pages.utsav_product_page import UtsavProductPage
from pages.utsav_cart_page import UtsavWishlist
from pages.utsav_checkout_page import UtsavCheckout

@pytest.mark.utsav
class TestUtsavQuantity(BaseTest):

    @pytest.mark.sanity(allure.severity_level.MINOR)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_product4(self):
        homepage_utsav = UtsavHomePage(self.driver)
        productlist_utsav = UtsavProductList(self.driver)
        productpage_utsav = UtsavProductPage(self.driver)
        wishList_utsav = UtsavWishlist(self.driver)
        checkout_utsav = UtsavCheckout(self.driver)

        env = Environment('utsav')

        base_url = env.get_base_url()

        with allure.step("Navigate"):
            homepage_utsav.navigate_to(base_url)

        with allure.step("mouse hover"):
            homepage_utsav.mouse_hover_men()

        with allure.step("click subcategory"):
            homepage_utsav.click_on_subcategory()

        with allure.step("click kurta_name"):
            homepage_utsav.click_on_kurta_name()

        with allure.step("click on size"):
            productlist_utsav.click_on_size()

        with allure.step("click on add to bag"):
            productpage_utsav.add_to_shopping_bag()

        # with allure.step("click on view bag"):
        #     wishList_utsav.click_on_continue_shopping()
        #
        # with allure.step("mouse hover jewellery"):
        #     homepage_utsav.mouse_hover_jewellery()
        #
        # with allure.step("click on rings"):
        #     homepage_utsav.click_on_rings()
        #
        # with allure.step("click on ring_name"):
        #     homepage_utsav.click_on_ring_name()
        #
        # with allure.step("click on add to bag"):
        #     productpage_utsav.add_to_shopping_bag()

        # with allure.step("view bag"):
        #     wishList_utsav.click_on_view_page()

        total_price = checkout_utsav.get_total_price()
        print(total_price)









