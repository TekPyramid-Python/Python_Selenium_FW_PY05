from ..pages.base_page import BasePage
from ..pages.furniture_page import Furniture_Module
from ..tests.base_test import BaseTest
from ..pages.rentomojo_wishlist import Rentomojo_Wishlist
import pytest
from ..config.environment import Environment
import allure



class TestWishlist(BaseTest):
    @pytest.mark.usefixtures("rentomojo_login")
    @pytest.mark.rentomojo
    def test_wishlist(self):
        rent = Rentomojo_Wishlist(self.driver)
        furniture = Furniture_Module(self.driver)
        with allure.step("Navigating to website"):
            furniture.navigate_to_website()
            base=BasePage(self.driver)
            base.wait_till_pageload()

        with allure.step("clearing wishlist"):
            rent.clear_wishlist()
        with allure.step("Verifying whether product is adding to wishlist"):
            furniture.navigate_to_website()
            expected_prodname=rent.get_expected_product_name()
            actual_prodname=rent.get_actual_product_name()
            assert expected_prodname == actual_prodname , "product not added to wishlist"
            print("product successfully added to wishlist")
            self.logger.info("\nTest finished. Check console output and the 'logs' folder.")
            assert True
