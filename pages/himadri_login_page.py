from pages.base_page import BasePage

class HimadriLoginPage(BasePage):
    #locators for input field
    LOGIN_CLICK = ('id','menu-item-6603')
    EMAIL_FIELD = ('id','username')
    PASSWORD_INPUT = ('id','password')
    LOGIN_BUTTON = ('xpath','//button[@name="login"]')
    ERROR_MESSAGE_CONTAINER = ('xpath','//ul[@role="alert"]')
    ACCOUNT_PAGE_HEADER = ('xpath','//p[text()="arshalokanathan"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login(self, email, password):
        self.logger.info(f"Attempting to log in with email: {email}")
        self.click(self.LOGIN_CLICK)
        self.send_keys(self.EMAIL_FIELD, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_login_successful(self):
        return self.is_visible(self.ACCOUNT_PAGE_HEADER, timeout=5)

    def get_error_message(self):
        if self.is_visible(self.ERROR_MESSAGE_CONTAINER, timeout=5):
            return self.get_text(self.ERROR_MESSAGE_CONTAINER)
        return "No error message found."