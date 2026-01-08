from time import sleep

import allure

from ..pages.rentomojo_homepage import RentomojoHomepage
from ..pages.rentomojo_location_handling import LocationHandling
from ..tests.base_test import BaseTest
import pytest
from ..tests.rentomojo_login_otp import rentomojo_login

class TestAddProducts(BaseTest):
    @pytest.mark.rentomojo

    def test_addDifferentLocationsProducts(self,rentomojo_login):
        location=LocationHandling(self.driver)
        with allure.step("adding product to cart from default city"):
            location.adding_product()
        with allure.step("adding product to cart from particular city"):
            location.changing_location()
            location.adding_product()