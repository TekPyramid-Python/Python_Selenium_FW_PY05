import allure
import pytest

from ..pages.rentomojo_homepage import RentomojoHomepage
from ..tests.rentomojo_login_otp import rentomojo_login
from ..pages.furniture_page import Furniture_Module
from ..tests.base_test import BaseTest  # Make sure this import path is correct for your structure



class TestFurnitureProductFlow(BaseTest):
    @pytest.mark.rentomojo

    def test_add_furniture_product(self,rentomojo_login):
        furniture=Furniture_Module(self.driver)
        with allure.step("clearing cart"):
            self.logger.info("clearing cart")
            furniture.clearing_cart()
        homepage = RentomojoHomepage(self.driver)
        homepage.redirect_to_website()
        with allure.step("adding to cart"):
            furniture.adding_furniture_product()
        with allure.step("clearing cart"):
            self.logger.info("clearing cart")
            furniture.clearing_cart()

