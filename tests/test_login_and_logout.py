import allure
import pytest

from config.environment import Environment
from pages.dental_home_page import HomePage
from pages.dental_kart_profile import ProfilePage
from pages.dental_login_page import LoginPage


@pytest.fixture(scope="function")
def log_in_and_out(request):
    driver = request.cls.driver  # Access the driver created in BaseTest

    # Initialize Pages
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    profile_page = ProfilePage(driver)
    env = Environment()

    # --- SETUP: Login ---
    with allure.step("Fixture: Navigating and Logging In"):
        home_page.navigate_to(env.get_base_url())
        if not(home_page.is_user_logged_in()):
            home_page.click_login()
            login_page.login(env.get_username(), env.get_password())


        assert home_page.is_user_logged_in, "Fixture Fail: Login failed."

    yield  # <--- Control is passed to your test function here

    # --- TEARDOWN: Logout ---
    with allure.step("Fixture: Logging Out"):
        home_page.click_profile()
        profile_page.logout()