'''test case 3'''
import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.environment import Environment
from pages.digit_home_page import Digit_home_page
from pages.digit_policy_page import Policy
from pages.medical_insurance_page import Medical_insurance_page
from tests.base_test import BaseTest


@allure.feature("Authentication")
@allure.story("User Login")
class Testsupertopuphealthpolicy(BaseTest):
    """
    Test class for login functionality against saucedemo.com.
    """

    @allure.title("verified title of go digit home page")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_super_top_up_navigation(self):
        """
        Test Case: Verify successful login using credentials from config.yaml.
        """
        # --- Initialize pages and variables ---
        home_page = Digit_home_page(self.driver)
        medical_insurance_page = Medical_insurance_page(self.driver)
        policy = Policy(self.driver)
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
                    EC.presence_of_element_located(home_page.health_image_link))

                home_page.click_health_insurance()
            except Exception:
                self.driver.execute_script("arguments[0].click();", element)

        with allure.step("Verify successful medical health insurance page title"):
            expected_title = "Health Insurance Plan: Buy Medical Insurance Online"  # This is the correct title "Health Insurance Plan: Buy Medical Insurance Online"
            actual_title = home_page.get_title()  # This method is inherited from BasePage
            assert expected_title == actual_title, f"Expected title '{expected_title}', but got '{actual_title}'"

            medical_insurance_page.send_keys_to_pincode()
            medical_insurance_page.send_keys_to_mobile_number()
            medical_insurance_page.click_on_view_prize()

        with allure.step("Verify successful 'Health Insurance Policy' page title"):
            expected_title = "Health Insurance Plan: Buy Medical Insurance Online"  # This is the correct title "Health Insurance Plan: Buy Medical Insurance Online"
            actual_title = home_page.get_title()  # This method is inherited from BasePage
            assert expected_title == actual_title, f"Expected title '{expected_title}', but got '{actual_title}'"

            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(policy.super_top_up_policy_link))
            self.driver.execute_script("arguments[0].click();", element)
        

            expected_popup_text='Get Super Top Up Policy'
            actual_popup_text=policy.text_super_pop_up()
            assert expected_popup_text==actual_popup_text, f"Expected pop up text '{expected_popup_text}', but got '{actual_popup_text}'"

            policy.send_keys_super_top_up_mobile_number()
            policy.click_on_get_a_call_back()
            # element = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located(policy.super_top_up_pop_up_get_a_call_back_button))
            # self.driver.execute_script("arguments[0].click();", element)

            expected_popup_confirmation_text = 'We will reach out to you shortly'
            actual_popup_confirmation_text = policy.text_confirmation_message()
            assert expected_popup_text == actual_popup_text, f"Expected confirmation message '{expected_popup_confirmation_text}', but got '{actual_popup_confirmation_text}'"

            policy.click_on_ok_button()

            with allure.step("Verify successful 'Health Insurance Policy' page title"):
                expected_title = "Health Insurance Plan: Buy Medical Insurance Online"  # This is the correct title "Health Insurance Plan: Buy Medical Insurance Online"
                actual_title = home_page.get_title()  # This method is inherited from BasePage
                assert expected_title == actual_title, f"Expected title '{expected_title}', but got '{actual_title}'"

                
            
            
            
            
