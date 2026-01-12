# pages/login_page.py

from pages.base_page import BasePage # Import the BasePage
from selenium.webdriver.common.by import By

class LoginEllePage(BasePage): # Make LoginPage inherit from BasePage
    """
    Page Object for the Sauce Labs Demo login page (saucedemo.com).
    """
    # --- Element Locators for saucedemo.com ---
    Click_Profile = (By.XPATH,"//span[text()='Profile']")
    CreateAccount = (By.XPATH, '(//a[@href="/account/register"])[1]')
    Firstname = (By.CSS_SELECTOR, 'input#RegisterForm-FirstName')
    Lastname = (By.CSS_SELECTOR, 'input#RegisterForm-LastName')
    Mail = (By.CSS_SELECTOR, 'input#RegisterForm-email')
    Phone = (By.CSS_SELECTOR, 'input[name="customer[phone]"]')
    Password = (By.CSS_SELECTOR, 'input#RegisterForm-password')
    Create_Account_button = (By.CSS_SELECTOR, 'input[value="Create An Account"]')
    Logo=(By.XPATH,"//span[text()='Offers']")

    def __init__(self, driver):
        # This calls the constructor of the BasePage to set up the driver, logger, etc.
        super().__init__(driver)

    def login(self, firstname,lastname,mail,phone,password):
        """
        Performs a full login action using methods inherited from BasePage.
        """
        # self.logger.info(f"Attempting to log in with username: {username}")
        self.click(self.Click_Profile)
        self.click(self.CreateAccount)
        self.send_keys(self.Firstname, firstname)
        self.send_keys(self.Lastname, lastname)
        self.send_keys(self.Mail, mail)
        self.send_keys(self.Phone, phone)
        self.send_keys(self.Password, password)
        self.click(self.Create_Account_button)

        # Note: We don't need to return True/False. If any step fails, an exception will be raised.

    def is_login_successful(self):
        """a
        Checks if login was successful by looking for an element on the inventory page.
        Uses the is_visible method inherited from BasePage.
        """
        return self.is_visible(self.Logo, timeout=5)
