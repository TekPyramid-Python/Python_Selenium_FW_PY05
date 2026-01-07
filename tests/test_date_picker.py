# tests/test_date_picker.py
import time

import pytest
import allure
from tests.base_test import BaseTest
from pages.date_picker_page import DatePickerPage
from config.environment import Environment


@allure.epic("Component Tests")
@allure.feature("Date Picker")
class TestDatePicker(BaseTest):
    """
    Test class for verifying the functionality of all calendar controls.
    """

    # NOTE: All tests require ENV=practice to be set in the Run Configuration.

    @pytest.mark.regression
    @allure.story("Calendar with Arrow Navigation")
    @allure.title("Test selecting a date from calendar with arrows (Picker 1)")
    def test_select_date_with_arrows(self):
        """Verifies selecting a date from a calendar with next/prev arrows."""
        date_page = DatePickerPage(self.driver)
        env = Environment("practice")

        target_date_str = "15-August-2026"
        expected_date_in_field = "08/15/2026"

        with allure.step("Navigate and select a date using arrows"):
            date_page.navigate_to(env.get_base_url())
            date_page.select_date_with_arrows(target_date_str)

        with allure.step("Verify the correct date is displayed"):
            selected_date = date_page.get_selected_date(picker_number=1)
            assert selected_date == expected_date_in_field
            time.sleep(3)

    @pytest.mark.regression
    @allure.story("Calendar with Dropdown Navigation")
    @allure.title("Test selecting a date from calendar with dropdowns (Picker 2)")
    def test_select_date_with_dropdowns(self):
        """Verifies selecting a date from a calendar with month/year dropdowns."""
        date_page = DatePickerPage(self.driver)
        env = Environment("practice")

        target_date_str = "25-December-2027"
        expected_date_in_field = "25/12/2027"

        with allure.step("Navigate and select a date using dropdowns"):
            date_page.navigate_to(env.get_base_url())
            date_page.select_date_with_dropdowns(target_date_str)
            time.sleep(2)

        with allure.step("Verify the correct date is displayed"):
            selected_date = date_page.get_selected_date(picker_number=2)
            assert selected_date == expected_date_in_field
            time.sleep(2)

    @pytest.mark.regression
    @allure.story("Native HTML5 Date Range Picker")
    @allure.title("Test selecting a date range (Picker 3)")
    def test_select_date_range(self):
        """Verifies selecting a start and end date from a native date range picker."""
        date_page = DatePickerPage(self.driver)
        env = Environment("practice")

        start_date = "2027-06-01"  # yyyy-MM-dd format
        end_date = "2027-06-15"
        expected_result_text = "You selected a range of 14 days."

        with allure.step("Navigate and select a date range"):
            date_page.navigate_to(env.get_base_url())
            date_page.select_date_range(start_date, end_date)

        with allure.step("Verify the correct result message is displayed"):
            actual_result = date_page.get_date_range_result()
            assert actual_result == expected_result_text