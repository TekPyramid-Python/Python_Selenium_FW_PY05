from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from pages.base_page import BasePage # Import the BasePage

class Signup_Page(BasePage):
   SIGNUP_ICON=(By.CSS_SELECTOR,"div.header__icons.header__icons--end.flex.justify-end.z-2>div>:nth-child(2)>svg")
   G_SIGNUP=(By.CSS_SELECTOR,".social-login-button")
   MAILID=(By.XPATH,"(//input[@class='whsOnd zHQkBf'])[1]")

   NEXT=(By.XPATH,"(//button[@jsname='LgbsSe'])[2]")
   PASS=(By.XPATH,'//input[@type="password"]')
   ANOTHERACC=(By.XPATH,'//div[.="Use another account"]')
   CART=(By.CSS_SELECTOR,"div.header__icons.header__icons--end.flex.justify-end.z-2>div>:nth-child(3)")
   search=(By.XPATH,"(//a[@aria-controls='SearchDrawer'])[2]")
   searchinp=(By.XPATH,'(//div[@class="search__field field flex items-center gap-4 relative"])[1]/input')
   searchallproduct=(By.XPATH,"//a[.='Shop All Products']")
   ALREADY_SIGNED_IN = (By.XPATH, "//div[@class='_15amvvq4 _15amvvq3 _1fragemn2 _1fragemq1 _1fragem2s']")


   def __init__(self, driver):
       # This calls the constructor of the BasePage to set up the driver, logger, etc.
       super().__init__(driver)

   def signup(self):
       """
       Performs a full login action using methods inherited from BasePage.
       """
       self.logger.info(f"Attempting to log in")
       self.click(self.SIGNUP_ICON)

       sleep(6)

   def switch_to_window(self):
        try:
            parent_window = self.driver.current_window_handle
            all_windows = self.driver.window_handles
            print(all_windows)

            for window in all_windows:
                if window != parent_window:
                    self.driver.switch_to.window(window)
                    break

        except Exception as e:
               self.logger.error(f"Error switching to child window: {e}")
               raise

   def siginthroughgoogle(self):
       self.click(self.G_SIGNUP)
       sleep(4)
       # self.click(self.ANOTHERACC)


   def entermail(self):
       sleep(20)
       self.send_keys(self.MAILID,"varshitharc@gmail.com")
       sleep(6)
       self.click(self.NEXT)
       sleep(4)
       self.send_keys(self.PASS, "appuvaru@25")
       sleep(15)
       self.click(self.NEXT)
       sleep(5)

   def select_cart(self):
       self.click(self.CART)

   def search_product(self):
       self.click(self.search)
       sleep(6)
       # self.click(self.searchinp)
       # self.send_keys(self.searchinp,"mats")
       self.click(self.searchallproduct)



