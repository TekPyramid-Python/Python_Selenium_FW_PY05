import pytest
import allure
from config.environment import Environment
from pages.modi_home_page import ModiHomePage
from pages.modi_login import ModiLoginPage
from tests.base_test import BaseTest
from pages.modi_blog_page import ModiBlogPage
from pages.modi_product_list_page import ModiProductListPage
from pages.modi_product_page import ModiProductPage
from pages.modi_cart_page import ModiCartPage

class TestBlog(BaseTest):
    @allure.title("Test login page to verify screenshot on failure")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.system
    def test_blog_for_modi(self):
        modi_home_page = ModiHomePage(self.driver)
        modi_login_page = ModiLoginPage(self.driver)
        modi_blog_page=ModiBlogPage(self.driver)
        modi_product_list_page=ModiProductListPage(self.driver)
        modi_product_page=ModiProductPage(self.driver)
        modi_cart_page=ModiCartPage(self.driver)


        env = Environment("modi")
        base_url = env.get_base_url()
        username = env.get_username()
        password = env.get_password()

        with allure.step("Navigate and perform a successful automation"):
            modi_home_page.navigate_to(base_url)
            modi_home_page.nav_to_login()
            modi_login_page.login(username, password)
            assert modi_login_page.is_login_successful(), "Login step failed before the intended assertion."
            modi_home_page.blog_method()
            modi_blog_page.modi_blog_recepi()
            modi_home_page.recepi_method()
            modi_blog_page.modi_blog_recepi()
            modi_home_page.modi_home_page()
            modi_product_list_page.modi_product_list_page()
            modi_product_page.modi_product_page()
            modi_cart_page.modi_view_cart_page()
            modi_cart_page.modi_size_button()


