from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CoachesPage(BasePage):

    COACHES_HEADER = (By.XPATH, "//h1[contains(text(),'Coach')]")
    LINKEDIN_ICON = (By.XPATH, "//a[contains(@href,'linkedin.com')]")
    TERMS_LINK = (By.XPATH, "//a[normalize-space()='Terms of Use']")

    def is_page_loaded(self):
        return self.is_element_visible(self.COACHES_HEADER)

    def is_coaches_page_loaded(self):
        return self.is_element_visible(self.COACHES_HEADER, timeout=30)

    def is_content_visible(self):
        body = self.wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "body"))
        )
        return len(body.text.strip()) > 50

    def open_linkedin_profile(self):
        linkedin_element = self.wait.until(
            EC.element_to_be_clickable(self.LINKEDIN_ICON)
        )
        url = linkedin_element.get_attribute("href")
        if not url:
            raise Exception("LinkedIn URL not found")
        self.driver.execute_script(f"window.open('{url}', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def is_linkedin_opened(self):
        return "linkedin.com" in self.driver.current_url.lower()

    def click_terms_of_use(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.force_click(self.TERMS_LINK)
