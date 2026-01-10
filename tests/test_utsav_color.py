import pytest
import allure
from time import sleep

from config.environment import Environment
from pages.utsav_login_page import UtsavLogin
from pages.utsav_product_list_page import UtsavProductList
from pages.utsav_product_page import UtsavProductPage
from pages.utsav_home_page import UtsavHomePage
from pages.utsav_cart_page import UtsavWishlist
from pages.utsav_checkout_page import UtsavCheckout

from tests.base_test import BaseTest
@pytest.mark.utsav
class TestUtsavSearch(BaseTest):

    @pytest.mark.sanity(allure.severity_level.MINOR)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_product3(self):
        homepage_utsav = UtsavHomePage(self.driver)
        productlist_utsav=UtsavProductList(self.driver)
        productpage_utsav=UtsavProductPage(self.driver)

        env = Environment('utsav')

        base_url = env.get_base_url()

        with allure.step("Navigate"):
            homepage_utsav.navigate_to(base_url)

        with allure.step("searching product"):
            homepage_utsav.search_product("saree")

        with allure.step("click"):
            homepage_utsav.click_search()

        with allure.step("select product color"):
            productlist_utsav.select_color()

        product_color_text = productlist_utsav.get_product_color()


        with allure.step("select product color"):
            productlist_utsav.get_product_name()

        product_name_text = productlist_utsav.get_product_name()

        assert product_color_text in product_name_text, "product color doesn't match"
        print("product color matched")
