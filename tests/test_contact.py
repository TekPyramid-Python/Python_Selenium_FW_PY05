import allure
import pytest
from selenium import webdriver
from pages.contact_us_page import ContactUsPage


@allure.feature("Contact Us Page")
@allure.story("Contact form submission")
class TestContactUsPage:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    @allure.title("Verify Contact Us page loads successfully")
    def test_contact_page_load(self, driver):
        contact = ContactUsPage(driver)

        contact.open_contact_us()
        assert contact.is_contact_page_loaded(), "Contact page did not load"

    @allure.title("Verify Contact form submission with dropdown")
    def test_contact_form_submission(self, driver):
        contact = ContactUsPage(driver)

        contact.open_contact_us()

        contact.fill_contact_form(
            first="Malini",
            email="malini@test.com",
            country="India",
            help_on="General Enquiry",
            message="Testing contact form with Allure"
        )

        contact.submit_form()
