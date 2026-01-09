import pytest
import allure
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.testimonies_page import TestimoniesPage


@allure.feature("Navigation")
@allure.story("Home to Testimonies and social media review")
class TestTestimoniesPage(BaseTest):

    @pytest.mark.testimonies
    @allure.title("Verify navigation from Home to Testimonies, open social media reviews, and return Home")
    def test_home_to_testimonies(self):

        home_page = HomePage(self.driver)
        testimonies_page = TestimoniesPage(self.driver)

        with allure.step("Navigate to Home page"):
            home_page.navigate_to("https://www.swasthyawarriors.com/")
            assert home_page.is_visible(home_page.TESTIMONIES_MENU), "Home page not loaded"

        with allure.step("Click Testimonies section from Home page"):
            home_page.click_testimonies_menu()
            assert testimonies_page.is_page_loaded(), "Testimonies page not loaded"

        with allure.step("Open social media reviews from Testimonies page"):
            parent_window = self.driver.current_window_handle
            testimonies_page.open_social_media_reviews()
            assert len(self.driver.window_handles) > 1, "Social media reviews page did not open"

        with allure.step("Return to Home page"):
            self.driver.switch_to.window(parent_window)
            testimonies_page.navigate_home_page()
            assert home_page.is_visible(home_page.TESTIMONIES_MENU), "Failed to return Home"

