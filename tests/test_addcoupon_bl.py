from time import sleep

import allure

from config.environment import Environment
from pages.bl_accounts import Accounts
from pages.bl_cart import Cart
from pages.bl_reviewpage import Review
from pages.bl_signup_page import Signup_Page
from tests.base_test import BaseTest


class TestAddCoupon(BaseTest):

    def test_increase_qty_and_add_coupon(self):
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
        cart = Cart(self.driver)
        with allure.step("clicking on the shop"):
            acct.select_shop1()
            signin.select_cart()
            # sleep(30)

            cart.add_to_cart()
            sleep(20)
            cart.increase_qty()
            cart.add_coupon()
            cart.check_out()
