import pytest
import allure
from config.environment import Environment
from pages.modi_home_page import ModiHomePage
from tests.base_test import BaseTest
from pages.modi_billing_page import ModiBillingPage
from pages.modi_cart_page import ModiCartPage
from pages.modi_product_list_page import ModiProductListPage
from pages.modi_product_page import ModiProductPage
@pytest.mark.modi
class TestCupon(BaseTest):
    @allure.title("Test order page to verify ")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.system

    def test_cupon_for_orders(self):
        modi_home_page=ModiHomePage(self.driver)
        modi_product_list_page=ModiProductListPage(self.driver)
        modi_product_page=ModiProductPage(self.driver)
        modi_cart_page=ModiCartPage(self.driver)
        modi_billing_page=ModiBillingPage(self.driver)


        env = Environment("modi")
        base_url = env.get_base_url()

        with allure.step("Navigate and perform a successful automation"):
            modi_home_page.navigate_to(base_url)
            modi_home_page.modi_home_page()
            modi_product_list_page.modi_product_list_page()
            modi_product_page.modi_product_page()
            modi_cart_page.modi_view_cart_page()
            modi_cart_page.modi_cupon()
            modi_cart_page.modi_cart_page()
            modi_billing_page.modi_billing_page()




