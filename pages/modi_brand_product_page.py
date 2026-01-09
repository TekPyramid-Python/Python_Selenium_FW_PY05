from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
class ModiBrandProductPage(BasePage):
    button=(By.XPATH,'//button[text()="Add to cart"]')

    def modi_brand_product(self):
        self.click(self.button)