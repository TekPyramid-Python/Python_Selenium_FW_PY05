# tests/test_itokri_product_verify.py
from time import sleep

import allure
import pytest
from datetime import datetime
from config.environment import Environment
from pages.itokri_home_page import ItokriHomePage
from pages.itokri_product_page import ItokriProductPage
from pages.itokri_listof_new_page import ItokriListOfNewPage
from tests.base_test import BaseTest


@allure.feature("Browse Sarees")
@allure.story("Browse Sarees by Craft Type")
class TestItokriProduct(BaseTest):
    """
    Test class for create account functionality against itokri.com.
    """

    @allure.title("Test successful login with valid credentials")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    @pytest.mark.itokri
    def test_product_verify(self):
        homepage=ItokriHomePage(self.driver)
        newpage=ItokriListOfNewPage(self.driver)
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

        with allure.step("2. Navigate to new page"):
            homepage.nav_to_new_menu()
            self.logger.info("New page is displayed successfully")

        with allure.step("3. Check the total number of item is >40 or not "):
            now = datetime.now()
            formatted_date = now.strftime("%d %B, %Y")
            print(formatted_date,newpage.get_latest_date())
            assert formatted_date in newpage.get_latest_date(), "Today's date is not same as latest date"
            self.logger.info("Today's date is same as latest date")

        # with allure.step("4. Check the saree is Banarasi Sarees or not"):
        #     listpage.click_first_product()
        #     assert "Banarasi" in productpage.get_craft_type(),"Saree type is not Banarasi"
        #     self.logger.info("Banarasi Saree craft checked successfully")
        #
        # with allure.step("5. Check the saree is from Verified Partner or not"):
        #     assert "Verified Partner" in productpage.get_artisan_text(),"Saree is not from Verified Partner "
        #     self.logger.info("The Saree is from Verified Partner checked successfully")
        # with allure.step("6. Check the saree is 100% made with silk or not"):
        #     assert "100%" in productpage.get_meterial_text(),"Saree in not made 100% silk"
        #     self.logger.info("The Saree is Check the saree is 100% made with silk successfully")
        #
        # with allure.step("7. Going back to list"):
        #     productpage.back_to_list()
        #     sleep(4)
        #     self.logger.info("The control goes back to the list page successfully")


