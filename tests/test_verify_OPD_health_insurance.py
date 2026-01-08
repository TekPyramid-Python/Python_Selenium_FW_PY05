'''test case 2'''
import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.environment import Environment
from pages.Health_Insurance_Plans_with_OPD_Cover_Online_page import OPD_cover_online
from pages.digit_home_page import Digit_home_page
from tests.base_test import BaseTest


@allure.feature("Authentication")
@allure.story("User Login")
class TestverifyOPDhealthinsurance(BaseTest):
    """
    Test class for login functionality against saucedemo.com.
    """

    @allure.title("verified title of go digit home page")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_successful_navigate_to_home_page(self):
        """
        Test Case: Verify successful login using credentials from config.yaml.
        """
        # --- Initialize pages and variables ---
        home_page = Digit_home_page(self.driver)
        env = Environment()  # Uses ENV=demo by default if not set
        base_url = env.get_base_url()

        with allure.step("Verify successful home page title"):
            home_page.navigate_to(base_url)
            expected_title = "Digit Insurance | Buy Car, Bike, Health & Travel Insurance Online in India"  # This is the correct title for saucedemo
            actual_title = home_page.get_title()  # This method is inherited from BasePage
            assert expected_title == actual_title, f"Expected title '{expected_title}', but got '{actual_title}'"

            home_page.scroll_to_health_insurance()

            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(home_page.opd_health_insurance_link))

                home_page.click_on_OPD_health_insurance()
            except Exception:
                self.driver.execute_script("arguments[0].click();", element)

            expected_title = "Buy Health Insurance Plans with OPD Cover Online in India"  # This is the correct title for saucedemo
            actual_title = home_page.get_title()  # This method is inherited from BasePage
            assert expected_title == actual_title, f"Expected title '{expected_title}', but got '{actual_title}'"
            
            OPD_insurance=OPD_cover_online(self.driver)
            OPD_insurance.send_keys_to_OPD_name()
            OPD_insurance.send_keys_to_OPD_mobile_number()
            OPD_insurance.click_on_lets_connect()
            
            expected_text_OPD='Great. We"ll call you soon.'
            actual_text_OPD=OPD_insurance.get_confirmation_message_OPD()
            assert expected_text_OPD==actual_text_OPD ,f"Expected text '{expected_text_OPD}', but got '{actual_text_OPD}'"
