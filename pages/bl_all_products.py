from time import sleep

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from ..pages.base_page import BasePage # Import the BasePage

class All_Products(BasePage):
   ITEM=(By.XPATH,"(//button[@aria-label='Add to cart'])[1]")
   clicksort=(By.XPATH,"//facet-sort[@class='sort-wrapper relative']")
   bestselling=(By.XPATH,"//label[.='Best selling']")
   SORT=(By.XPATH,"//select[@name='sort_by']")


   def add_product(self):
       self.scroll_to_element(self.ITEM)
       sleep(6)
       self.driver.execute_script("window.scrollBy(0, -500);")
       product_hover = self.wait_for_element(self.ITEM)
       ActionChains(self.driver).move_to_element(product_hover).perform()
       sleep(3)
       self.click(self.ITEM)

   def sort(self):
       # Select(self.wait_for_element(self.SORT)).select_by_visible_text("Best selling")
       self.click(self.clicksort)
       # self.scroll_to_element(self.bestselling)
       self.driver.execute_script("window.scrollBy(0, 200);")

       sleep(6)
       self.click(self.bestselling)




