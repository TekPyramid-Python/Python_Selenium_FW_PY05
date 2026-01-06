from time import sleep

import allure

from ..pages.furniture_page import Furniture_Module
from ..pages.rentomojo_location_handling import LocationHandling
from ..tests.base_test import BaseTest
import pytest
class TestAddProducts(BaseTest):


    @pytest.mark.rentomojo

    def test_addDifferentLocationsProducts(self):
        furniture = Furniture_Module(self.driver)
        location=LocationHandling(self.driver)
        with allure.step("Navigating to website"):
            furniture.navigate_to_website()
            sleep(5)
        with allure.step("adding product to cart from default city"):
            location.adding_product()
        with allure.step("adding product to cart from particular city"):
            location.changing_location()
            location.adding_product()