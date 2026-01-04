
# tests/test_itokri_product_verify.py
from time import sleep

import allure
import pytest

from config.environment import Environment
from pages.itokri_home_page import ItokriHomePage
from pages.itokri_product_page import ItokriProductPage
from pages.itokri_listof_product_page import ItokriListOfProductPage
from tests.base_test import BaseTest


@allure.feature("Browse Sarees")
@allure.story("Browse Sarees by Craft Type")
class TestItokriGetProductAndAddtocart(BaseTest):
    """
    Test class for create account functionality against itokri.com.
    """

    @allure.title("Test successful login with valid credentials")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_get_product_and_addtocart(self):
        homepage=ItokriHomePage(self.driver)
        listpage=ItokriListOfProductPage(self.driver)
        productpage=ItokriProductPage(self.driver)
        env = Environment()
        base_url = env.get_base_url()
        email=env.get_username()
        password=env.get_password()
        with allure.step("1. Open homepage"):
            homepage.navigate_to(base_url)
            try:
                homepage.click_cross_button()
            except:
                print("cross button not came")
            self.logger.info("Home page is displayed successfully.")

        with allure.step("2. Hover on Sarees and click on Banarasi Sarees"):
            homepage.product_select()
            self.logger.info("Banarasi Saree page is displayed successfully")

        with allure.step("3. Click on first Banarasi Sarees "):
            listpage.click_first_product()
            assert "Banarasi" in productpage.get_craft_type(),"Saree type is not Banarasi"
            self.logger.info("Banarasi Saree craft checked successfully and clicked")

        with allure.step("4. Click on the add to tokri"):
            productpage.click_on_add_to_tokri()
            self.logger.info("The Saree is added successfully")

        with allure.step("5. Going back to homepage"):
            listpage.back_to_homepage()
            self.logger.info("The control goes back to the home page successfully")

        with allure.step("6. Hover on Dupattas and click on Ajrakh Dupatta"):
            homepage.dupatta_select()
            self.logger.info("Ajrakh Dupatta page is displayed successfully")

        with allure.step("7. Click on first Ajrakh Dupatta"):
            listpage.click_first_product()
            assert "Ajrakh" in productpage.get_craft_type(),"Dupatta type is not Ajrakh"
            self.logger.info("Ajrakh Dupatta craft checked successfully and clicked")

        with allure.step("8. Click on the add to tokri"):
            productpage.click_on_add_to_tokri()
            self.logger.info("The First Dupatta is added successfully")

        with allure.step("9. Going back to homepage"):
            listpage.back_to_homepage()
            self.logger.info("The control goes back to the home page successfully")

        with allure.step("10. Hover on Home & Decor and click on Kalamkari Cushion Covers"):
            homepage.home_decor_select()
            self.logger.info("Kalamkari Cushion Covers page is displayed successfully")

        with allure.step("11. Click on first Kalamkari Cushion Covers"):
            listpage.click_first_product()
            assert "kalamkari" in productpage.get_craft_type(),"Cushion Covers type is not Kalamkari"
            self.logger.info("Kalamkari Cushion Covers craft checked successfully and clicked")

        with allure.step("12. Click on the add to tokri"):
            productpage.click_on_add_to_tokri()
            self.logger.info("The First Cushion Covers is added successfully")

        with allure.step("13. Going back to list"):
            productpage.back_to_list()
            self.logger.info("The control goes back to the list page successfully")

        with allure.step("14. Going back to homepage"):
            listpage.back_to_homepage()
            self.logger.info("The control goes back to the home page successfully")

        with allure.step("15. Going to Add to cart page"):
            listpage.click_on_cart()
            listpage.click_on_view_cart()
            self.logger.info("The control goes to the add to cart page successfully")
            sleep(10)
