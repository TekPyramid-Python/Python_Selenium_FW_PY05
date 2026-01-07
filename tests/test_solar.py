import pytest
import allure
import time
from datetime import datetime, date
from tests.base_test import BaseTest
from config.environment import Environment
from pages.solar_login_page import LoginPage
from pages.solar_lead_creation_page import LeadCreationPage
from pages.solar_lead_summary import SiteInfo
from pages.solar_lead_data import Lead_Data
from pages.solar_validate_leadCreation_page import SiteInfoValidation

@allure.feature('Lead_Management Journey')
class TestLeadManagement(BaseTest):

    # @allure.mark.smoke
    @pytest.mark.solarsystem
    @allure.story("Happy Lead Management")
    @allure.title("Test End-to-End Lead Management")
    @allure.description("This test verifies the complete Lead management cycle: Login > Add Item > Checkout > Finish > Logout.--to be edited")

    def test_end_to_end_lead_management_happy_path(self):

        login_page = LoginPage(self.driver)
        lead_creation_page = LeadCreationPage(self.driver)
        lead_summary = SiteInfo(self.driver)
        lead_data = Lead_Data()
        site_info_validation = SiteInfoValidation(self.driver)


        env = Environment()
        base_url = env.get_base_url()

        with allure.step("1. Login to Application"):
            login_page.navigate_to(base_url)
            login_page.login(env.get_username(), env.get_password())
            time.sleep(3)
            assert login_page.is_login_successful(), "Did not land on Lead management page."
            time.sleep(2)
            self.logger.info("Login successful and lead management page is displayed.")

        with allure.step("2. Open Lead Creation Page"):
            lead_creation_page.open_lead_creation_page()
            assert lead_creation_page.is_lead_creation_page_opening_successful()

        with allure.step("3. Create Lead"):
            lead_creation_page.fill_and_submit_lead(lead_data.site_address, lead_data.lead_name, lead_data.lead_email)

        with allure.step('4. Verify lead name'):
            # print(str(lead_data.lead_name[0]))
            assert lead_data.lead_name == site_info_validation.get_lead_name(), "Lead name does not match."
            self.logger.info("Lead name verified successfully.")

        with allure.step('5. Verify lead email'):
            assert lead_data.lead_email in site_info_validation.get_lead_email(), "Lead email does not match."
            self.logger.info("Lead email verified successfully")

        with allure.step("6. Additional info page"):
            lead_summary.additional_info(lead_data.deal_value, lead_data.target_close_date, lead_data.system_size, lead_data.probability)

        with allure.step("7. Verify deal value"):
            def normalize_amount(value: str) -> int:
                return int(value.replace("₹", "").replace(",", "").strip())

            assert normalize_amount(lead_data.deal_value) == \
                   normalize_amount(site_info_validation.get_deal_value()), \
                   "Deal value does not match."
            self.logger.info("Deal value verified successfully.")

        with allure.step("8. Verify target close date"):
            def normalize_date(value: str) -> date:
                for fmt in ("%m-%d-%Y", "%B %d, %Y"):
                    try:
                        return datetime.strptime(value.strip(), fmt).date()
                    except ValueError:
                        pass

                raise ValueError(f"Unsupported date format: {value}")

            assert normalize_date(lead_data.target_close_date) == normalize_date(site_info_validation.get_target_close_date()), "Target close date do not match."
            self.logger.info("Target close date verified successfully.")

        with allure.step("9. Verify system size"):
            def normalize_system_size(value: str) -> int:
                return int(value.replace("kW", "").strip())

            assert normalize_system_size(lead_data.system_size) == \
                   normalize_system_size(site_info_validation.get_system_size()), \
                   "System size do not match."
            self.logger.info("System size verified successfully.")

        with allure.step("10. Verify probability"):
            assert lead_data.probability == site_info_validation.get_probability(), "Probability do not match."
            self.logger.info("Probability verified successfully.")
