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
        with allure.step("Navigating to website"):
            furniture = Furniture_Module(self.driver)
            furniture.navigate_to_website()
        rent = Rentomojo_Wishlist(self.driver)
        with allure.step("clearing wishlist"):
            rent.clear_wishlist()
        with allure.step("Verifying whether product is adding to wishlist"):
            rent.add_to_wishlist()
            self.logger.info("\nTest finished. Check console output and the 'logs' folder.")
            assert True
