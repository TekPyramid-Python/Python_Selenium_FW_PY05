from time import sleep

import allure
import pytest
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from config.environment import Environment
from pages.clinicwala_homepage import HomePage
from pages.dawaiwala_page import MedicinePage
from tests.base_test import BaseTest


@allure.feature("Dawaiwala")
@allure.story("To book medicine")
class TestBuyMedicine(BaseTest):
    @pytest.mark.clinicwala
    def test_book_medicine(self):
        home_page = HomePage(self.driver)
        dawaiwala_page = MedicinePage(self.driver)
        env = Environment()
        base_url = env.get_base_url()

        with allure.step("Navigate to home page"):
            home_page.navigate_to(base_url)
            assert home_page.is_visible(home_page.MEDICINE_LINK), "Home page did not load properly"

        with allure.step("Navigate to dawaiwala page"):
            home_page.on_click_book_medicines()
            sleep(10)
            expected_title = "Buy Medicines Online in India | Fast Medicine Delivery | DawaiWala.com ePharmacy"
            actual_title = dawaiwala_page.get_title()
            assert expected_title == actual_title, "Title mismatch"


        with allure.step("Navigate to Medicine list page"):
            dawaiwala_page.on_click_ayurveda()

        with allure.step("Selecting category"):
            dawaiwala_page.select_category()
            expected_title = "Buy Multivitamins products Online in India | DawaiWala.com ePharmacy"
            actual_title = dawaiwala_page.get_title()
            assert expected_title == actual_title, "Title mismatch"

        with allure.step("Selecting product"):
            dawaiwala_page.select_product()
