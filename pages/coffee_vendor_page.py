# pages/coffee_vendor_page.py
import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage # Import the BasePage
from utils.dropdown_utils import DropdownUtils
from selenium.webdriver.support.ui import Select

class VendorRegistrationPage(BasePage): # Make VendorRegistrationPage inherit from BasePage
    """
    Page Object for the total.coffee.com coffee_vendor_page.
    """
    # --- Element Locators for total.coffee.com ---
    LOGO = (By.XPATH, '//a[@href="https://total.coffee/"]')
    REG_EMAIL= (By.ID, 'user_email')
    REG_FIRST_NAME = (By.ID, 'first_name')
    REG_LAST_NAME = (By.ID, 'last_name')
    REG_ADD1 = (By.ID, 'addr_1')
    REG_ADD2 = (By.ID, 'addr_2')
    REG_CITY = (By.ID, 'city')
    REG_POSTCODE = (By.ID, 'zip')
    REG_PHONE = (By.ID, 'phone')
    REG_PASS = (By.ID, 'passoword')
    REG_CONFIRM_PASS = (By.ID, 'confirm_pwd')
    REG_BTN = (By.ID, 'wcfm_membership_register_button')
    REG_TITLE ='Vendor Registration - Total.Coffee'
    state_name="Karnataka"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    REG_STATE = (By.ID, "state")

    def select_state(self, state_name):
        dropdown_element = self.driver.find_element(*self.REG_STATE)
        DropdownUtils.select_by_visible_text(dropdown_element, state_name)

    def get_selected_state(self):
        dropdown_element = self.driver.find_element(*self.REG_STATE)
        return Select(dropdown_element).first_selected_option.text

    def fill_vendor_registration(self):
        """
        Fills out the vendor registration form.
        user_data: a dictionary containing form values
        """

        # Filling text fields
        self.send_keys(self.REG_EMAIL, 'plimpton8@gmail.com')
        self.send_keys(self.REG_FIRST_NAME,'Plimpton')
        self.send_keys(self.REG_LAST_NAME,'Tharcis')
        self.send_keys(self.REG_ADD1,'3,3rd cross street subramani layout')
        self.send_keys(self.REG_ADD2,'ramamoorthy nager ')
        self.send_keys(self.REG_CITY,'Bangalore')
        self.send_keys(self.REG_POSTCODE,'560016')
        self.send_keys(self.REG_PHONE,'9080811905')
        self.send_keys(self.REG_PASS,'Zaccheo@99')
        self.send_keys(self.REG_CONFIRM_PASS,'Zaccheo@99')
        time.sleep(3)
        self.click(self.REG_BTN)
        time.sleep(10)


