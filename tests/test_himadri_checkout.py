import allure

from config.environment import Environment
from pages.himadri_cart_page import HimadriCartPage
from pages.validation_shop_all_page import ShopAll_Validation
from tests.base_test import BaseTest
from pages.himadri_login_page import HimadriLoginPage
from pages.himadri_checkout import HimadriCheckout

class TestHimadriCartPage(BaseTest):
    def test_successful_login(self):
        login_page = HimadriLoginPage(self.driver)
        shopall_valid = ShopAll_Validation(self.driver)
        cart_page = HimadriCartPage(self.driver)
        checkout_page = HimadriCheckout(self.driver)
        env = Environment('himadri')
        base_url = env.get_base_url()
        email = env.get_email()
        password = env.get_password()

        with allure.step("Navigate to login page"):
            login_page.navigate_to(base_url)
            assert login_page.is_visible(login_page.LOGIN_CLICK), "Login page did not load properly"

        with allure.step("Perform login with valid credentials"):
            login_page.login(email, password)

        with allure.step('click on the shop all button on the account page'):
            shopall_valid.click_shopall()

        with allure.step("Checking Click on Shop All is successful"):
            shopall_valid.is_clickon_shopall_successful()

        with allure.step("Click on Aquarium Accessories"):
            cart_page.click_on_aquarium_accessories()

        with allure.step("Checking click on Aquarium Accessories is successful"):
            cart_page.click_on_aquarium_accessories_sucessful()
            assert cart_page.click_on_aquarium_accessories_sucessful,'click on Aquarium Accessories is unsuccessful'

        with allure.step("Clicking on aquarium black lava rock"):
            cart_page.click_on_aquarium_black_lava_rock_product()

        with allure.step('Click on go to cart page'):
            cart_page.go_to_cart()

        with allure.step("Click on Proceed to checkout"):
            checkout_page.click_on_checkout_button()

        with allure.step("Checking click on checkout button is successful"):
            checkout_page.is_click_on_checkout_button_sucessful()
            assert checkout_page.is_click_on_checkout_button_sucessful,'click on checkout button is unsuccessful'

        with allure.step("fill the shipping address"):
            checkout_page.fill_shipping_address('Varsha','Lokanathan','laxmi nagar','karatuvayal','kanhangad','kerala','671315','7907179414','varsha@gmail.com')

        with allure.step(" click on terms and condition"):
            checkout_page.click_on_termsandcondition()


