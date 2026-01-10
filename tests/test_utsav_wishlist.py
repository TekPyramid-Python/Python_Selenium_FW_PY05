import pytest
import allure
from time import sleep

from config.environment import Environment
from pages.utsav_login_page import UtsavLogin
from pages.utsav_product_list_page import UtsavProductList
from pages.utsav_product_page import UtsavProductPage
from pages.utsav_home_page import UtsavHomePage
from pages.utsav_wishlist_page import UtsavWishlistPage

from tests.base_test import BaseTest
@pytest.mark.utsav
class TestUtsavWishlist(BaseTest):

    @pytest.mark.sanity(allure.severity_level.MINOR)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_product6(self):
        homepage_utsav = UtsavHomePage(self.driver)
        productlist_utsav=UtsavProductList(self.driver)
        productpage_utsav=UtsavProductPage(self.driver)
        wishlistpage_utsav=UtsavWishlistPage(self.driver)

        env = Environment('utsav')

        base_url = env.get_base_url()

        with allure.step("Navigate"):
            homepage_utsav.navigate_to(base_url)

        with allure.step("searching product"):
            homepage_utsav.search_product("saree")

        with allure.step("click"):
            homepage_utsav.click_search()

        with allure.step('add to wishlist'):
            productlist_utsav.add_to_wishlist()

        product_text1=productlist_utsav.get_product_name()

        sleep(2)
        with allure.step('click wishlist'):
            homepage_utsav.click_wishlist()

        product_text2=wishlistpage_utsav.get_wishlist_product_name()

        assert product_text1 in product_text2,"product doesn't match"
        print("product matched")
