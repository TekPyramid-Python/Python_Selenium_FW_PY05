# pages/itokri_create_account_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage # Import the BasePage

class ItokriCreateAccountPage(BasePage):
    """
        Page Object for the itokri create account page (itokri.com/account/register).
        """
    # --- Element Locators for itokri.com/account/register ---
    FIRST_NAME=(By.ID,"RegisterForm-FirstName")
    LAST_NAME=(By.ID,"RegisterForm-LastName")
    EMAIL=(By.ID,"RegisterForm-email")
    PASSWORD=(By.ID,"RegisterForm-password")
    PHONE=(By.ID,"RegisterForm-Phone")
    CREATE_BUTTON=(By.XPATH,"//span[@class='flitsCreateButton']")
    PAGE_TITLE=(By.TAG_NAME,"title")
    def __init__(self, driver):
        # This calls the constructor of the BasePage to set up the driver, logger, etc.
        super().__init__(driver)
    def create_account(self,firstname,lastname,email,password,phone):
        self.send_keys(self.FIRST_NAME,firstname)
        self.send_keys(self.LAST_NAME,lastname)
        self.send_keys(self.EMAIL,email)
        self.send_keys(self.PASSWORD,password)
        self.send_keys(self.PHONE,phone)
        self.click(self.CREATE_BUTTON)
    def is_create_account_visible(self):
        """Verifies if the login page is displayed by checking for the title."""
        if self.is_visible(self.PAGE_TITLE):
            return "Create Account" in self.get_title()
        return False
    def is_home_page_visible(self):
        """Verifies if the login page is displayed by checking for the title."""
        if self.is_visible(self.PAGE_TITLE):
            return "Create Account" in self.get_title()
        return False