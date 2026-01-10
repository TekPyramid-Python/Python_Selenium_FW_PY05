import allure
from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import get_logger  # Import our central logger utility
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class UtsavMethodPage(BasePage):
    """
    Base class for all page objects. Contains common methods that can be used
    across all page objects to maintain the DRY (Don't Repeat Yourself) principle.
    """

    def __init__(self, driver):
        """
        Initialize BasePage with the WebDriver instance and our central logger.
        """
        super().__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        # Use our central logger, already configured in conftest.py
        self.logger = get_logger()
        #Action Chains
        self.actions = ActionChains(self.driver)

    @allure.step("Mouse Hover to element")
    def mouse_hover(self, locator):
        """
        Generic method to mouse hover on an element
        :param locator: tuple (By.XPATH, "//xpath")
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.actions.move_to_element(element).perform()

    @allure.step("scroll to element")
    def scroll_to_element(self, locator, timeout=20):
        """
        Scrolls to element with custom timeout
        :param locator: tuple (By.XPATH, "//xpath")
        :param timeout: max wait time in seconds
        """
        try:
            wait1 = WebDriverWait(self.driver, timeout)
            element = wait1.until(EC.presence_of_element_located(locator))
            sleep(0.5)
            self.driver.execute_script("arguments[0].scrollIntoView();",element)


        except TimeoutException:
            raise Exception(f"Element not found within {timeout} seconds: {locator}")

