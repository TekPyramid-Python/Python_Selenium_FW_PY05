from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from pages.base_page import BasePage # Import the BasePage

class Signup_Page(BasePage):
   SIGNUP_ICON=(By.CSS_SELECTOR,"div.header__icons.header__icons--end.flex.justify-end.z-2>div>:nth-child(2)>svg")
   G_SIGNUP=(By.CSS_SELECTOR,".social-login-button")
   MAILID=(By.ID,"identifierId")
   NEXT=(By.XPATH,"//span[.='Next']")
   PASS=(By.XPATH,'//input[@type="password"]')
   ANOTHERACC=(By.XPATH,'//div[.="Use another account"]')
   CART=(By.CSS_SELECTOR,"div.header__icons.header__icons--end.flex.justify-end.z-2>div>:nth-child(3)")
   search=(By.XPATH,"(//a[@aria-controls='SearchDrawer'])[2]")
   searchinp=(By.XPATH,'(//div[@class="search__field field flex items-center gap-4 relative"])[1]/input')
   searchallproduct=(By.XPATH,"//a[.='Shop All Products']")


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
       # Note: We don't need to return True/False. If any step fails, an exception will be raised.

   # def is_login_successful(self):
   #     """
   #     Checks if login was successful by looking for an element on the inventory page.
   #     Uses the is_visible method inherited from BasePage.
   #     """
   #     return self.is_visible(self.INVENTORY_PAGE_HEADER, timeout=5)
   #
   # def get_error_message(self):
   #     """Gets the text of the login error message."""
   #     if self.is_visible(self.ERROR_MESSAGE_CONTAINER, timeout=5):
   #         # Uses the get_text method inherited from BasePage
   #         return self.get_text(self.ERROR_MESSAGE_CONTAINER)
   #     return "No error message found."

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
       self.click(self.ANOTHERACC)


   def entermail(self):
       self.send_keys(self.MAILID,"varshitharc@gmail.com")
       sleep(6)
       self.click(self.NEXT)
       sleep(4)
       self.send_keys(self.PASS, "appuvaru@25")
       sleep(4)
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



