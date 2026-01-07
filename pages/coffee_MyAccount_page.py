# pages/login_page.py
from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import BasePage # Import the BasePage

class LoginPage(BasePage): # Make LoginPage inherit from BasePage
    """
    Page Object for the total.coffee.com login page.
    """
    # --- Element Locators for total.coffee.com ---
    LOGO = (By.XPATH, '//a[@href="https://total.coffee/"]')
    LOGIN_ICON = (By.ID, 'nm-menu-account-btn')
    USERNAME_INPUT = (By.XPATH, '//input[@id="username"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@name="login"]') # Element on the page after successful login
    HELLO_USER = (By.XPATH, '//span[@class="nm-username"]')

    def __init__(self, driver):
        # This calls the constructor of the BasePage to set up the driver, logger, etc.
        super().__init__(driver)

    def login(self,username,password):
        self.click(self.LOGIN_ICON)
        self.send_keys(self.USERNAME_INPUT,username)
        self.send_keys(self.PASSWORD_INPUT,password)
        sleep(3)
        self.click(self.LOGIN_BUTTON)

    def is_login_successful(self):
        """
        Checks if login was successful by looking for an element on the inventory page.
        Uses the is_visible method inherited from BasePage.
        """
        return self.is_visible(self.HELLO_USER, timeout=10)
    #
    # def get_error_message(self):
    #     """Gets the text of the login error message."""
    #     if self.is_visible(self.ERROR_MESSAGE_CONTAINER, timeout=5):
    #         # Uses the get_text method inherited from BasePage
    #         return self.get_text(self.ERROR_MESSAGE_CONTAINER)
    #     return "No error message found."