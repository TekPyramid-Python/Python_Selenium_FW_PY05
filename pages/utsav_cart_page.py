from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.utsav_methods_page import UtsavMethodPage

class UtsavWishlist(UtsavMethodPage):

    VIEW_BAG=(By.XPATH,'// button[text() = "View bag"]')
    CONTINUE_SHOPPING=(By.XPATH,"(//a[text()='Continue Shopping'])[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_view_page(self):
        self.click(self.VIEW_BAG)

    def click_on_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING)