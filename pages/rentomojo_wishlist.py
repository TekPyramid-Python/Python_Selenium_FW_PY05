from ..pages.base_page import BasePage
import allure
from time import sleep

class Rentomojo_Wishlist(BasePage):
    WISHLIST_OPTION = ("css selector", "ul.nav-arrow.rm-user__loggedIn>li:nth-child(2)")
    PROFILE_ICON=("css selector","a.rm-user__fullName")

    PROD_LOCATION=("css selector",'div.rm-listicle__block div div.swiper-wrapper div:nth-child(1) a')
    EXPECTED_PRODUCT_NAME=("css selector","h1.rm-product-title")
    ACTUAL_PRODUCT_NAME=("css selector","div.rm-card__product div:nth-child(2) h2") #after adding to wishlist
    WISHLIST_BTN=("css selector","div.rm-product__wishlist>div")
    LOGIN_BUTTON = ("css selector", "button.rm-login__btn")
    PHONE_FIELD = ("css selector", "div.rm-auth__user-input>div>input")
    CONTINUE_BTN = ("css selector", "form.rm-auth__form>div:nth-child(2)>button")
    LOGOUT_BTN = ("css selector", "ul.nav-arrow.rm-user__loggedIn>li:nth-child(4) a")
    CLEAR_WISHLIST_BTN=("css selector","div.rm-wishlist__container>div>div>div>div>div>div")

    def get_expected_product_name(self,product_=None):
        with allure.step("adding product to wishlist and getting expected product name."):
            self.scroll_to_element(self.PROD_LOCATION)
            self.click(self.PROD_LOCATION)
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[1])
            self.wait_till_pageload()
            expected_prodname=self.get_text(self.EXPECTED_PRODUCT_NAME)
            return expected_prodname

    def get_actual_product_name(self):
        with allure.step("verifying that product is successfully added to wishlist by getting actual name."):
            self.click(self.WISHLIST_BTN)
            self.wait_till_pageload()
            self.hover_over_element(self.PROFILE_ICON)
            sleep(10)
            self.click(self.WISHLIST_OPTION)
            self.wait_till_pageload()
            actual_prodname = self.get_text(self.ACTUAL_PRODUCT_NAME)
            return actual_prodname

    def clear_wishlist(self):
            self.hover_over_element(self.PROFILE_ICON)
            sleep(5)
            self.click(self.WISHLIST_OPTION)
            self.wait_till_pageload()
            wishlist_products=self.driver.find_elements(*self.CLEAR_WISHLIST_BTN)
            for i in wishlist_products:
                self.click(i)


