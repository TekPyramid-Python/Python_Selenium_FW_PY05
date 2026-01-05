from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ModiProductPage(BasePage):
    drop_down = (By.ID, 'pa_new-variation')
    size = (By.XPATH, '//select[@id="pa_new-variation"]/child::option[text()="500ml Pet Bottle"]')
    cart_button = (By.XPATH, '//button[text()="Add to cart"]')


    def modi_product_page(self):
        self.select_by_visible_text(self.drop_down)
        self.click(self.size)
        self.click(self.cart_button)
        sleep(3)