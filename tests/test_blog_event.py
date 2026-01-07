import pytest
import allure
from pages.home_page import HomePage
from pages.blog_page import BlogPage
from pages.events_page import EventsPage
from tests.base_test import BaseTest


@allure.feature("Blog and Events Navigation")
@allure.story("Navigate from Home → Blog → Events section")
class TestBlogAndEventsNavigation(BaseTest):

    @allure.title("Verify navigation from Home to Blog and Events section")
    def test_blog_events_navigation(self):

        home = HomePage(self.driver)
        blog = BlogPage(self.driver)
        events = EventsPage(self.driver)

        with allure.step("Navigate to Home page"):
             home.navigate_to("https://www.swasthyawarriors.com/")
             assert home.is_home_loaded()

        with allure.step("Navigate to Blog page"):
             home.click_blog()
             assert blog.is_blog_page_loaded()

        with allure.step("Navigate to Events page"):
                home.click_events()
                assert events.is_events_page_loaded(), "Events page not loaded"

        with allure.step("Return to Home"):
                events.navigate_home()
                assert home.is_home_loaded()