# pages/coffee_cart_page.py
import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage # Import the BasePage

class CoffeeCartPage(BasePage): # Make CoffeeCartPage inherit from BasePage
    """
    Page Object for the total.coffee.com coffee_product_page.
    """
    # --- Element Locators for total.coffee.com ---
    CHECKOUT_BTN = (By.XPATH, '//div/a[contains(text(),"Proceed to checkout")]')
    CART_TEXT = (By.XPATH,'(//a[contains(text(),"Coffee Subscription")])[2]')



    def proceed_to_checkout(self):
        self.scroll_to_element(self.CHECKOUT_BTN)
        self.wait_for_element(self.CHECKOUT_BTN)
        self.click(self.CHECKOUT_BTN)

        return True
