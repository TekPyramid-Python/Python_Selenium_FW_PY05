import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.environment import Environment
from pages.digit_home_page import Digit_home_page
from pages.directors_and_officers_page import Directors_and_Officers
from tests.base_test import BaseTest


@allure.feature("Authentication")
@allure.story("User Login")
class TestverifyDandOinsurancequote(BaseTest):
   
    @allure.title("verified title of go digit home page")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_to_verify_D_and_O_insurance_quote(self):
      
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
                    EC.presence_of_element_located(home_page.D_and_O_insurance_link))

                home_page.click_on_OPD_health_insurance()
            except Exception:
                self.driver.execute_script("arguments[0].click();", element)

        with allure.step("Verify successful medical health insurance page title"):
            expected_title = "D&O Insurance: Directors and Officers Liability Insurance by Digit"  # This is the correct title "Health Insurance Plan: Buy Medical Insurance Online"
            actual_title = home_page.get_title()  # This method is inherited from BasePage
            assert expected_title == actual_title, f"Expected title '{expected_title}', but got '{actual_title}'"
            
        directors=Directors_and_Officers(self.driver)
        directors.send_user_name()
        directors.send_mobile_number()
        directors.send_email()
        directors.click_on_next_button()
        
        directors.send_company_name()
        directors.send_pincode()
        directors.send_number_employee()
        directors.click_on_next_button()
        
        directors.select_industry_category()
        directors.send_sum_insured()
        directors.click_on_no()
        directors.click_on_next_button()
        
        expected_text='Thank you for sharing your details with us!'
        actual_text=directors.confirmation_text()
        assert expected_text==actual_text , f"Expected text '{expected_text}', but got '{actual_text}'"