# pages/coffee_product_page.py
import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage # Import the BasePage

class ProductPage(BasePage): # Make ProductPage inherit from BasePage
    """
    Page Object for the total.coffee.com coffee_product_page.
    """
    # --- Element Locators for total.coffee.com ---
    SIZE = (By.XPATH, "(//li[@class='nm-variation-option'])[1]")
    ADD_TO_BASKET = (By.XPATH, '//button[contains(text(),"Add to basket")]')
    VIEW_BASKET = (By.XPATH, '(//a[text()="View basket"])[2]')
    CLOSE_BUTTON = (By.XPATH,'//span/i[@class="nm-font-close2"]')
    CART_ICON = (By.ID, 'nm-menu-cart-btn')

    def add_to_basket(self):

        self.click(self.ADD_TO_BASKET)
        time.sleep(3)
        self.click(self.CLOSE_BUTTON)
        self.click(self.CART_ICON)
        self.wait_for_element(self.VIEW_BASKET,50)
        time.sleep(5)
        self.click(self.VIEW_BASKET)
        time.sleep(5)
        return True

    def add_to_wishlist_basket(self):
        self.click(self.SIZE)
        time.sleep(3)
        self.click(self.ADD_TO_BASKET)
        time.sleep(3)
        self.click(self.CLOSE_BUTTON)
        self.click(self.CART_ICON)
        self.wait_for_element(self.VIEW_BASKET, 50)
        time.sleep(5)
        self.click(self.VIEW_BASKET)
        time.sleep(5)
        return True