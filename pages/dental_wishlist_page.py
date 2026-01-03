from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.dental_cart import Cart
from time import sleep

class WishListPage(Cart):
    home_button=(By.XPATH,"//a[@aria-label='Go to homepage']//*[name()='svg']")
    def remove_all_items_if_present(self):
        sleep(3)
        self.click(self.driver.find_element(By.XPATH, "//div[@class='sc-55a2692a-8 dHNAjs']//span//*[name()='svg']"))
        self.click(self.driver.find_element(By.XPATH,"//p[normalize-space()='Delete']"))
        self.click(self.driver.find_element(By.XPATH,"//button[@class='sc-8235fce6-0 dNZNQZ sc-7c2e7391-1 iTFhOu']"))

    def click_home_button(self):
        self.click(self.home_button)