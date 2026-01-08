# pages/itokri_listof_new_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage # Import the BasePage

class ItokriListOfNewPage(BasePage):
    """
        Page Object for the itokri Ekdam Fresh page (itokri.com/collections/latest-collections-on-ekdum-fresh).
        """
    # --- Element Locators for itokri.com/collections/latest-collections-on-ekdum-fresh---
    # LATEST_DATE=(By.XPATH,"//section[@id='section8']/h2")
    LATEST_DATE=(By.XPATH,"//h2[@class='main_heading']")

    def get_latest_date(self):
        self.scroll_to_element(self.LATEST_DATE)
        return self.get_text(self.LATEST_DATE)

