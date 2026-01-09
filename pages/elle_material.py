from pages.base_page import BasePage # Import the BasePage
from selenium.webdriver.common.by import By

class MaterialFilter(BasePage): # Make LoginPage inherit from BasePage
    slider = (By.XPATH, '(//button[@class="slick-prev slick-arrow"])[1]')


    def __init__(self, driver):
        # This calls the constructor of the BasePage to set up the driver, logger, etc.
        super().__init__(driver)

    def material_click(self, search_prod,upi_id):
        """
        Performs a full login action using methods inherited from BasePage.
        """
        # self.logger.info(f"Attempting to log in with username: {username}")
        self.click(self.slider)


