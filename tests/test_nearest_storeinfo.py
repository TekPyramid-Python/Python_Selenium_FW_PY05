from time import sleep

import allure
from ..pages.rentomojo_homepage import RentomojoHomepage
# from ..pages.furniture_page import Furniture_Module
from ..pages.rentomojo_store_experience import RentomojoStoresPage
import pytest
from ..tests.base_test import BaseTest  # Make sure this import path is correct for your structure
from ..tests.rentomojo_login_otp import rentomojo_login


class TestRentomojoStores(BaseTest):
    @pytest.mark.rentomojo
    def test_nearest_rentomojo_stores(self,rentomojo_login):
        homepage=RentomojoHomepage(self.driver)
        with allure.step("Navigating to website"):
            homepage.redirect_to_website()
        stores=RentomojoStoresPage(self.driver)
        with allure.step("Validating whether we are redirecting to correct sore page"):
            store_name=stores.rentomojo_get_expected_name()
            sleep(5)
            actual_store_name=stores.rentomojo_get_actual_name()
            assert store_name == actual_store_name