import pytest
import allure
from config.environment import Environment
from pages.modi_home_page import ModiHomePage
from pages.modi_brand_product_page import ModiBrandProductPage
from pages.modi_billing_page import ModiBillingPage
from pages.modi_cart_page import ModiCartPage
from pages.modi_product_list_page import ModiProductListPage
from tests.base_test import BaseTest


@pytest.mark.modi
class TestBrand(BaseTest):
    @allure.title("Test order page to verify ")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.integration

    def test_brand_for_orders(self):
        modi_home_page=ModiHomePage(self.driver)
        modi_product_list_page=ModiProductListPage(self.driver)
        modi_brand_product_page=ModiBrandProductPage(self.driver)
        modi_cart_page=ModiCartPage(self.driver)
        modi_billing_page=ModiBillingPage(self.driver)


        env = Environment("modi")
        base_url = env.get_base_url()

        with allure.step("Navigate and perform a successful automation"):
            modi_home_page.navigate_to(base_url)
            # modi_home_page.brand_hover_method()
            modi_product_list_page.modi_product_list_page()
            modi_brand_product_page.modi_brand_product()
            modi_cart_page.modi_view_cart_page()
            modi_cart_page.modi_cart_page()
            modi_billing_page.modi_billing_page()


