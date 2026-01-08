
from pages.base_page import BasePage
class HomePage(BasePage):
    profile = ('xpath', '//a[@class="header__icon header__icon--account link link--text"])[2]')
    phone = ('css selector', '[name="sa_phone_no"]')

    def click_profile(self):
        self.click(*self.profile)

    def enter_phone(self, phone):
        self.send_keys(phone)


