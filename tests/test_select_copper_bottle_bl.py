import time

import pytest
import allure
from selenium.webdriver.common.by import By

from ..config.environment import Environment
from ..pages.bl_accounts import Accounts
from ..pages.bl_bottleandsippers import BottleAndSippers
from ..pages.bl_madewithcopperpage import MadeWithCopperPage
from ..pages.bl_signout import SignOut
from ..pages.bl_signup_page import Signup_Page
from ..tests.base_test import BaseTest


class TestSelectCopperBottle(BaseTest):
    # G_SIGNUP = (By.CSS_SELECTOR, ".social-login-button")

    def test_add_product_to_cart(self):

        env = Environment("newapp")
        base_url = env.get_base_url()
        acct = Accounts(self.driver)
        signin = Signup_Page(self.driver)
        cpp = MadeWithCopperPage(self.driver)
        bttlnsip = BottleAndSippers(self.driver)
        with allure.step("Navigate to base url"):
            signin.navigate_to(base_url)
            self.logger.info(f"navigating to base url")

        with allure.step("clicking on sign in through google"):
            signin.signup()
            self.logger.info(f"clicked on signup button in home page")
            signin.switch_to_window()
            self.logger.info("switched to new window")
            assert signin.is_visible(signin.ALREADY_SIGNED_IN), "Not able to locate the google signupicon"


            # expected_title = "Sign in - Brown Living™"  # This is wrong on purpose
            # actual_title = signin.get_title()
            # assert expected_title == actual_title, "This assertion is designed to fail to test screenshot capture."
            # signin.siginthroughgoogle()
            # assert signin.is_visible(signin.G_SIGNUP), "Not able to locate the google signup button"
            # self.logger.info("switched to new window")
            #
            # expected_title = "Sign in to continue to brownliving.in"  # This is wrong on purpose
            # actual_title = signin.get_title()
            # assert expected_title == actual_title, "This assertion is to check google signin button."
            # signin.entermail()
            # time.sleep(30)

        with allure.step("clicking on the product"):
             assert acct.is_visible(acct.SHOP), "Not able to locate the shop button"
             acct.select_shop()

             acct.select_copper()
             # acct.select_shop_and_copper()

        self.logger.info("selecting the product")

        # expected_title = "Made with Copper on Brown Living™" # This is wrong on purpose
        # actual_title = signin.get_title()
        # assert expected_title in actual_title, "This assertion is designed to fail to test screenshot capture for product page."
        assert "eco-friendly-copper-essentials" in self.driver.current_url
        # assert cpp.is_visible(cpp.INSTOCK), "Not able to locate the instock filter"

        cpp.filterproducttye()
        # assert cpp.is_visible(cpp.PRODUCTTYPE), "Not able to locate the product type filter"

        cpp.bottlensippers()
        self.logger.info("selecting the copper product")
        time.sleep(8)
        bttlnsip.select_product()
        # assert bttlnsip.is_visible(bttlnsip.BUYIT), "Not able to locate the copperbottle filter"
        time.sleep(8)

        # assert "Bottles" in self.driver.current_url and "Sippers" in self.driver.current_url
        # assert bttlnsip.is_visible(bttlnsip.BUYIT), "Not able to locate the buyit"
        bttlnsip.buyit()

        # signout=SignOut(self.driver)
        # with allure.step("signing out"):
        #     self.logger.info("in the signout")
        #
        #     expected_title = "Orders - Brown Living™ - Account"  # This is wrong on purpose
        #     actual_title = signin.get_title()
        #     assert expected_title == actual_title, "This assertion is designed to fail to test screenshot capture."
        #     signout.signout()
        #
        #     time.sleep(9)






