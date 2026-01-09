# pages/mywishlist_page.py
import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage # Import the BasePage
from selenium.webdriver.support import expected_conditions as EC


class MyWishlistPage(BasePage): # Make MyWishlistPage inherit from BasePage
    """
    Page Object for the total.coffee.com MyWishlistPage.
    """
    # --- Element Locators for total.coffee.com ---
    SELECTION_1= (By.XPATH, '(//li/div[@class="nm-product-buttons"])[1]')


    def click_select_option(self):
        self.is_visible(self.SELECTION_1)
        self.click(self.SELECTION_1)




