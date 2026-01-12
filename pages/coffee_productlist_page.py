# pages/coffee_productlist_page.py
import time

from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

from pages.base_page import BasePage # Import the BasePage
from selenium.webdriver.common.action_chains import ActionChains


class ProductListPage(BasePage): # Make ProductListPage inherit from BasePage
    """
    Page Object for the total.coffee.com coffee_productlist_page.
    """
    # --- Element Locators for total.coffee.com ---
    LOGO = (By.XPATH, '//a[@href="https://total.coffee/"]')
    SEARCH_ICON = (By.ID, 'nm-menu-search-btn')
    PRODUCT1 = (By.XPATH, '(//div[@class="nm-shop-loop-product-wrap"])[1]')
    ELEMENT = (By.XPATH,'//a[contains(text(),"Red Honey – BeanSong")]')
    WISHLIST_1 = (By.ID, 'nm-wishlist-item-4774-button')


    def click_searched_product(self):
        self.click(self.PRODUCT1)
        return True

    def add_to_wishlist(self):

        self.hover_to_element(self.ELEMENT)
        self.wait_for_element(self.WISHLIST_1)
        time.sleep(3)
        self.click(self.WISHLIST_1)
        time.sleep(3)



