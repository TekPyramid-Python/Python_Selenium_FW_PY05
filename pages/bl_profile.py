from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


from pages.base_page import BasePage

import time

class Profile(BasePage):
    add=(By.XPATH,"//button[@aria-label='Add address']")

    def add_address(self):
        self.click(self.add)
