import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class VanalayaMethods(BasePage):


    @allure.step("Scrolling to element: {locator}")
    def scroll_to_elements(self, locator):
        """Scrolls until the element is visible in viewport."""
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                element
            )
            self.logger.info(f"Scrolled to element: {locator}")
            return element
        except Exception as e:
            self.logger.error(f"Failed to scroll to element {locator}. Error: {e}")
            raise

    @allure.step("Select element by value: {value}")
    def select_dropdown_by_value(self, locator, value):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        Select(element).select_by_value(value)

    def upload_file(self, locator, file_path):
        self.driver.find_element(*locator).send_keys(file_path)

    def wait_for_dom_ready(self, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def wait_and_click(self, locator, timeout=30):
        wait = WebDriverWait(self.driver, timeout, poll_frequency=0.5)
        wait.until(lambda d: d.find_element(*locator).is_enabled())
        self.driver.find_element(*locator).click()


    @allure.step("Scroll to end of page")
    def scroll_to_end(self, timeout=30):
        """
        Scrolls to bottom using WebDriverWait instead of sleep.
        """
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        def page_height_changed(driver):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            new_height = driver.execute_script("return document.body.scrollHeight")
            return new_height != last_height

        try:
            WebDriverWait(self.driver, timeout).until(page_height_changed)
        except:
            pass
