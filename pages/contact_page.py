from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactPage(BasePage):
    CONTACT_CLICK = (By.CSS_SELECTOR,'div.col-10>ul li.nav-item.dropdown:nth-child(5)')
    ENTER_NAME = (By.XPATH,'//input[@placeholder="Name"]')
    ENTER_EMAIL = (By.XPATH,'//input[@placeholder="Email"]')
    ENTER_PHONE = (By.XPATH,'//input[@placeholder=" Phone/Mobile"]')
    ENTER_DEPARTMENT = (By.XPATH,'//input[@placeholder="Department"]')
    ENTER_QUERIES = (By.XPATH,'//textarea[@placeholder="Enter Your Queries"]')
    SCROLL_TO_SUBMIT = (By.ID,'contact-form-block-button_JTgfjB')
    CLICK_SUBMIT = (By.ID,'contact-form-block-button_JTgfjB')
    CONTACT_TITLE = (By.CSS_SELECTOR,'div.col-10>ul li.nav-item.dropdown:nth-child(5)')



    def __init__(self,driver):
        super().__init__(driver)

    def click_contact_button(self):
        self.click(self.CONTACT_CLICK)
        self.logger.info("Clicked the Contact button.")

    def enter_details(self, name, email, phone, department, queries):
        self.js_send_keys(self.ENTER_NAME,name)
        self.logger.info(f"Entered the Email ID:{name}")

        self.js_send_keys(self.ENTER_EMAIL, email)
        self.logger.info(f"Entered the Email ID:{email}")

        self.js_send_keys(self.ENTER_PHONE, phone)
        self.logger.info(f"Entered the Email ID:{phone}")

        self.js_send_keys(self.ENTER_DEPARTMENT, department)
        self.logger.info(f"Entered the Department:{department}")

        self.js_send_keys(self.ENTER_QUERIES, queries)
        self.logger.info(f"Entered the Email Queries:{queries}")

    def scroll_to_submit(self):
        self.scroll_to_element(self.SCROLL_TO_SUBMIT)
        self.logger.info("Scroll to bottom of the Submit button")

    def click_submit(self):
        self.click(self.CLICK_SUBMIT)
        self.logger.info("Clicked the Submit button.")


    def is_query_successful(self):
        return self.is_visible(self.CONTACT_TITLE, timeout=5)




