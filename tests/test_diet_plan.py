from time import sleep

import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.environment import Environment
from pages.clinicwala_homepage import HomePage
from pages.dietplanpage import DietPlanPage
from tests.base_test import BaseTest

@allure.feature("Food and Diet")
@allure.story("To get Diet plan")
class TestDietPlan(BaseTest):
    @pytest.mark.clinicwala
    def test_get_dietplan(self):
        home_page = HomePage(self.driver)
        dietplan_page=DietPlanPage(self.driver)
        env = Environment()
        base_url = env.get_base_url()

        with allure.step("Navigate to home page"):
            home_page.navigate_to(base_url)
            assert home_page.is_visible(home_page.FOOD_DIET_LINK), "Home page did not load properly"

        with allure.step("Navigate to diet plan page"):
            home_page.on_click_foodndiet()
            expected_title = "Clinicwala: Expert Diet Plans for Specific Health Conditions"
            actual_title = home_page.get_title()
            assert expected_title == actual_title, 'Title mismatch'

        with allure.step("Selecting specific health condition"):
            dietplan_page.selct_health_condition()

        with allure.step("Navigate to reciepe link"):
            dietplan_page.select_reciepe()

        dietplan_page.on_click_back()
