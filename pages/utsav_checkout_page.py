from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import re
from pages.utsav_methods_page import UtsavMethodPage

class UtsavCheckout(UtsavMethodPage):

    # QUANTITY_INPUT=(By.ID,"cart-26692040-qty")
    QUANTITY_INPUT=(By.XPATH,'(//select[@title="Qty"])[1]')
    INDIVIDUAL_PRICE=(By.XPATH,'(//span[@class="price"])[2]')
    ITEM_PRICE=(By.XPATH,'(//span[@class="price"])[5]')

    TOTAL_PRICE=(By.XPATH,'//span[@class="price totalyoupay"]')
    CHECKOUT_BUTTON=(By.XPATH,'//span[text()="Proceed to Checkout"]')

    def scroll_to_checkout(self):
        self.scroll_to_element(self.CHECKOUT_BUTTON)

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    # def click_to_quantity(self):
    #     self.click(self.QUANTITY_INPUT)

    # def select_quantity(self,QUANTITY_INPUT,text):
    #     self.select_by_visible_text(text)

    def get_unit_price(self):
        price_text = self.get_text(self.INDIVIDUAL_PRICE)
        return int(re.sub(r"[^\d]", "", price_text))
    #
    # def quality_input_click(self):
    #     self.click(self.QUANTITY_INPUT)

    # def select_quantity(self):
    #     self.select_by_visible_text(self.QUANTITY_INPUT, 3)

    def get_total_price(self):
        price_text = self.get_text(self.ITEM_PRICE)
        return int(re.sub(r"[^\d]", "", price_text))


    def scroll_to_total_price(self):
        self.scroll_to_element(self.TOTAL_PRICE)

    def get_total_price1(self):
        price_text =self.get_text(self. TOTAL_PRICE)
        return price_text





