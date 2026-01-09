# pages/terms_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class TermsPage(BasePage):

    PAGE_HEADER = (By.XPATH, "//h1[contains(text(),'Terms')]")
    HOME_LOGO = (By.XPATH, "//a[contains(@href,'/')]")  # Home logo in header/footer

    def is_page_loaded(self):
        return self.is_element_visible(self.PAGE_HEADER)

    def is_content_visible(self):
        body = self.wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "body"))
        )
        return len(body.text.strip()) > 50

    def click_home_logo(self):
        self.force_click(self.HOME_LOGO)
