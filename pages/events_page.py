from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage

class EventsPage(BasePage):
    EVENTS_SECTION = (By.XPATH, "//h1[contains(text(),'Event')]")

    def is_events_page_loaded(self):
        return "event" in self.driver.current_url.lower()

    def is_events_section_visible(self, timeout=20):
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.EVENTS_SECTION)
            )
            self.logger.info("Events section is visible")
            return True
        except TimeoutException:
            self.logger.error("Events section not visible")
            return False

    def scroll_and_verify_events_content(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.wait.until(
                EC.visibility_of_element_located(self.EVENTS_SECTION)
            )
            return True
        except TimeoutException:
            self.logger.error("Events content not displayed")
            return False

    def navigate_home(self):
        self.navigate_to("https://www.swasthyawarriors.com")

