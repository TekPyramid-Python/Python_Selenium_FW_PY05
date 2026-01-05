from time import sleep

import allure

from config.environment import Environment
from pages.bl_accounts import Accounts
from pages.bl_address import Address
from pages.bl_cart import Cart
from pages.bl_profile import Profile
from pages.bl_reviewpage import Review
from pages.bl_signup_page import Signup_Page
from tests.base_test import BaseTest


class Test_Add_Address(BaseTest):

    def test_add_address(self):
        signin = Signup_Page(self.driver)
        env = Environment()
        base_url = env.get_base_url()

        with allure.step("Navigate and sign in in child window"):
            signin.navigate_to(base_url)
            # time.sleep(3)
        with allure.step("clicking on sign in"):
            signin.signup()
            signin.switch_to_window()

        acct = Accounts(self.driver)
        acct.selct_menu()
        acct.click_on_profile()
        # sleep(18)
        prof=Profile(self.driver)
        prof.add_address()
        # sleep(18)
        addr=Address(self.driver)
        addr.add_address()

        addr.add_fn_ln()

        addr.address()
        addr.zipcode()
        # sleep(18)
        addr.save_add()
        sleep(18)




