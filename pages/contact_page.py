from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium import webdriver

class ContactUsPage(BasePage):

    CONTACT_US_URL = "https://example.com/contact"


    PAGE_HEADER = (By.XPATH, "//h1[contains(text(),'Contact')]")
    FIRST_NAME = (By.ID, "firstName")
    EMAIL = (By.ID, "email")
    COUNTRY_DROPDOWN = (By.ID, "country")
    HELP_ON_DROPDOWN = (By.ID, "helpOn")
    MESSAGE = (By.ID, "message")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")

    def open_contact_us(self):
        self.driver.get(self.CONTACT_US_URL)

    def fill_contact_form(self, first, email, country, help_on, message):
        self.find(self.FIRST_NAME).send_keys(first)
        self.find(self.EMAIL).send_keys(email)
        self.select_by_visible_text(self.COUNTRY_DROPDOWN, country)
        self.select_by_visible_text(self.HELP_ON_DROPDOWN, help_on)

        self.find(self.MESSAGE).send_keys(message)

    def submit_form(self):
        self.find(self.SUBMIT_BUTTON).click()
