from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
class ModiBillingPage(BasePage):
    billing_fn = (By.XPATH, '//input[@id="billing_first_name"]')
    billing_ln = (By.XPATH, '//input[@id="billing_last_name"]')
    billing_addr = (By.XPATH, '//input[@id="billing_address_1"]')
    billing_city = (By.XPATH, '//input[@id="billing_city"]')
    # billing_state = (By.ID, 'select2-billing_state-container')

    # billing_search = (By.XPATH, '//input[@class="select2-search__field"]')
    pincode = (By.XPATH, '//input[@id="billing_postcode"]')
    phone = (By.XPATH, '//input[@id="billing_phone"]')
    email = (By.XPATH, '//input[@id="billing_email"]')
    place_order = (By.ID, 'place_order')


    def modi_billing_page(self):
        self.send_keys(self.billing_fn, 'Asha')
        self.send_keys(self.billing_ln, 'Akkund')
        self.send_keys(self.billing_addr, 'chilakavad houseno 121')
        sleep(2)
        action_obj=ActionChains(self.driver)

        self.send_keys(self.billing_city, 'Chilakavad')
        # self.click(self.billing_state)
        # self.send_keys(self.billing_state, 'Karnataka')
        # action_obj.send_keys(Keys.ENTER).perform()
        self.send_keys(self.pincode, '582208')
        self.send_keys(self.email, 'ashagudisagar30@gmail.com')
        self.send_keys(self.phone, '8197375829')
        sleep(2)
        self.click(self.place_order)
        sleep(3)
