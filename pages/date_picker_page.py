from ..pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class DatePickerPage(BasePage):
    """
    Page Object for the Test Automation Practice blogspot page,
    focusing on the date picker widgets.
    """
    # --- Locators for Date Picker 1 ---
    DATE_PICKER_INPUT = (By.ID, "datepicker")
    CALENDAR_MONTH_DROPDOWN = (By.CLASS_NAME, "ui-datepicker-month")
    CALENDAR_YEAR_DROPDOWN = (By.CLASS_NAME, "ui-datepicker-year")

    # This locator is dynamic. We will use .format() to insert the day number.
    CALENDAR_DAY_LINK = (By.XPATH, "//a[text()='{}']")

    def __init__(self, driver):
        super().__init__(driver)

    def select_date(self, target_date):
        """
        Selects a specific date from the calendar widget.

        Args:
            target_date (str): The date to select in "DD-Month-YYYY" format
                               (e.g., "15-August-2025").
        """
        self.logger.info(f"Attempting to select date: {target_date}")

        # 1. Split the target date into day, month, and year
        try:
            day, month, year = target_date.split('-')
        except ValueError:
            self.logger.error("Date format is incorrect. Please use 'DD-Month-YYYY'.")
            raise

        # 2. Click the input field to open the calendar
        self.click(self.DATE_PICKER_INPUT)

        # Give the calendar a moment to animate and become fully visible
        time.sleep(1)

        # 3. Select the year from the dropdown
        year_dropdown = self.wait_for_element(self.CALENDAR_YEAR_DROPDOWN)
        if year_dropdown:
            select_year = Select(year_dropdown)
            select_year.select_by_visible_text(year)
            self.logger.info(f"Selected year: {year}")
        else:
            self.logger.error("Could not find the Year dropdown.")
            return

        # 4. Select the month from the dropdown
        month_dropdown = self.wait_for_element(self.CALENDAR_MONTH_DROPDOWN)
        if month_dropdown:
            select_month = Select(month_dropdown)
            select_month.select_by_visible_text(month)
            self.logger.info(f"Selected month: {month}")
        else:
            self.logger.error("Could not find the Month dropdown.")
            return

        # 5. Select the day by clicking the link with the correct text
        day_locator = (self.CALENDAR_DAY_LINK[0], self.CALENDAR_DAY_LINK[1].format(day))
        self.click(day_locator)
        self.logger.info(f"Selected day: {day}")

    def get_selected_date(self):
        """
        Gets the currently selected date from the input field.
        """
        # We need to get the 'value' attribute, not the text
        date_input_element = self.wait_for_element(self.DATE_PICKER_INPUT)
        if date_input_element:
            return date_input_element.get_attribute("value")
        return ""