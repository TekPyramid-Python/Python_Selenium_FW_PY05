# pages/itokri_login_page.py
from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import BasePage # Import the BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
class ItokriLoginPage(BasePage):
    """
        Page Object for the itokri login page (itokri.com).
        """
    # --- Element Locators for itokri.com ---
    LOGIN_WITH_EMAIL = (By.XPATH, "//span[text()='Login with email & password']")
    CREATE_ACC = (By.XPATH, "//a[contains(text(),'Create account')]")
    EMAIL=(By.ID,"CustomerEmail")
    PASSWORD=(By.ID,"CustomerPassword")
    SINGIN_BUTTON=(By.CSS_SELECTOR,"form#customer_login button")
    def __init__(self, driver):
        # This calls the constructor of the BasePage to set up the driver, logger, etc.
        super().__init__(driver)
    def nav_create_acc_page(self):
        # self.scroll_to_element(self.LOGIN_WITH_EMAIL)
        # assert self.is_visible(self.LOGIN_WITH_EMAIL)
        self.click(self.LOGIN_WITH_EMAIL)
        self.click(self.CREATE_ACC)
    def login(self,email,password):
        self.click(self.LOGIN_WITH_EMAIL)
        self.send_keys( self.EMAIL,email)
        self.send_keys(self.PASSWORD,password)
        # ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        button=self.driver.find_element(By.CSS_SELECTOR,"form#customer_login button")
        self.driver.execute_script("""
        const rect = arguments[0].getBoundingClientRect();
        const x = rect.left + rect.width / 2;
        const y = rect.top + rect.height / 2;

        document.elementFromPoint(x, y).click();
        """, button)
        # action=ActionChains(self.driver)
        # loc = button.location
        # size = button.size
        #
        # x = loc['x'] + size['width'] / 2
        # y = loc['y'] + size['height'] / 2
        # action.move_to_element_with_offset(loc,x,y).click().perform()
        # self.driver.execute_script("arguments[0].scrollIntoView(true);",loc)
        # self.driver.execute_script("""var r = arguments[0].getBoundingClientRect();document.elementFromPoint(r.left + r.width/2,r.top + r.height/2).click();""", loc)
        # action.move_to_element_with_offset(loc,loc.location['x'],loc.location['y']).click().perform()
        sleep(10)
        # self.driver.execute_script("arguments[0].click();", self.SINGIN_BUTTON)
        # self.submit_form(self.SINGIN_BUTTON)
        # self.submit_form(self.SINGIN_BUTTON)
        # button=self.driver.find_element(By.XPATH,"//form[@id='customer_login']//button")
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});",button)
        # self.click(self.SINGIN_BUTTON)
