# pages/coffee_home_page.py
import time
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



from pages.base_page import BasePage # Import the BasePage

class HomePage(BasePage): # Make LoginPage inherit from BasePage
    """
    Page Object for the total.coffee.com login page.
    """
    # --- Element Locators for total.coffee.com ---
    LOGO = (By.XPATH,'//a[@href="https://total.coffee/"]')
    LOGIN_ICON= (By.ID,'nm-menu-account-btn')
    USERNAME_INPUT = (By.XPATH, '//input[@id="username"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@name="login"]')
    SEARCH_ICON= (By.ID,'nm-menu-search-btn')
    SEARCH_TEXT_BAR= (By.ID, 'nm-header-search-input')
    WISHLIST_ICON= (By.XPATH,'//li/a[@href="https://total.coffee/wishlist/"]')
    CART_ICON= (By.ID,'nm-menu-cart-btn')
    GREEN_COFFEE_CATEGORY = (By.ID,'menu-item-1301')
    ROASTED_COFFEE_CATEGORY = (By.ID,'menu-item-1315')
    QUICK_COFFEE_CATEGORY = (By.ID,'menu-item-5557')
    EQUIPMENTS_CATEGORY = (By.ID,'menu-item-1323')
    BRANDS_CATEGORY= (By.ID,'menu-item-3318')
    BLOGS = (By.ID, 'menu-item-9085')
    COFFEE_SUBSCRIPTION = (By.ID, 'menu-item-10191')
    PRODUCT1 = (By.XPATH, '//div[@class="nm-shop-loop-product-wrap"]')
    VENDOR_REGISTRATION = (By.XPATH,'//a[@title="Vendor Registration"]')

    def __init__(self, driver):
        # This calls the constructor of the BasePage to set up the driver, logger, etc.
        super().__init__(driver)

    def login(self,username,password):
        time.sleep(5)
        self.click(self.LOGIN_ICON)
        self.send_keys(self.USERNAME_INPUT,username)
        self.send_keys(self.PASSWORD_INPUT,password)
        sleep(3)
        self.click(self.LOGIN_BUTTON)

    def click_search(self):
        """Navigates to Searching the product"""
        self.click(self.SEARCH_ICON)
        return True

    def search_product(self,product):
        self.send_keys(self.SEARCH_TEXT_BAR, product + Keys.ENTER)
        return True

    def scroll_till_vendor_option(self):
        time.sleep(2)
        self.scroll_to_element(self.VENDOR_REGISTRATION)

    def click_vendor_registration(self):
        """Navigates to vendor registration page"""
        time.sleep(2)
        self.click(self.VENDOR_REGISTRATION)

    def click_coffee_subscription(self):
        """Navigates to coffee subscription page"""
        time.sleep(2)
        self.click(self.COFFEE_SUBSCRIPTION)

    def click_wishlist_icon(self):
        """Navigates to Wishlist page"""
        self.is_visible(self.WISHLIST_ICON)
        self.click(self.WISHLIST_ICON)
        time.sleep(3)






