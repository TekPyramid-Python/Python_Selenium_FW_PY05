from pages.base_page import BasePage # Import the BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class DropDown(BasePage): # Make LoginPage inherit from BasePage



    def __init__(self, driver):
        # This calls the constructor of the BasePage to set up the driver, logger, etc.
        super().__init__(driver)


    KITCHENWARE = (
        By.XPATH,
        '(//a[contains(@class,"header__menu-item")])[1]'
    )

    TABLEWARE = (
        By.XPATH,
        '(//a[contains(@class,"header__menu-item")])[2]'
    )

    SERVEWARE = (
        By.XPATH,
        '(//a[contains(@class,"header__menu-item")])[3]'
    )
    def hover_on_serveware(self):
        """
        Performs a full login action using methods inherited from BasePage.
        """
        # self.logger.info(f"Attempting to log in with username: {username}")

        self.hover(self.KITCHENWARE)
        self.hover(self.SERVEWARE)
        self.hover(self.TABLEWARE)






