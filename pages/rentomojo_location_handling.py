from selenium.webdriver.common.keys import Keys

from .furniture_page import Furniture_Module
from ..pages.base_page import BasePage
from time import sleep
import allure
from ..config.environment import Environment

class LocationHandling(BasePage):
    PROD_LOCATION = ("css selector", 'div.rm-listicle__block div div:nth-child(1)')
    CART_BTN = ("css selector", "div.rm-section__flex-row>button")
    DELIVERY_PINCODE_BOX = ("css selector", "input.rm-pincode__input")
    DELIVERY_PINCODE_BTN = ("css selector", "button.rm-pincode__apply-btn")
    IFREAME_DIALOG_LOCATOR = ("css selector", "div#skip")
    AC_DIALOG_PROCEED_BTN = ("css selector", "div.rm-ac-rental__dialog>div.rm-dialog__footer>button.rm-button__proceed")
    AC_INSTALLATION_BTN = ("css selector", "div.rm-ac__container>div>button.rm-btn__red")
    INSTALLATION_EXTRAINFO_PROCEED_BTN = ("css selector", "div.rm-ac__popup-container>button")
    VIEW_CART_BTN = ("css selector", "div.rm-sticky__other-cta-btns>span:nth-child(2)>a")
    CHANGE_LOCATION=("css selector","span.tooltip.tooltip--bottom")
    SEARCH_BTN=("css selector","ul.rm-dropdown__city>li>ul>li>div>input")
    NEW_LOCATION=("css selector","li.rm-city__list-container>div>ul>li>a")
    LOCATION_TXT=("css selector","span.tooltip.tooltip--bottom span span")
    CHANGE_CITY_PROCEED_BTN=("css selector","div.rm-button__container button:nth-child(2)")


    def adding_product(self):
        self.selecting_product(self.PROD_LOCATION)
        self.switch_to_window(1)
        sleep(15)
        self.click(self.CART_BTN)
        try:
            self.send_keys(self.DELIVERY_PINCODE_BOX, "515005")
            self.click(self.DELIVERY_PINCODE_BTN)
        except Exception as e:
            self.logger.info("Delivery pincode not needed")
        try:
            self.click(self.AC_DIALOG_PROCEED_BTN)
            self.click(self.AC_INSTALLATION_BTN)
            self.click(self.INSTALLATION_EXTRAINFO_PROCEED_BTN)
        except Exception as e:
            self.logger.info("Dialog box is only for AC Products")
        self.click(self.VIEW_CART_BTN)
        sleep(15) #to check with eyes whether the product is added or not
        self.driver.close()

    def changing_location(self,location_='Hyderabad'):
        with allure.step("changing location from default city to desired city"):
            self.switch_to_window(0)
            self.wait_till_pageload()
            self.click(self.CHANGE_LOCATION)
            self.send_keys(self.SEARCH_BTN,location_)
            sleep(5)
            self.send_keys(self.SEARCH_BTN,Keys.ENTER)
            sleep(5)
            self.click(self.NEW_LOCATION)
            try:
                self.click(self.CHANGE_CITY_PROCEED_BTN)
            except Exception as e:
                self.logger.info("proceed button not present")
            sleep(5)
            self.logger.info(self.get_text(self.LOCATION_TXT))
            assert location_==self.get_text(self.LOCATION_TXT)
            self.logger.info("location successfully changed")
            sleep(10)



