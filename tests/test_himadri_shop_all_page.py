import allure
import pytest

from config.environment import Environment
from pages.validation_shop_all_page import ShopAll_Validation
from tests.base_test import BaseTest
from pages.himadri_login_page import HimadriLoginPage

class TestLogin(BaseTest):

    @allure.title("Test successful login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_successful_login(self):
        login_page = HimadriLoginPage(self.driver)
        shopall_valid = ShopAll_Validation(self.driver)
        env = Environment('himadri')
        base_url = env.get_base_url()
        email = env.get_email()
        password = env.get_password()


        with allure.step("Navigate to login page"):
            login_page.navigate_to(base_url)
            assert login_page.is_visible(login_page.LOGIN_CLICK), "Login page did not load properly"

        with allure.step("Perform login with valid credentials"):
            login_page.login(email, password)


        with allure.step('click on the shop all button on the account page'):
            shopall_valid.click_shopall()

        with allure.step("Checking Click on Shop All is successful"):
            shopall_valid.is_clickon_shopall_successful()

        with allure.step("Validating productname in Product categories and Product page are same"):
            shopall_valid.validating_productname_in_productcategories()

