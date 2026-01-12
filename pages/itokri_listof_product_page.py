# pages/itokri_listof_product_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage # Import the BasePage

class ItokriListOfProductPage(BasePage):
    """
        Page Object for the itokri create account page (itokri.com/collections/*).
        """
    # --- Element Locators for itokri.com/collections/*---
    TOTAL_COUNT=(By.XPATH,"(//div[@class='st-sidebar-content']//span)[3]")
    FIRST_PRODUCT=(By.XPATH,"(//div[@class='card__content'])[2]")
    PRODUCT_NAMES=(By.XPATH,"(//div[@class='media media--transparent media--hover-effect'])[1]")
    CART_ICON=(By.XPATH,"//a[@role='button']/div")
    VIEW_CART=(By.XPATH,"//a[@title='View Cart']")
    HOME_ICON=(By.XPATH,"//img[@class='header__heading-logo motion-reduce']")
    def get_total_count(self):
        return int(self.get_text(self.TOTAL_COUNT))

    def click_first_product(self):
        self.scroll_to_element(self.PRODUCT_NAMES)
        self.click(self.PRODUCT_NAMES)
    def get_first_product_name(self):
        return self.get_text()
    def click_on_cart(self):
        self.click(self.CART_ICON)
    def click_on_view_cart(self):
        self.click(self.VIEW_CART)
    def back_to_homepage(self):
        self.click(self.HOME_ICON)