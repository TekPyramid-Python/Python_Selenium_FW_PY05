from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..pages.base_page import BasePage # Import the BasePage

class Cart(BasePage):

   Prod=(By.XPATH,"(//button[@class='rebuy-button'])[16]")
   increaseqty=(By.XPATH,"(//button[@class='rebuy-cart__flyout-item-quantity-widget-button'])[2]")
   coupon=(By.ID,"rebuy-cart__discount-input")
   apply=(By.XPATH,"(//button[@class='rebuy-button'])[18]")

   checkout=(By.XPATH,'//button[@class="rebuy-button rebuy-cart__checkout-button block"]')
   def add_to_cart(self):
      self.scroll_to_element(self.Prod)
      self.click(self.Prod)

   def increase_qty(self):
       self.scroll_to_element(self.increaseqty)
       self.click(self.increaseqty)

   def add_coupon(self):
       self.scroll_to_element(self.apply)

       self.send_keys(self.coupon,"save5")
       self.click(self.apply)

   def check_out(self):
       self.scroll_to_element(self.checkout)
       self.click(self.checkout)


