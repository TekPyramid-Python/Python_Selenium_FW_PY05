import allure

from ..pages.rentomojo_login_otp import rentomojo_login
from ..tests.base_test import BaseTest
from ..pages.furniture_page import Furniture_Module
import pytest
from ..config.environment import Environment


class TestFurnitureProductFlow(BaseTest):
    @pytest.mark.rentomojo

    def test_add_furniture_product(self,rentomojo_login):
        furniture=Furniture_Module(self.driver)
        with allure.step("clearing cart"):
            self.logger.info("clearing cart")
            furniture.clearing_cart()
        furniture.navigate_to(Environment.get_base_url(self.driver))
        with allure.step("adding to cart"):
            furniture.adding_furniture_product()
        with allure.step("clearing cart"):
            self.logger.info("clearing cart")
            furniture.clearing_cart()

