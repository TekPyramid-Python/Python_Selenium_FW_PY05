from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.utsav_methods_page import UtsavMethodPage

class UtsavProductList(UtsavMethodPage):

        PRODUCT_COLOR=(By.XPATH,'//span[text()="Purple"]')
        PRODUCT_TYPE = (By.XPATH, '(//span[text()="Woven Saree"])[2]')
        PRODUCT_NAME = (By.XPATH, '(//div[@class="product-top"])[1]')
        PRODUCT_NAME_TEXT=(By.XPATH,'(//a[@class="product-item-link"])[1]')
        PRODUCT_SIZE = (By.XPATH, '//span[text()="30"]')
        WISHLIST_BUTTON=(By.XPATH,'(//button[@data-title="Add to Wish List"])[1]')

        def select_color(self):
            self.click(self.PRODUCT_COLOR)

        def select_type(self):
            self.click(self.PRODUCT_TYPE)

        def select_product(self):
            self.click(self.PRODUCT_NAME)

        def add_to_wishlist(self):
            self.click(self.WISHLIST_BUTTON)

        def get_product_name(self):
            return self.get_text(self.PRODUCT_NAME_TEXT)

        def click_on_size(self):
            self.click(self.PRODUCT_SIZE)

        def get_product_color(self):
            return self.get_text(self.PRODUCT_COLOR)







