from ..pages.base_page import BasePage
from ..config.environment import Environment
import allure
from time import sleep




class Rentomojo_OtpLogin(BasePage):
        LOGIN_BUTTON = ("css selector", "button.rm-login__btn")
        PHONE_FIELD = ("css selector", "div.rm-auth__user-input>div>input")
        CONTINUE_BTN = ("css selector", "form.rm-auth__form>div:nth-child(2)>button")
        PROFILE_ICON = ("css selector", "a.rm-user__fullName")
        LOGOUT_BTN = ("css selector", "ul.nav-arrow.rm-user__loggedIn>li:nth-child(4)")

        def test_rentopmojo_login(self):
                env = Environment()
                base_url = env.get_base_url()
                with allure.step("Navigating to url"):
                        print(base_url)
                        self.navigate_to(base_url)
                        self.wait_till_pageload()
                self.click(self.LOGIN_BUTTON)
                self.send_keys(self.PHONE_FIELD, 8431926335)
                self.click(self.CONTINUE_BTN)

        def test_rentomojo_logout(self):
                env = Environment()
                base_url = env.get_base_url()
                with allure.step("Navigating to url"):
                        print(base_url)
                        self.navigate_to(base_url)
                self.hover_over_element(self.PROFILE_ICON)
                sleep(5)
                self.click(self.LOGOUT_BTN)
                sleep(5)