from selenium.webdriver.common.by import By
from pages.vanalaya_methods_page import VanalayaMethods

class ProductPage(VanalayaMethods):

    CLICK_CART = (By.XPATH,'((//div[@class="col-4"])[2]/ul/li)[5]')
    CLICK_PRODUCT = (By.XPATH,"(//a[contains(text(),'A2 Pure Buffalo Ghee – Traditional Bilona Made')])[1]")
    CLICK_ADD_TO_CART = (By.XPATH,"//span[contains(text(),'Add to cart')]")
    CLICK_CHECKOUT = (By.XPATH,"//form[@id='cart_form']")
    HEADER_CONTACT = (By.XPATH,'//h2[@id="header"]')

    def __init__(self,driver):
        super().__init__(driver)

    def click_cart_button(self):
        self.click(self.CLICK_CART)
        self.logger.info("Clicked the Cart button.")

    def click_product_button(self):
        self.click(self.CLICK_PRODUCT)
        self.logger.info("Clicked the Product button.")

    def scroll_to_add_to_cart_button(self):
        self.scroll_to_elements(self.CLICK_ADD_TO_CART)
        self.logger.info("Scroll to Add To Cart button.")

    def click_add_to_cart_button(self):
        self.click(self.CLICK_ADD_TO_CART)
        self.logger.info("Clicked the Add To Cart button.")

    def click_checkout_button(self):
        self.click(self.CLICK_CHECKOUT)
        self.logger.info("Clicked the Checkout button.")

    def is_payment_page_open_successful(self):
        return self.is_visible(self.HEADER_CONTACT, timeout=5)




