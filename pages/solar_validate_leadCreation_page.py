import time
from pages.base_page import BasePage


class SiteInfoValidation(BasePage):
    # LEAD_NAME_ACTUAL = ('xpath', '//div[text()="Lead Full Name"]/following-sibling::div/span')
    LEAD_NAME_ACTUAL = ('xpath', '//div[text()="Lead Full Name"]/../div/span')
    LEAD_EMAIL_ACTUAL = ('xpath', '//div[text()="Lead Email ID"]/following-sibling::div/span')

    # Additonal info verification locators
    ACTUAL_DEAL_VALUE = ('xpath', '//div[text()=" Deal Value "]/../..//div/span')
    ACTUAL_TARGET_CLOSE_DATE = ('xpath', '//div[text()="Target Close Date"]/..//div/span')
    ACTUAL_SYSTEM_SIZE = ('xpath', '//div[text()="System Size"]/..//div/p')
    ACTUAL_PROBABILITY = ('xpath', '//div[text()="Probability"]/..//div/span')

    def __init__(self, driver):
        super().__init__(driver)

    def get_lead_name(self):
        return str(self.get_text(self.LEAD_NAME_ACTUAL))

    def get_lead_email(self):
        return self.get_text(self.LEAD_EMAIL_ACTUAL)

    # Additonal info verification methods
    def get_deal_value(self):
        return self.get_text(self.ACTUAL_DEAL_VALUE)

    def get_target_close_date(self):
        return self.get_text(self.ACTUAL_TARGET_CLOSE_DATE)

    def get_system_size(self):
        return self.get_text(self.ACTUAL_SYSTEM_SIZE)

    def get_probability(self):
        return self.get_text(self.ACTUAL_PROBABILITY)


