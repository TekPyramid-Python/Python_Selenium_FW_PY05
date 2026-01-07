
from selenium.webdriver.common.by import By
from ..pages.base_page import BasePage

from selenium.webdriver.support.ui import Select
from datetime import datetime
import time

class MadeWithCopperPage(BasePage):
    INSTOCK = (By.XPATH, "//input[@id='sidebar-filter.v.availability']")
    PRODUCTTYPE=(By.XPATH,"(//span[.='Product type'])[2]")
    BOTTLENSIPPERS = (By.ID, "sidebar-filter.p.product_type-1")
    # COPPERBOTTLE=(By.ID,"(//div[@class='flickity-slider'])[2]")
    BUYIT=(By.XPATH,"//button[.='Buy it now']")


    def instockbutton(self):
        self.scroll_to_element(self.INSTOCK)
        self.click(self.INSTOCK)


    def filterproducttye(self):
        self.click(self.PRODUCTTYPE)

    def bottlensippers(self):
        self.click(self.BOTTLENSIPPERS)



