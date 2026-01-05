import allure
import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.environment import Environment
from pages.clinicwala_homepage import HomePage
from pages.doctor_list_page import DoctorListPage
from tests.base_test import BaseTest

@allure.feature("Book Appointment")
@allure.story("To book doctor appointment")
class TestBookDoctorAppointment(BaseTest):
    @pytest.mark.clinicwala
    def test_book_doctor_appointment(self):
        home_page = HomePage(self.driver)
        doc_page= DoctorListPage(self.driver)
        env = Environment()
        base_url = env.get_base_url()


        with allure.step("Navigate to home page"):
            home_page.navigate_to(base_url)
            assert home_page.is_visible(home_page.DOCTOR_APPOINTMENT_LINK), "Home page did not load properly"


        with allure.step("Navigate to Book appointment page"):
            try:
                element= WebDriverWait(self.driver,15).until(EC.presence_of_element_located(home_page.DOCTOR_APPOINTMENT_LINK))
                home_page.on_click_book_appointment()
            except Exception:
                self.driver.execute_script("arguments[0].click();",element)
            expected_title="Online doctor appointment: Securely Connect with Doctors Online in India."
            actual_title=home_page.get_title()
            assert expected_title == actual_title , 'Title mismatch'

        with allure.step("Filter doctor list according to speciality"):
            doc_page.select_speciality()

        with allure.step("Verify to view Doctor profile"):
            doc_page.select_doctor_profile()

        with allure.step("Select appointment date"):
            doc_page.select_appointment_date()

        doc_page.click_continue()

