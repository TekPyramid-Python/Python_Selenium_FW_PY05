from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ModiEditBillingPage(BasePage):
    last_name=(By.XPATH,'//input[@id="billing_last_name"]')
    save_button=(By.XPATH,'//button[text()="Save address"]')


    def modi_edit_billing(self):
        self.send_keys(self.last_name,'Goudru')
        sleep(2)
        self.click_save_button(self.save_button)
