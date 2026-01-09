# tests/test_login.py
import allure
import pytest

from config.environment import Environment
from pages.vanalaya_back_to_top_pages import BackTopPages
from tests.base_test import BaseTest


# @allure.feature("Authentication")
# @allure.story("User Login")
class TestVanalayaBackTop(BaseTest):
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
        back_top = BackTopPages(self.driver)
        env = Environment("test")  # Uses ENV=demo by default if not set
        base_url = env.get_base_url()
        username = env.get_username()


        with allure.step("Navigate to Blog page"):
            back_top.navigate_to(base_url)
            # The is_visible method is inherited from BasePage
            assert back_top.is_visible(back_top.LOGO), "Page did not load properly"

        with allure.step("Scrolling downwards"):
            back_top.scroll_down_home()
            assert back_top.is_visible(back_top.BLOG_BUTTON),'Scroll Down Successfully'

        with allure.step("Perform blog with valid credentials"):
            back_top.click_b2top_button_from_home()
            assert back_top.is_visible(back_top.BACK_TO_TOP_BUTTON)

        with allure.step("Perform blog with valid credentials"):
            back_top.click_blog_button()
            assert back_top.is_visible(back_top.BLOG_BUTTON),'Blog Button is not visible'

        with allure.step("Scrolling downwards"):
            back_top.scroll_down_from_blog()
            assert back_top.is_visible(back_top.BACK_TO_TOP_BUTTON),'Scroll Down from home is not working'

        with allure.step("Perform blog with valid credentials"):
            back_top.click_b2top_button_from_blog()
            assert back_top.is_visible(back_top.LOGO),'Logo is not visible'

        with allure.step("Perform blog with valid credentials"):
            back_top.click_contact_button()
            assert back_top.is_visible(back_top.CONTACT_CLICK),'Contact button is not visible'

        with allure.step("Scrolling downwards"):
            back_top.scroll_down_contact()
            assert back_top.is_visible(back_top.BACK_TO_TOP_BUTTON),'Scroll Down is not working'

        with allure.step("Perform blog with valid credentials"):
            back_top.click_b2top_button_from_contact()
            assert back_top.is_visible(back_top.LOGO),'Logo is not visible'
