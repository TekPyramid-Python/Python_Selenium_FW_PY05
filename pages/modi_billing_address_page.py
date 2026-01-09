from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ModiBillingAddressPage(BasePage):
    edit_address=(By.XPATH,'//a[@class="edit"]')


    def modi_billing_address(self):
        self.click(self.edit_address)