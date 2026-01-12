from time import sleep

import allure

from ..config.environment import Environment
from ..pages.bl_accounts import Accounts
from ..pages.bl_address import Address
from ..pages.bl_all_products import All_Products
from ..pages.bl_cart import Cart
from ..pages.bl_profile import Profile
from ..pages.bl_reviewpage import Review
from ..pages.bl_signup_page import Signup_Page
from ..tests.base_test import BaseTest


class Test_Search_Product(BaseTest):

    def test_search_product(self):
        signin = Signup_Page(self.driver)
        env = Environment("newapp")
        base_url = env.get_base_url()
        acct = Accounts(self.driver)
        prod=All_Products(self.driver)
        with allure.step("Navigate and sign in in child window"):
            signin.navigate_to(base_url)
            # time.sleep(3)
        with allure.step("clicking on sign in"):
            signin.signup()
            signin.switch_to_window()
            acct.select_shop()
            signin.search_product()
        with allure.step("clicking on product"):
            prod.sort()
            prod.add_product()
            sleep(100)

