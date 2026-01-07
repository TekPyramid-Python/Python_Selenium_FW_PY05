import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.coaches_page import CoachesPage
from pages.terms_page import TermsPage
from tests.base_test import BaseTest


data = {
    "home_url": "https://www.swasthyawarriors.com/",
}

#@pytest.mark.e2e
@allure.feature("End to End Navigation")
@allure.story("Home → Coaches → LinkedIn → Terms → Home")
class TestCoachesLinkedInTerms(BaseTest):

    @allure.title("Verify Coaches, LinkedIn, Terms of Use navigation")
    def test_coaches_linkedin_terms_navigation(self):


        home = HomePage(self.driver)
        coaches = CoachesPage(self.driver)
        terms = TermsPage(self.driver)

        with allure.step("Open Swasthya Warriors Home page"):
            home.navigate_to(data['home_url'])
            assert home.is_home_loaded(), "Home page did not load"


        with allure.step("Navigate to Coaches page"):
            home.click_coaches()
            assert coaches.is_page_loaded(), "Coaches page not loaded"

        with allure.step("Verify Coaches page content"):
            assert coaches.is_content_visible(), "Coaches content missing"

        with allure.step("Open LinkedIn profile"):
            coaches.open_linkedin_profile()
            WebDriverWait(self.driver, 10).until(lambda d: "linkedin.com" in d.current_url)
            assert coaches.is_linkedin_opened(), "LinkedIn did not open"


        self.driver.switch_to.window(self.driver.window_handles[0])

        with allure.step("Open Terms of Use from footer"):
            coaches.click_terms_of_use()
            assert terms.is_page_loaded(), "Terms of Use page not loaded"

        with allure.step("Verify Terms of Use content"):
            assert terms.is_content_visible(),"Terms of Use page not loaded"

        with allure.step("Return to Home page"):
            terms.click_home_logo()
            assert home.is_home_loaded(), "Failed to return Home page"
