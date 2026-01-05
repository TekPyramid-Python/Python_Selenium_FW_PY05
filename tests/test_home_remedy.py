from time import sleep

import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.environment import Environment
from pages.clinicwala_homepage import HomePage
from pages.remedies_page import HomeRemedyPage
from tests.base_test import BaseTest
@allure.feature("Dawaiawala")
@allure.story("To get Home remedy")
class TestHomeRemedy(BaseTest):
    @pytest.mark.clinicwala
    def test_get_home_remedy(self):
        home_page = HomePage(self.driver)
        remedy_page =HomeRemedyPage(self.driver)
        env = Environment()
        base_url = env.get_base_url()
        with allure.step("Navigate to home page"):
            home_page.navigate_to(base_url)
            assert home_page.is_visible(home_page.FIND_CURE_LINK), "Home page did not load properly"

        with allure.step("Navigate to Remedies page"):
            home_page.on_click_find_cure()
            expected_title = "Alternative Medicine: Remedies holistic treatments"
            actual_title = home_page.get_title()
            assert expected_title == actual_title, 'Title mismatch'

        with allure.step("Get Home remedy for specific illness"):
            remedy_page.select_ill()

        with allure.step("Scrolling to bottom of the remedies page"):
            remedy_page.get_doctors_apps()



