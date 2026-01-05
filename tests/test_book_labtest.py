from time import sleep

import allure
import pytest
from config.environment import Environment
from pages.clinicwala_homepage import HomePage
from pages.janchwala_page import PathologyPage
from tests.base_test import BaseTest

@allure.feature("Pathology")
@allure.story("To book lab test")
class TestPathology(BaseTest):
    @pytest.mark.clinicwala
    def test_book_labtest(self):
        home_page = HomePage(self.driver)
        janchwala_page= PathologyPage(self.driver)
        env = Environment()
        base_url = env.get_base_url()

        with allure.step("Navigate to home page"):
            home_page.navigate_to(base_url)
            assert home_page.is_visible(home_page.PATHOLOGY_LINK), "Home page did not load properly"

        with allure.step("Navigate to Janchwala page"):
            home_page.on_click_book_test()
            expected_title="Janchwala Pathology – Book Lab Tests Online in India"
            actual_title=janchwala_page.get_title()
            assert expected_title==actual_title,"Title mismatch"

        with allure.step("Navigate to janchwala page"):
            janchwala_page.on_click_booktest()

        with allure.step("Navigate to Health packages page"):
            janchwala_page.on_click_healthpackage()
            expected_title = "Explore all health package | Janchwala - Book Lab Tests Online"
            actual_title = janchwala_page.get_title()
            assert expected_title == actual_title, 'Title mismatch'

        with allure.step("Selecting one health package"):
            janchwala_page.select_fullbody_package()

        with allure.step("Attempting to book package"):
            janchwala_page.on_click_booknow()


        with allure.step("Upload file to dropzone"):
            janchwala_page.file_upload(r"C:\Clinicwala\prescription.png")
