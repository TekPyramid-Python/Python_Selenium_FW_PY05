from pages.base_page import BasePage # Import the BasePage
from selenium.webdriver.common.by import By

class FooterEllePage(BasePage): # Make LoginPage inherit from BasePage
    # Elle_Logo = (By.XPATH,'(//a[@class="header__heading-link focus-inset"])[1]')
    CONTACT_US = (By.XPATH, '//span[text()="Contact Us"]')
    Logo=(By.XPATH,"//span[text()='Offers']")


    def __init__(self, driver):
        # This calls the constructor of the BasePage to set up the driver, logger, etc.
        super().__init__(driver)

    def footer_click(self):
        """
        Performs a full login action using methods inherited from BasePage.
        """
        # self.logger.info(f"Attempting to log in with username: {username}")
        self.scroll_to_element(self.CONTACT_US)
        self.click(self.CONTACT_US)

    def is_login_successful(self):
        """a
        Checks if login was successful by looking for an element on the inventory page.
        Uses the is_visible method inherited from BasePage.
        """
        return self.is_visible(self.Logo, timeout=5)

