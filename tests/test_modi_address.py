import pytest
import allure
from config.environment import Environment
from pages.modi_login import ModiLoginPage
from tests.base_test import BaseTest
from pages.modi_home_page import ModiHomePage
from pages.modi_dashboard_page import ModiDashboardPage
from pages.modi_billing_address_page import ModiBillingAddressPage
from pages.modi_edit_billing_page import ModiEditBillingPage
# from pages.modi_edit_account_page import ModiEditAccountPage
@pytest.mark.modi
class TestLogin(BaseTest):
    @allure.title("Test login page to verify screenshot on failure")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.integration
    def test_login_for_modi_address(self):
        modi_home_page=ModiHomePage(self.driver)
        modi_login_page = ModiLoginPage(self.driver)
        modi_dashboard_page=ModiDashboardPage(self.driver)
        modi_billing_address=ModiBillingAddressPage(self.driver)
        modi_edit_billing_page= ModiEditBillingPage(self.driver)
        # modi_edit_account_page=ModiEditAccountPage(self.driver)
        env = Environment("modi")
        base_url = env.get_base_url()
        username = env.get_username()
        password = env.get_password()

        with allure.step("Navigate and perform a successful automation"):
            modi_home_page.navigate_to(base_url)
            modi_home_page.nav_to_login()
            modi_login_page.login(username, password)
            assert modi_login_page.is_login_successful(), "Login step failed before the intended assertion."
            modi_dashboard_page.modi_dashboard()
            modi_billing_address.modi_billing_address()
            modi_edit_billing_page.modi_edit_billing()
            modi_dashboard_page.nav_to_logout()
            # modi_dashboard_page.nav_to_account_details()
            # assert modi_edit_account_page.is_account_details_page(), \
            #     "Account Details page not loaded or user logged out"
            # modi_edit_account_page.modi_edit_account_page()
