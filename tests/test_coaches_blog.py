# tests/test_coaches_blog.py
import pytest
import allure
from pages.home_page import HomePage
from pages.coaches_page import CoachesPage
from pages.blog_page import BlogPage
from tests.base_test import BaseTest

@allure.feature("End-to-End Navigation")
@allure.story("Coaches to Blog images flow")
class TestCoachesBlogNavigation(BaseTest):

    @allure.title("Verify Coaches page, Blog images, and Home navigation")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_coaches_blog_navigation(self):
        home_page = HomePage(self.driver)
        coaches_page = CoachesPage(self.driver)
        blog_page = BlogPage(self.driver)

        with allure.step("Open website and verify Home page"):
            home_page.navigate_to("https://swasthyawarriors.com")
            assert home_page.is_home_loaded(), "Home page did not load"

        with allure.step("Navigate to Coaches page"):
            home_page.click_coaches()
            assert coaches_page.is_coaches_page_loaded(), "Coaches page not loaded"

        with allure.step("Navigate to Blog page and click blog images"):
            home_page.click_blog()
            assert blog_page.is_blog_page_loaded(), "Blog page not loaded"
            blog_page.click_all_blog_images()

        with allure.step("Verify Blog content is displayed"):
            assert blog_page.is_blog_content_visible(), "Blog content not displayed"

        with allure.step("Navigate back to Home page"):
            blog_page.navigate_home()
            assert home_page.is_home_loaded(), "Failed to return to Home page"
