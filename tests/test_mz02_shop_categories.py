import pytest
import allure
from pages.login_page import LoginPage
from pages.shop_page import ShopPage


@allure.feature("Shop")
@allure.story("Verify Lighting and Furniture categories")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_mz02_verify_lighting_and_furniture(driver, env):

    login_page = LoginPage(driver)
    shop_page = ShopPage(driver)

    with allure.step("Login to application"):
        login_page.login(env.get_username(), env.get_password())

    with allure.step("Navigate to SHOP"):
        shop_page.open_shop()

    with allure.step("Open Lighting category"):
        shop_page.open_lighting()
        assert shop_page.products_are_displayed(), "Lighting products not displayed"

    with allure.step("Navigate back to SHOP"):
        shop_page.open_shop()

    with allure.step("Open Furniture category"):
        shop_page.open_furniture()
        assert shop_page.products_are_displayed(), "Furniture products not displayed"




