from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.utsav_methods_page import UtsavMethodPage

class UtsavProductPage(UtsavMethodPage):

    PRODUCT_SIZE=(By.XPATH,'//span[@data-standardsizeoptid="38"]')
    ADD_TO_SHOPPING_BAG=(By.XPATH,'//span[text()="Add to Shopping Bag"]')
    WISHLIST=(By.XPATH,'//button[@data-title="Add to  Wishlist"]')


    def select_size(self):
        self.click(self.PRODUCT_SIZE)

    def scroll_to_shopping_bag(self):
        self.scroll_to_element(self.ADD_TO_SHOPPING_BAG)

    def add_to_shopping_bag(self):
        self.click(self.ADD_TO_SHOPPING_BAG)



