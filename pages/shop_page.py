from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ShopPage(BasePage):

    SHOP_MENU = (By.XPATH, "//a[contains(text(),'Shop')]")
    LIGHTING_CATEGORY = (By.XPATH, "//a[contains(text(),'Lighting')]")
    FURNITURE_CATEGORY = (By.XPATH, "//a[contains(text(),'Furniture')]")

    PRODUCTS = (By.XPATH, "//div[contains(@class,'product')]")

    def open_shop(self):
        self.wait.until(EC.element_to_be_clickable(self.SHOP_MENU))
        self.click(self.SHOP_MENU)

    def open_lighting(self):
        self.wait.until(EC.element_to_be_clickable(self.LIGHTING_CATEGORY))
        self.click(self.LIGHTING_CATEGORY)

    def open_furniture(self):
        self.wait.until(EC.element_to_be_clickable(self.FURNITURE_CATEGORY))
        self.click(self.FURNITURE_CATEGORY)

    def products_are_displayed(self):
        self.wait.until(EC.visibility_of_any_elements_located(self.PRODUCTS))
        return len(self.find_elements(self.PRODUCTS)) > 0

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ShopPage(BasePage):

    FIRST_PRODUCT = (By.CSS_SELECTOR, "a[href*='/products/']")
    VARIANT_OPTION = (By.CSS_SELECTOR, "input[type='radio'], select")
    ADD_TO_CART = (By.XPATH, "//button[.//span[contains(text(),'Add to cart')] or contains(text(),'Add to cart')]")

    def open_shop_all(self):
        self.driver.get("https://www.mianzi.in/collections/all")
        self.wait.until(EC.presence_of_element_located(self.FIRST_PRODUCT))

    def select_any_product(self):
        self.js_click(self.FIRST_PRODUCT)

    def select_variant_if_present(self):
        variants = self.driver.find_elements(*self.VARIANT_OPTION)
        if variants:
            try:
                self.js_click(variants[0])
            except:
                pass  # Some products may auto-select

    def add_product_to_cart(self):
        self.select_variant_if_present()
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART))
        self.js_click(self.ADD_TO_CART)





