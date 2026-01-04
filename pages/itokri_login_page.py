# pages/itokri_login_page.py
import random
from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import BasePage # Import the BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
class ItokriLoginPage(BasePage):
    """
        Page Object for the itokri login page (itokri.com).
        """
    # --- Element Locators for itokri.com ---
    LOGIN_WITH_EMAIL = (By.XPATH, "//span[contains(text(), 'Login with email & password')]")
    CREATE_ACC = (By.XPATH, "//a[contains(text(),'Create account')]")
    EMAIL=(By.ID,"CustomerEmail")
    PASSWORD=(By.ID,"CustomerPassword")
    SINGIN_BUTTON=(By.CSS_SELECTOR,"#customer_login button")

    def human_delay(self,min_sec=0.5, max_sec=2):
        """Add random delays to mimic human behavior"""
        sleep(random.uniform(min_sec, max_sec))
    def __init__(self, driver):
        # This calls the constructor of the BasePage to set up the driver, logger, etc.
        super().__init__(driver)
    def nav_create_acc_page(self):
        self.click(self.LOGIN_WITH_EMAIL)
        self.click(self.CREATE_ACC)
    def login(self,email,password):
        self.click(self.LOGIN_WITH_EMAIL)
        self.human_delay(1,2)
        for char in email:
            self.send_char(self.EMAIL,char)
            sleep(random.uniform(0.05, 0.15))
        self.human_delay(0.5, 2)
        for char in password:
            self.send_char(self.PASSWORD,char)
            sleep(random.uniform(0.05, 0.15))
        self.human_delay(0.1, 2)
        self.click(self.SINGIN_BUTTON)

        sleep(10)
