from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    email_id=(By.ID,"phone")
    password=(By.ID,"password")
    continue_button=(By.XPATH,'//button[@label="Continue"]')
    email_button=(By.XPATH,'//div[text()="Login with Email"]')
    password_button=(By.XPATH,'//div[text()="Use Password"]')

    def __init__(self,driver):
        super().__init__(driver)

    def login(self,email,passw):
        self.logger.info(f"Attempting to log in with email: {email}")
        self.click(self.email_button)
        self.send_keys(self.email_id,email)
        self.click(self.password_button)
        self.is_visible(self.password)
        self.send_keys(self.password,passw)
        self.click(self.continue_button)




