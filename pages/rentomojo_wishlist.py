from ..pages.base_page import BasePage
import allure
from ..config.environment import Environment
from time import sleep

class Rentomojo_Wishlist(BasePage):
    WISHLIST_OPTION = ("css selector", "ul.nav-arrow.rm-user__loggedIn>li:nth-child(2)")
    PROFILE_ICON=("css selector","a.rm-user__fullName")
    PROD_LOCATION=("css selector",'div.rm-listicle__block div div:nth-child(1)')
    EXPECTED_PRODUCT_NAME=("css selector","h1.rm-product-title")
    ACTUAL_PRODUCT_NAME=("css selector","div.rm-card__product div:nth-child(2) h2") #after adding to wishlist
    WISHLIST_BTN=("css selector","div.rm-product__wishlist>div")
    LOGIN_BUTTON = ("css selector", "button.rm-login__btn")
    PHONE_FIELD = ("css selector", "div.rm-auth__user-input>div>input")
    CONTINUE_BTN = ("css selector", "form.rm-auth__form>div:nth-child(2)>button")
    LOGOUT_BTN = ("css selector", "ul.nav-arrow.rm-user__loggedIn>li:nth-child(4) a")
    CLEAR_WISHLIST_BTN=("css selector","div.rm-wishlist__container>div>div>div>div>div>div")

    def add_to_wishlist(self,product_=None):
        with allure.step("adding product to wishlist"):
            env = Environment()
            base_url = env.get_base_url()
            self.navigate_to(base_url)
            self.wait_till_pageload()
            sleep(10)
            self.click(self.PROD_LOCATION)
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[1])
            self.wait_till_pageload()
            expected_prodname=self.get_text(self.EXPECTED_PRODUCT_NAME)
            self.click(self.WISHLIST_BTN)
        with allure.step("verifying that product is successfully added to wishlist"):
            self.wait_till_pageload()
            self.hover_over_element(self.PROFILE_ICON)
            sleep(10)
            self.click(self.WISHLIST_OPTION)
            self.wait_till_pageload()
            assert expected_prodname==self.get_text(self.ACTUAL_PRODUCT_NAME),"product not added to wishlist"
            print("product successfully added to wishlist")

    def clear_wishlist(self):
        with allure.step("clearing wishlist"):
            self.hover_over_element(self.PROFILE_ICON)
            # sleep(5)
            self.click(self.WISHLIST_OPTION)
            self.wait_till_pageload()
            wishlist_products=self.driver.find_elements(*self.CLEAR_WISHLIST_BTN)
            for i in wishlist_products:
                self.click(i)


