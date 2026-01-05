from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage # Import the BasePage

class Address(BasePage):

   default=(By.XPATH,"//div[@class='_1mmswk96 _1mmswk95 _1fragemn2 _1fragempb']")
   fn = (By.XPATH, '//input[@placeholder="First name"]')
   ln = (By.XPATH, '//input[@placeholder="Last name"]')

   addr=(By.XPATH,'//input[@placeholder="Address"]')

   zip=(By.XPATH,"//input[@placeholder='PIN code']")
   save=(By.XPATH,"//button[@aria-label='Save address']")

   def add_address(self):
       self.click(self.default)

   def add_fn_ln(self):
       self.send_keys(self.fn,"V")
       self.send_keys(self.ln,"R")

   def address(self):
       self.send_keys(self.addr,"RR Nagar")

   def zipcode(self):
       self.send_keys(self.zip,"744101")

   def save_add(self):
       self.click(self.save)

