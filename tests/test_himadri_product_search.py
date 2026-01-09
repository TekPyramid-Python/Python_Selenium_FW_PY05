import allure

from config.environment import Environment
from tests.base_test import BaseTest
from pages.himadri_login_page import HimadriLoginPage
from pages.himadri_search_product import HimadriProductSearch

class TestHimadriCartPage(BaseTest):
    def test_successful_login(self):
        login_page = HimadriLoginPage(self.driver)
        search_product = HimadriProductSearch(self.driver)
        env = Environment('himadri')
        base_url = env.get_base_url()
        email = env.get_email()
        password = env.get_password()
        searched_text = 'lotus'

        with allure.step("Navigate to login page"):
            login_page.navigate_to(base_url)
            assert login_page.is_visible(login_page.LOGIN_CLICK), "Login page did not load properly"

        with allure.step("Perform login with valid credentials"):
            login_page.login(email, password)

        with allure.step("Search for a product"):
            search_product.search_for_product(searched_text)

        with allure.step("Verify search results"):
            product_names = search_product.result_products_names()

            assert len(product_names) > 0, "No products displayed for search"

            for name in product_names:
                assert searched_text.lower() in name.lower(), \
                    f"Search mismatch! '{searched_text}' not found in '{name}"