from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_PAGE_VERIFICATION_TEXT = ('xpath', '//div[text()="Login"]')
    EMAIL = ('xpath', '(//input[@type="text"])[1]')
    PASSWORD = ('id', 'password')
    LOGIN_BUTTON = ('xpath', '(//button[@type="button"])[1]')
    LEAD_PAGE_HEADER = ('xpath', '//p[text()="Lead Management"]')

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.logger.info(f"Attempting to log in with username: {username}")

        # If already logged in, skip login
        if self.is_visible(self.LEAD_PAGE_HEADER, timeout=5):
            self.logger.info("User already logged in. Skipping login.")
            return

        self.logger.info("User not logged in. Proceeding with login.")

        # Now perform login
        self.send_keys(self.EMAIL, username)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

        # Verify login succeeded
        assert self.is_visible(self.LEAD_PAGE_HEADER, timeout=10), "Login failed"

    def is_login_successful(self):
        return self.is_visible(self.LEAD_PAGE_HEADER, timeout=10)

