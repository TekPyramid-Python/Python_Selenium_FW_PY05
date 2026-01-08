from pages.base_page import BasePage # Import the BasePage
from selenium.webdriver.common.by import By

class StorePage(BasePage): # Make LoginPage inherit from BasePage
    STORES_OPTION = (By.XPATH, '//span[text()="Stores"]')

    STORES_DROPDOWN=(By.XPATH,'//select[@id="location-select"]')

    def __init__(self, driver):
        # This calls the constructor of the BasePage to set up the driver, logger, etc.
        super().__init__(driver)

    def stores_option(self):
        """
        Performs a full login action using methods inherited from BasePage.
        """
        # self.logger.info(f"Attempting to log in with username: {username}")
        self.click(self.STORES_OPTION)
        self.click(self.STORES_DROPDOWN)
        self.select_by_text(self.STORES_DROPDOWN,"Jaipur")



