from time import sleep

import allure

from ..config.environment import Environment
from ..pages.bl_accounts import Accounts
from ..pages.bl_reviewpage import Review
from ..pages.bl_signup_page import Signup_Page
from ..tests.base_test import BaseTest


class TestWriteReview(BaseTest):
    # G_SIGNUP = (By.CSS_SELECTOR, ".social-login-button")

    def test_write_review(self):
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
        review=Review(self.driver)
        with allure.step("entering to write review"):
            acct.select_review()
            sleep(8)
            # review.closepop()
            # sleep(100)
            review.clickonreview()
            sleep(4)
            review.writeareview()
            # sleep(100)
            review.fillratings()

