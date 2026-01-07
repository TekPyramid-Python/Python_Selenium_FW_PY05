from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PrivacyPolicyPage(BasePage):

    PAGE_TITLE = (By.XPATH, "//h1[contains(text(),'Privacy')]")

    def open(self, base_url):
        self.driver.get(base_url + "/privacy-policy")

    def is_page_loaded(self):
        return self.is_element_visible(self.PAGE_TITLE)
