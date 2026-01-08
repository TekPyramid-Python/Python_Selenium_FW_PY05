from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MedicinePage(BasePage):

    AYURVEDA_LINK=(By.XPATH,"//a[contains(.,'Ayurveda')]")
    SELECT_CATEGORY = (By.XPATH, "//a[contains(.,'Proteins')]")
    SELECT_SUB_CATEGORY = (By.XPATH, "//a[.='Multivitamins']")
    SELECT_PRODUCT = (By.XPATH, "(//div[@class='card-body'])[2]")


    def on_click_ayurveda(self):
        self.logger.info("Navigate to medicine list page")
        self.click(self.AYURVEDA_LINK)

    def select_category(self):
        self.click(self.SELECT_CATEGORY)
        self.click(self.SELECT_SUB_CATEGORY)

    def select_product(self):
        self.click(self.SELECT_PRODUCT)
