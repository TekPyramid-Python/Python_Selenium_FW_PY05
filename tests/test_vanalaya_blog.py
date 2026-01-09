

import allure
import pytest

from config.environment import Environment
from pages.vanalaya_blog_page import BlogPage
from tests.base_test import BaseTest


# @allure.feature("Authentication")
# @allure.story("User Login")
class TestVanalayaBlog(BaseTest):
    """
    Test class for login functionality against saucedemo.com.
    """

    @allure.title("Test successful login with valid credentials")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_successful_login(self):
        """
        Test Case: Verify successful login using credentials from config.yaml.
        """
        # --- Initialize pages and variables ---
        blog_page = BlogPage(self.driver)
        env = Environment("test")  # Uses ENV=demo by default if not set
        base_url = env.get_base_url()
        # username = env.get_username()


        with allure.step("Navigate to Blog page"):
            blog_page.navigate_to(base_url)
            # The is_visible method is inherited from BasePage
            assert blog_page.is_visible(blog_page.BLOG_BUTTON), "Blog page did not load properly"

        with allure.step("Clicking Blog button"):
            blog_page.click_blog_button()
            assert blog_page.is_visible(blog_page.BLOG_IMAGE),"Blog Button is visible or not"

        with allure.step("Click Blog Image"):
            blog_page.click_blog_image()
            assert blog_page.is_visible(blog_page.LOGO),"Blog Button is not visible"

        with allure.step("Scroll Down to Element"):
            blog_page.scroll_bottom()
            assert blog_page.is_visible(blog_page.SCROLL_DOWN,20),"Not scrolling down properly"

        with allure.step("Enter Email ID"):
            blog_page.enter_email("abcd@gmail.com")
            assert blog_page.is_visible(blog_page.ENTER_EMAIL_ID),"Email Id is not visible"

        with allure.step("Click Submit button"):
            blog_page.click_submit()
            assert blog_page.is_visible(blog_page.CLICK_SUBMIT),"Blog Button is visible or not"

        with allure.step("Verify successful blog and page title"):
            assert blog_page.is_subscribe_successful(), "Subscribe was not successful, inventory page not found."

            expected_title = '5 Everyday Organic Swaps That Can Transform Your Health Naturally – Vanalaya'# This is the correct title for saucedemo
            actual_title = blog_page.get_title()  # This method is inherited from BasePage
            assert expected_title == actual_title, f"Expected title '{expected_title}', but got '{actual_title}'"

