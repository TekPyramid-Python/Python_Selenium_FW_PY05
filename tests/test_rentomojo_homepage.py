import allure
from ..pages.furniture_page import Furniture_Module
from ..tests.base_test import BaseTest
from ..pages.rentomojo_homepage import RentomojoHomepage
import pytest
from ..tests.base_test import BaseTest  # Make sure this import path is correct for your structure
from ..tests.rentomojo_login_otp import rentomojo_login


class TestHomepage(BaseTest):
    @pytest.mark.rentomojo
    def test_homepage(self,rentomojo_login):
        furniture = Furniture_Module(self.driver)
        homepage = RentomojoHomepage(self.driver)
        with allure.step("Navigating to website"):
            homepage.navigate_to('https://www.rentomojo.com/bangalore')
        with allure.step("clearing cart"):
            homepage.clearing_cart()
            homepage.navigate_to('https://www.rentomojo.com/bangalore')
        with allure.step("validating whether the right product added from homepage to cart."):
            assert homepage.get_expected_product_name() == homepage.get_actual_product_name(), 'product not added to cart'
            self.logger.info('product successfully added to cart.')
        with allure.step("clearing cart"):
            homepage.clearing_cart()