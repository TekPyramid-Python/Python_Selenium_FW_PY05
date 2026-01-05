from ..pages.rentomojo_login_otp import Rentomojo_OtpLogin
from ..tests.base_test import BaseTest
import allure
from time import sleep

class Test_Rentomojo_Login(BaseTest):

    def test_rentomojo_user_auth(self):
        login_page = Rentomojo_OtpLogin(self.driver)
        login_page.test_rentopmojo_login()
        # login_page.test_rentopmojo_logout()



