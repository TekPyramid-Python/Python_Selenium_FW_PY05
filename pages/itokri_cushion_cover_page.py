# pages/itokri_cushion_cover_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage # Import the BasePage

class ItokriHomePage(BasePage):
    """
        Page Object for the itokri cushion cover page (itokri.com/collections/cushion-covers-online).
        """
    # --- Element Locators for itokri.com/collections/cushion-covers-online ---
    MADHUBANI=(By.XPATH,"//span[contains(text(),'Madhubani')]")