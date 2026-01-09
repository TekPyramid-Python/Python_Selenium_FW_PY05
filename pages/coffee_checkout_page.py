# pages/coffee_checkout_page.py
import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage # Import the BasePage
from pages.coffee_home_page import HomePage

class CheckoutPage(BasePage): # Make CheckoutPage inherit from BasePage
    """
    Page Object for the total.coffee.com coffee_product_page.
    """
    # --- Element Locators for total.coffee.com ---
    FIRST_NAME = (By.ID, 'billing_first_name')
    LAST_NAME = (By.ID, 'billing_last_name')
    COMPANY_NAME = (By.ID, 'billing_company')
    ADDRESS_1 = (By.ID,'billing_address_1')
    ADDRESS_2 = (By.ID, 'billing_address_2')
    CITY = (By.ID,'billing_city')
    STATE = (By.ID, 'select2-billing_state-result-wk4o-KA')
    PINCODE = (By.ID, 'billing_postcode')
    PHONE = (By.ID, 'billing_phone')
    EMAIL = (By.ID, 'billing_email')
    DELIVER_ADDRESS_checkbox = (By.ID,'ship-to-different-address-checkbox')
    CART_ICON = (By.ID, 'nm-menu-cart-btn')
    PAY_NOW = (By.ID,'place_order')
    payment =(By.XPATH,'(//div[contains(text(),"Total coffee")])[1]')
    TITLE='Checkout - Total.Coffee'
    def billing_details(self):
        self.send_keys(self.FIRST_NAME,"Plimpton")
        self.send_keys(self.LAST_NAME, "Tharcis")
        self.send_keys(self.COMPANY_NAME, "Oregano")
        self.send_keys(self.ADDRESS_1, "2nd floor door no:210 pen park")
        self.send_keys(self.ADDRESS_2, "K.R Pura near Tin factory ")
        self.send_keys(self.CITY, "Bangalore")
        self.send_keys(self.PINCODE, "560016")
        self.send_keys(self.PHONE, "9080811905")
        self.click(self.DELIVER_ADDRESS_checkbox)
        time.sleep(3)
        self.click(self.PAY_NOW)
        time.sleep(30)


