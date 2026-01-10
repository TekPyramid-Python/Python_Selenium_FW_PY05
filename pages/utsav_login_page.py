from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.utsav_methods_page import UtsavMethodPage

class UtsavLogin(UtsavMethodPage):

    EMAIL_TEXT = (By.XPATH, '(//input[@name="username"])[1]')
    PASSWORD_INPUT = (By.XPATH, '(//input[@name="password"])[1]')
    SUBMIT_BUTTON = (By.XPATH, '(//button[@type="submit"])[3]')

    ACCOUNT = (By.XPATH, "(//a[text()='Account'])[2]")
    ACCOUNT_DASHBOARD=(By.XPATH,"(//a[text()='Account Dashboard'])")
    BOX_CONTENT=(By.XPATH,'(//div[@class="box-content"])[1]')
    LOGIN_BUTTON=(By.XPATH,"//a[text() = 'Login']")

    def __init__(self, driver):
        # This calls the constructor of the BasePage to set up the driver, logger, etc.
        super().__init__(driver)

    def login(self, username, password):
        """
        Performs a full login action using methods inherited from BasePage.
        """
        self.logger.info(f"Attempting to log in with username: {username}")
        self.send_keys(self.EMAIL_TEXT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def mouse_hover_to_account(self):
        self.mouse_hover(self.ACCOUNT)

    def click_on_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_email_text(self):
        return self.get_text(self.EMAIL_TEXT)

    def click_on_account_dashboard(self):
        self.click(self.ACCOUNT_DASHBOARD)

    def get_box_content(self):
        return self.get_text(self.BOX_CONTENT)

