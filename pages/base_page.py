"""
Base Page class containing common, reusable methods for all page objects.
This class is the foundation of the Page Object Model pattern.
"""

import allure
from select import select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import get_logger  # Import our central logger utility
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



class BasePage:
    """
    Base class for all page objects. Contains common methods that can be used
    across all page objects to maintain the DRY (Don't Repeat Yourself) principle.
    """

    def __init__(self, driver):
        """
        Initialize BasePage with the WebDriver instance and our central logger.
        """
        self.driver = driver
        # Explicit wait timeout can be configured here
        self.wait = WebDriverWait(driver, 20)
        # Use our central logger, already configured in conftest.py
        self.logger = get_logger()

    @allure.step("Clicking Element: {locator}")
    def click(self, locator):
        """
        Waits for an element to be clickable and then clicks it.
        Fails the test immediately if the element is not clickable within the timeout.
        """
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            self.logger.info(f"Successfully clicked element: {locator}")
        except TimeoutException:
            self.logger.error(f"Timeout: Element not clickable: {locator}")
            # Re-raise the exception to fail the test and trigger failure evidence capture
            raise

    @allure.step("Force clicking Element: {locator}")
    def force_click(self, locator):
            """
            JS click to bypass overlays / sticky headers
            """
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", element
            )
            self.driver.execute_script("arguments[0].click();", element)
            self.logger.info(f"Force clicked element: {locator}")

    @allure.step("Entering text '{text}' into Element: {locator}")

    def send_keys(self, locator, text, clear_first=True):
        """
        Sends keys to an element after waiting for it to be visible.
        Fails the test immediately if the element is not found within the timeout.
        """
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            if clear_first:
                element.clear()
            element.send_keys(text)
            self.logger.info(f"Successfully entered text into element: {locator}")
        except TimeoutException:
            self.logger.error(f"Timeout: Element not visible for text entry: {locator}")
            raise

    @allure.step("Checking if Element is visible: {locator}")
    def is_visible(self, locator, timeout=15):
        """
        Checks if an element is visible on the page within a given timeout.
        Returns True or False. Does not fail the test.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            self.logger.info(f"Element is visible: {locator}")
            return True
        except TimeoutException:
            self.logger.info(f"Element is not visible within {timeout}s: {locator}")
            return False

    @allure.step("Getting text from Element: {locator}")
    def get_text(self, locator):
        """
        Gets text from an element. Fails test if element not found.
        """
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            text = element.text
            self.logger.info(f"Retrieved text '{text}' from element: {locator}")
            return text
        except TimeoutException:
            self.logger.error(f"Timeout: Could not get text from element as it was not visible: {locator}")
            raise

    @allure.step("Getting page title")
    def get_title(self):
        """Gets the title of the current page."""
        title = self.driver.title
        self.logger.info(f"Current page title: {title}")
        return title

    @allure.step("Navigating to URL: {url}")
    def navigate_to(self, url):
        """Navigates to a specific URL."""
        try:
            self.driver.get(url)
            self.logger.info(f"Successfully navigated to: {url}")
        except Exception as e:
            self.logger.error(f"Failed to navigate to {url}. Error: {e}")
            raise

    @allure.step("Navigating to URL: {url}")
    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    @allure.step("Checking if Element is present in DOM: {locator}")
    def is_present(self, locator, timeout=15):
            """
            Wait until element is present in the DOM (does not need to be visible).
            Returns True if element is present, False if timeout occurs.
            """
            try:
                WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(locator)
                )
                self.logger.info(f"Element is present in DOM: {locator}")
                return True
            except TimeoutException:
                self.logger.info(f"Element not present in DOM within {timeout}s: {locator}")
                return False

    @allure.step("Opening URL: {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Finding element: {locator}")
    def find(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Element_Not_Found",
                attachment_type=allure.attachment_type.PNG
            )
            raise
    @allure.step("Clicking element: {locator}")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Typing text '{text}' into element: {locator}")
    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Getting text from element: {locator}")
    def get_text(self, locator):
        return self.find(locator).text

    @allure.step("Checking if element is displayed: {locator}")
    def is_displayed(self, locator):
        try:
            return self.find(locator).is_displayed()
        except:
            return False

    @allure.step("Selecting '{text}' from dropdown: {locator}")
    def select_by_visible_text(self, locator, text):
            dropdown = Select(self.find(locator))
            dropdown.select_by_visible_text(text)

    @allure.step("Selecting value '{value}' from dropdown: {locator}")
    def select_by_value(self, locator, value):
            dropdown = Select(self.find(locator))
            dropdown.select_by_value(value)

    @allure.step("Selecting index '{index}' from dropdown: {locator}")
    def select_by_index(self, locator, index):
            dropdown = Select(self.find(locator))
            dropdown.select_by_index(index)

    @allure.step("Getting selected option from dropdown: {locator}")
    def get_selected_option(self, locator):
            dropdown = Select(self.find(locator))
            return dropdown.first_selected_option.text

    @allure.step("Selecting '{option_text}' from custom dropdown")
    def select_custom_dropdown(self, dropdown_locator, option_locator):
        self.click(dropdown_locator)
        self.click(option_locator)



    def scroll_to_element(self, locator):
            element = self.driver.find_element(*locator)
            self.driver.execute_script(
          "arguments[0].scrollIntoView({block: 'center'});", element)





