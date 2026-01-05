import time

import pytest
import allure
from selenium.webdriver.common.by import By

from config.environment import Environment
from pages.bl_accounts import Accounts
from pages.bl_bottleandsippers import BottleAndSippers
from pages.bl_madewithcopperpage import MadeWithCopperPage
from pages.bl_signout import SignOut
from pages.bl_signup_page import Signup_Page
from tests.base_test import BaseTest


class TestSelectCopperBottle(BaseTest):
    # G_SIGNUP = (By.CSS_SELECTOR, ".social-login-button")

    def test_add_product_to_cart(self):
        signin = Signup_Page(self.driver)
        env = Environment()
        base_url = env.get_base_url()

        with allure.step("Navigate and sign in in child window"):
            signin.navigate_to(base_url)
            # time.sleep(3)
        with allure.step("clicking on sign in"):
            signin.signup()
            signin.switch_to_window()
            # signin.siginthroughgoogle()
            # signin.entermail()
            # time.sleep(30)
        acct=Accounts(self.driver)
        with allure.step("clicking on the product"):
             acct.select_shop()
             acct.select_copper()
             # acct.select_shop_and_copper()
        cpp=MadeWithCopperPage(self.driver)
        cpp.instockbutton()
        cpp.filterproducttye()
        cpp.bottlensippers()
        bttlnsip=BottleAndSippers(self.driver)
        bttlnsip.select_product()
        bttlnsip.buyit()


        # signout=SignOut(self.driver)
        # with allure.step("signing out"):
        #
        #     signout.signout()
        #
        # time.sleep(9)






