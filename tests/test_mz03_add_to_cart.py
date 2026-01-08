import pytest
import allure
from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from pages.cart_page import CartPage


@allure.feature("Cart")
@allure.story("Add product to cart")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_mz03_add_to_cart(driver, env):

    login_page = LoginPage(driver)
    shop_page = ShopPage(driver)
    cart_page = CartPage(driver)

    with allure.step("Login to application"):
        login_page.login(env.get_username(), env.get_password())

    with allure.step("Go to Shop All"):
        shop_page.open_shop_all()

    with allure.step("Select any product"):
        shop_page.select_any_product()

    with allure.step("Add product to cart"):
        shop_page.add_product_to_cart()

    with allure.step("Open cart"):
        cart_page.open_cart()

    with allure.step("Verify product is present in cart"):
        assert cart_page.is_product_present(), "Product not found in cart"
