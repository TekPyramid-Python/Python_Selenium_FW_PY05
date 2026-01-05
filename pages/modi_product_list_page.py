from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ModiProductListPage(BasePage):
    product=(By.XPATH, '(//a[@class="woocommerce-LoopProduct-link woocommerce-loop-product__link"])[2]')


    def modi_product_list_page(self):
        self.scroll_to_element(self.product)
        self.click(self.product)
        sleep(2)
