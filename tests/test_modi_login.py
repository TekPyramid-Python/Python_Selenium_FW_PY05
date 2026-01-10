import pytest
import allure
from config.environment import Environment
from pages.modi_login import ModiLoginPage
from pages.modi_home_page import ModiHomePage
from pages.modi_product_page import ModiProductPage
from pages.modi_billing_page import ModiBillingPage
from pages.modi_cart_page import ModiCartPage
from pages.modi_product_list_page import ModiProductListPage
from tests.base_test import BaseTest
@pytest.mark.modi
class TestLogin(BaseTest):
    @allure.title("Test login page to verify screenshot on failure")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.system

    def test_login_for_modi(self):
        modi_home_page=ModiHomePage(self.driver)
        modi_login_page = ModiLoginPage(self.driver)
        modi_product_list_page=ModiProductListPage(self.driver)
        modi_product_page=ModiProductPage(self.driver)
        modi_cart_page=ModiCartPage(self.driver)
        modi_billing_page=ModiBillingPage(self.driver)
        env = Environment("modi")
        base_url = env.get_base_url()
        username = env.get_username()
        password = env.get_password()

        with allure.step("Navigate and perform a successful automation"):
            modi_home_page.navigate_to(base_url)
            modi_home_page.nav_to_login()
            modi_login_page.login(username, password)
            assert modi_login_page.is_login_successful(), "Login step failed before the intended assertion."
            modi_home_page.modi_home_page()
            modi_product_list_page.modi_product_list_page()
            modi_product_page.modi_product_page()
            modi_cart_page.modi_view_cart_page()
            modi_cart_page.modi_cart_page()
            modi_billing_page.modi_billing_page()

