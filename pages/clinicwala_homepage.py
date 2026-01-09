from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    SERVICES_LINK= (By.XPATH,"//a[contains(.,'SERVICES')]")
    ECLINIC_LINK= (By.XPATH,"//a[contains(.,'E-CLINIC')]")
    FOOD_DIET_LINK= (By.XPATH,"(//a[contains(.,'FOOD')])[2]")
    FIND_CURE_LINK= (By.XPATH,"//a[contains(.,'FIND CURE')]")
    ABOUT_LINK = (By.XPATH,"//a[contains(.,'ABOUT')]")
    LOGIN_LINK = (By.XPATH,"//span[contains(.,'LOGIN')]")
    DOCTOR_APPOINTMENT_LINK = (By.XPATH,"//a[@href='/doctor/consult.html']")
    PATHOLOGY_LINK = (By.XPATH,"//a[@href='https://www.janchwala.com']")
    MEDICINE_LINK = (By.XPATH,"//a[@href='https://www.dawaiwala.com']")
    DIET_PLAN_LINK=(By.XPATH,"(//a[.='DIET PLANS'])[2]")
    HOME_REMEDY_LINK=(By.XPATH,"//a[.='HOME REMEDIES']")

    def __init__(self, driver):
        # This calls the constructor of the BasePage to set up the driver, logger, etc.
        super().__init__(driver)

    def on_click_book_appointment(self):
      self.logger.info(f"Attempting to book doctor appointment")
      self.click(self.DOCTOR_APPOINTMENT_LINK)


    def on_click_book_test(self):
      self.logger.info(f"Attempting to book pathology lab test")
      # self.click(self.PATHOLOGY_LINK)
      current_window = self.driver.current_window_handle
      self.click(self.PATHOLOGY_LINK)

      # Wait until a new window opens
      self.wait.until(lambda d: len(d.window_handles) > 1)

      # Switch to the new window
      for window in self.driver.window_handles:
          if window != current_window:
              self.driver.switch_to.window(window)
              self.logger.info("Switched to janchwala.com window")
              break

    def on_click_foodndiet(self):
        self.logger.info("Click on Food and Diet")
        self.click(self.FOOD_DIET_LINK)
        self.click(self.DIET_PLAN_LINK)

    def on_click_find_cure(self):
        self.logger.info("Click on FindCure link")
        self.click(self.FIND_CURE_LINK)
        self.click(self.HOME_REMEDY_LINK)

    def on_click_book_medicines(self):
        self.logger.info("Attempting to book medicine")

        current_window = self.driver.current_window_handle
        self.click(self.MEDICINE_LINK)

        # Wait until a new window opens
        self.wait.until(lambda d: len(d.window_handles) > 1)

        # Switch to the new window
        for window in self.driver.window_handles:
            if window != current_window:
                self.driver.switch_to.window(window)
                self.logger.info("Switched to dawaiwala.com window")
                break




