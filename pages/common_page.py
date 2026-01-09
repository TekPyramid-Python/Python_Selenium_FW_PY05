from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CommonPage(BasePage):

    page_heading=("xpath", "//h1 | //h2")

    def __init__(self,driver):
        super().__init__(driver)

    def is_page_loaded(self):
        return self.is_visible(self.page_heading)

