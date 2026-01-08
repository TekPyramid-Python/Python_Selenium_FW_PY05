from pages.base_page import BasePage
from pages.dental_cart import Cart
from selenium.webdriver.common.by import By

class ProfilePage(Cart):
    logout_button=(By.XPATH,'//span[text()="Logout"]')
    logout_popup=(By.XPATH,'//div[text()="Logout"]')
    profile_full_name=(By.XPATH,"//input[@id='fullname']")
    profile_button=(By.XPATH,"//span[normalize-space()='Profile']")
    edit_profile=(By.XPATH,"//button[@class='text-blue-600 hover:text-blue-800 flex items-center gap-1']//*[name()='svg']")

    def __init__(self,driver):
        super().__init__(driver)

    def logout(self):
        self.scroll_to_element(self.logout_button)
        self.click(self.logout_button)
        self.click(self.logout_popup)

    def full_name_change(self,name):
        self.click(self.profile_button)
        self.click(self.edit_profile)
        self.is_visible(self.profile_full_name)
        self.send_keys(self.profile_full_name,name,True)

