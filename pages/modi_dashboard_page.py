from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ModiDashboardPage(BasePage):
    address_link=(By.XPATH,'//li[@class="woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--edit-address"]')
    account_details=(By.XPATH,'//li[@class="woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--customer-logout"]')
    logout=(By.XPATH,'//li[@class="woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--customer-logout"]')

    def modi_dashboard(self):
        self.click(self.address_link)

    # def nav_to_account_details(self):
    #     self.click(self.account_details)


    def nav_to_logout(self):
        self.click(self.logout)



