import time
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class SiteInfo(BasePage):

#Site_info_lead_and_site_info
    LEAD_AND_SITE_BUTTON = ('xpath', '//div[@id="tab-lead"]')

#Site_info_Pipeline_info
    PIPELINE_INFO_BUTTON = ('xpath', '//div[@id="tab-pipeline"]')

#Site_info_Additional_info
    ADDITIONAL_INFO_BUTTON = ('id', "tab-additional")
    EDIT_BUTTON = ('xpath', '(//i[@class="bi-pencil lead-update-icon"])[3]')
    DEAL_VALUE = ('xpath', '(//input[@type="number"])[1]')
    TARGET_CLOSE_BUTTON = ('xpath', '//input[@placeholder="Select a day"]')
    SYSTEM_SIZE = ('xpath', '(//input[@type="number"])[2]')
    PROBABILITY = ('xpath', '(//input[@type="number"])[3]')
    LEAD_SOURCE = ('xpath', '//label[text()="Lead Source"]/..//span[text()="Lead Source"]')
    LEAD_SOURCE_OPTION = ('xpath', '//li[text()="Marketing"]')
    REGION = ('xpath', '//label[text()="Region"]/..//span[text()="Region"]')
    REGION_OPTION = ('xpath', '//li[text()="region_-2025-04-09 14:00:00"]')
    UPDATE_BUTTON = ('xpath', '(//button[@type="button"])[4]')



    def __init__(self, driver):
        super().__init__(driver)

    def lead_and_site_info(self):
        pass

    def pipeline_info(self):
        pass

    def additional_info(self, deal_value, target_close_date, system_size, probability):
        self.logger.info(f"Attempting to Edit Additional info page")
        self.click(self.ADDITIONAL_INFO_BUTTON)
        self.click(self.EDIT_BUTTON)
        self.send_keys(self.DEAL_VALUE, deal_value)
        self.send_keys(self.TARGET_CLOSE_BUTTON, target_close_date)
        self.send_keys(self.SYSTEM_SIZE, system_size)
        self.send_keys(self.PROBABILITY, probability)
        self.click(self.LEAD_SOURCE)
        self.click(self.LEAD_SOURCE_OPTION)
        self.click(self.REGION)
        self.click(self.REGION_OPTION)
        self.click(self.UPDATE_BUTTON)
        time.sleep(4)


