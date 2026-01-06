from time import sleep

import allure

from ..pages.furniture_page import Furniture_Module
from ..tests.base_test import BaseTest
from ..pages.rentomojo_store_experience import RentomojoStoresPage
import pytest
class TestRentomojoStores(BaseTest):
    @pytest.mark.rentomojo
    def test_nearest_rentomojo_stores(self):
        with allure.step("Navigating to website"):
            furniture = Furniture_Module(self.driver)
            furniture.navigate_to_website()
        stores=RentomojoStoresPage(self.driver)
        with allure.step("Validating whether we are redirecting to correct sore page"):
            store_name=stores.rentomojo_get_expected_name()
            sleep(5)
            actual_store_name=stores.rentomojo_get_actual_name()
            assert store_name == actual_store_name