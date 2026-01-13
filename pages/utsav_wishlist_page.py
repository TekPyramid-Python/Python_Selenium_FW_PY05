from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.utsav_methods_page import UtsavMethodPage

class UtsavWishlistPage(UtsavMethodPage):

    WISHLIST_PRODUCT = (By.XPATH, '(//a[@class="product-item-link"])[1]')

    def get_wishlist_product_name(self):
        return self.get_text(self.WISHLIST_PRODUCT)