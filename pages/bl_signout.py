from time import sleep

from selenium.webdriver.common.by import By
from ..pages.base_page import BasePage # Import the BasePage

class SignOut(BasePage):
    SIGNOUTDD=(By.XPATH,"//button[@aria-label='Show Account menu']")
    SIGNOUT=(By.XPATH,"//span[.='Sign out']")

    def signout(self):
        self.click(self.SIGNOUTDD)
        self.click(self.SIGNOUT)
