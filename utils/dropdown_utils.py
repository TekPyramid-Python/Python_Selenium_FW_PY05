from selenium.webdriver.support.ui import Select

class DropdownUtils:

    @staticmethod
    def select_by_visible_text(element, text):
        Select(element).select_by_visible_text(text)

    @staticmethod
    def select_by_value(element, value):
        Select(element).select_by_value(value)

    @staticmethod
    def select_by_index(element, index):
        Select(element).select_by_index(index)
