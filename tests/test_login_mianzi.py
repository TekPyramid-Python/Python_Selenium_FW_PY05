import pytest
import allure
from pages.login_page import LoginPage

@allure.feature("Login")
@allure.story("Login page loads and accepts credentials")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_mz01_valid_login(driver, env):

    login_page = LoginPage(driver)

    with allure.step("Open login page"):
        login_page.open_login()

    with allure.step("Enter email and password"):
        login_page.enter_credentials(
            env.get_username(),
            env.get_password()
        )

    with allure.step("Verify email is entered"):
        assert login_page.get_email_value() == env.get_username()

    with allure.step("Verify password is entered"):
        assert login_page.get_password_value() == env.get_password()








