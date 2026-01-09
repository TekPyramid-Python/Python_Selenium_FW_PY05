import time
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class LeadCreationPage(BasePage):
    CREATE_LEAD_BUTTON = ('xpath', '(//button[@type="button"])[2]')
    LEAD_FORM_HEADER = ('xpath', '(//span[text()="Create Lead"])[2]')
    SITE_ADDRESS = ('xpath', '//input[@placeholder="Enter Site Address"]')
    LEAD_NAME = ('xpath', '//input[@placeholder="Enter Lead Full Name"]')
    LEAD_EMAIL = ('xpath', '//input[@placeholder="Enter Lead Email ID"]')
    SITE_TYPE = ('name', "el-id-4462-212")
    CREATE_BUTTON = ('xpath', '//span[text()=" Create "]')

    def __init__(self, driver):
        super().__init__(driver)

    def open_lead_creation_page(self):
        self.click(self.CREATE_LEAD_BUTTON)

    def fill_and_submit_lead(self, site_address, lead_name, lead_email):
        self.logger.info("Attempting to create lead page.")
        self.send_keys(self.SITE_ADDRESS, site_address)
        time.sleep(1)
        self.send_keys(self.SITE_ADDRESS, Keys.ARROW_DOWN)
        self.send_keys(self.SITE_ADDRESS, Keys.ENTER)
        self.is_visible(self.LEAD_NAME, timeout=2)
        self.send_keys(self.LEAD_NAME, lead_name)
        self.send_keys(self.LEAD_EMAIL, lead_email)
        self.is_visible(self.CREATE_BUTTON, timeout=10)
        self.click(self.CREATE_BUTTON)

    def is_lead_creation_page_opening_successful(self):
        return self.is_visible(self.LEAD_FORM_HEADER, timeout=10)









