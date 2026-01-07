import pytest
import allure
from pages.home_page import HomePage
from tests.base_test import BaseTest


@allure.feature("Home Page")
@allure.story("Verify Home page loads correctly")
class TestHomePage(BaseTest):

    @pytest.mark.smoke
    @allure.title("Verify Home page loads and logo is visible")
    def test_home_page_loads(self):

        home_page = HomePage(self.driver)

        with allure.step("Open Swasthya Warriors website"):
            home_page.navigate_to("https://www.swasthyawarriors.com/")
            assert home_page.is_home_loaded(), "Home page did not load"

        with allure.step("Verify website logo is displayed"):
            assert home_page.is_logo_visible(), "Home page logo is not visible"

        with allure.step("Verify main menu items are visible"):
            assert home_page.is_menu_visible(), "Main menu is not visible"
