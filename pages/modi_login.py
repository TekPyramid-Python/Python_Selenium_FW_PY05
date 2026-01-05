from pages.base_page import BasePage
from selenium.webdriver.common.by import By
class ModiLoginPage(BasePage):


        Username=(By.ID,'username')
        Password=(By.XPATH,'//input[@id="password"]')
        Login_button=(By.XPATH,'//button[@name="login"]')

        INVENTORY_PAGE_HEADER = (By.CLASS_NAME, "app_logo")  # Element on the page after successful login
        LOGO=(By.CSS_SELECTOR,"img[src$='Modi-Naturals-Logo.png']")

        def __init__(self,driver):
            super().__init__(driver)

        def login(self, username, password):

            self.logger.info(f"Attempting to log in with username: {username}")
            self.send_keys(self.Username, username)
            self.send_keys(self.Password, password)
            self.click(self.Login_button)

        def is_login_successful(self):
            return self.is_visible(self.LOGO, timeout=5)