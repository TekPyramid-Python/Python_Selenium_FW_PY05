import allure

from ..pages.furniture_page import Furniture_Module
from ..tests.base_test import BaseTest
from ..pages.rentomojo_homepage import RentomojoHomepage
import pytest

class TestHomepage(BaseTest):
    @pytest.mark.rentomojo
    def test_homepage(self):
        with allure.step("Navigating to website"):
            furniture = Furniture_Module(self.driver)
            furniture.navigate_to_website()
        homepage = RentomojoHomepage(self.driver)
        with allure.step("adding product from homepage to cart"):
            homepage.addingproduct_tocart()
        with allure.step("clearing cart"):
            homepage.clearing_cart()