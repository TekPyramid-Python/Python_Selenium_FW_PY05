import pytest
import allure
from pages.home_page import HomePage
from pages.common_page import CommonPage
from tests.base_test import BaseTest
from pages.events_page import EventsPage



@allure.feature("End-to-End Navigation")
@allure.story("Navigate all menu pages and return Home")
class TestFullWebsiteNavigation(BaseTest):

    #@pytest.mark.e2e
    @allure.title("Verify navigation across all main pages and back to Home")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_full_site_navigation(self):

        home_page = HomePage(self.driver)
        common_page = CommonPage(self.driver)
        events_page = EventsPage(self.driver)


        with allure.step("Open website and verify Home page"):
            home_page.navigate_to("https://swasthyawarriors.com")
            assert home_page.is_home_loaded(), "Home page did not load"


        with allure.step("Navigate to Philosophy page"):
            home_page.click_philosophy()
            assert common_page.is_page_loaded(), "Philosophy page not loaded"
            home_page.click_home()


        with allure.step("Navigate to Testimonies page"):
            home_page.click_testimonies()
            assert common_page.is_page_loaded(), "Testimonies page not loaded"
            home_page.click_home()


        with allure.step("Navigate to Coaches page"):
            home_page.click_coaches()
            assert common_page.is_page_loaded(), "Coaches page not loaded"
            home_page.click_home()

        with allure.step("Navigate to Blog page"):
            home_page.click_blog()
            assert common_page.is_page_loaded(), "Blog page not loaded"
            home_page.click_home()


        with allure.step("Navigate to Contact Us page"):
            home_page.click_contact_us()
            assert common_page.is_page_loaded(), "Contact Us page not loaded"
            home_page.click_home()


        with allure.step("Verify user is back on Home page"):
            assert home_page.is_home_loaded(), "Failed to return to Home page"
