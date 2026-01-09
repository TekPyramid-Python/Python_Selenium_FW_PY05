from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ModiEditAccountPage(BasePage):
    def is_account_details_page(self):
        return self.is_visible((By.ID, "password_current"))
    current_pwd=(By.XPATH,'//input[@id="password_current"]')
    new_pwd=(By.XPATH,'//input[@id="password_1"]')
    confirm_new_pwd=(By.XPATH,'//input[@id="password_2"]')
    submit=(By.XPATH,'//button[text()="Save changes"]')

    def modi_edit_account_page(self):
        self.send_keys(self.current_pwd,'8197375829')
        self.send_keys(self.new_pwd,'1234')
        self.send_keys(self.confirm_new_pwd,'1234')
        sleep(2)
        self.click(self.submit)

