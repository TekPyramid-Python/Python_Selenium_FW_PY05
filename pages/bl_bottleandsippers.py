from time import sleep, time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from ..pages.base_page import BasePage


class BottleAndSippers(BasePage):
     COPPERBOTTLE = (By.CSS_SELECTOR, ".media.media--height.w-full.h-full.overflow-hidden.flickity-cell.is-selected")
     BUYIT = (By.XPATH, "//button[.='Buy it now']")

     def select_product(self):
         self.click(self.COPPERBOTTLE)

     def buyit(self):
         self.scroll_to_elementbuyit(self.BUYIT)
         self.is_visible(self.BUYIT)
         self.wait_for_element(self.BUYIT)
         self.click(self.BUYIT)

     def scroll_to_elementbuyit(self, locator, timeout=10, retries=3):
         for _ in range(retries):
             try:
                 element = WebDriverWait(self.driver, timeout).until(
                     EC.presence_of_element_located(locator)
                 )
                 self.driver.execute_script(
                     "arguments[0].scrollIntoView({block:'center'});",
                     element
                 )
                 return element
             except StaleElementReferenceException:

              raise Exception(f"Element always stale: {locator}")