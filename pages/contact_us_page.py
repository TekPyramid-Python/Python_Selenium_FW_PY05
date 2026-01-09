# pages/contact_us_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class ContactUsPage(BasePage):
    PAGE_TITLE = (By.XPATH, "//h1[contains(text(),'Contact Us')]")
    FIRST_NAME_INPUT =   ("xpath", "//input[@name='first_name']")
    LAST_NAME_INPUT = (By.XPATH, "//label[contains(text(),'Last Name')]/following::input[1]")
    EMAIL_INPUT =  ("xpath", "//input[@name='email']")
    MESSAGE_INPUT =  (By.XPATH, "//textarea[@name='message']")
    SUBMIT_BUTTON =  ("xpath", "//button[text()='Submit']")
    COUNTRY_DROPDOWN = (By.XPATH, "//label[contains(text(),'Country')]/following::select[1]")
    HELP_ON_DROPDOWN = (By.XPATH, "//label[contains(text(),'Help On')]/following::select[1]")
    HEARD_FROM_DROPDOWN = (By.XPATH, "//label[contains(text(),'Heard From')]/following::select[1]")


    def __init__(self, driver):
        super().__init__(driver)

    def is_page_loaded(self):
        return self.is_visible(self.PAGE_TITLE)


    def select_dropdown_by_text(self, locator, text):
        element = self.driver.find_element(*locator)
        Select(element).select_by_visible_text(text)


    def get_dropdown_options(self, locator):
        element = self.driver.find_element(*locator)
        return [option.text for option in Select(element).options]


    def fill_text_field(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)
    def submit_form(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def is_contact_us_page_successful(self):
        pass
