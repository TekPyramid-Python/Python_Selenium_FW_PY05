from ..tests.base_test import BaseTest
from ..pages.rentomojo_wishlist import Rentomojo_Wishlist
import pytest
from ..config.environment import Environment
import allure



class TestWishlist(BaseTest):
    @pytest.mark.usefixtures("rentomojo_login")
    @pytest.mark.rentomojo
    def test_wishlist(self):
        with allure.step("Verifying whether product is adding to wishlist"):
            rent = Rentomojo_Wishlist(self.driver)
            rent.clear_wishlist()
            rent.add_to_wishlist()
            print("\nTest finished. Check console output and the 'logs' folder.")
            assert True
