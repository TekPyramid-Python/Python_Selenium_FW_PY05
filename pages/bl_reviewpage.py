
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from ..pages.base_page import BasePage

import time

class Review(BasePage):
    CLICKWRITEREVIEW=(By.XPATH,"(//button[@aria-haspopup='dialog'])[1]")
    RATING=(By.XPATH,"//button[@aria-label='Set rating to 1']")
    FILLREVIEW=(By.XPATH,"//textarea[@placeholder='Write a review']")
    NEXT=(By.XPATH,"//button[@aria-live='polite']")
    closepopup=(By.XPATH,'//button[@aria-label="Close"]')
    RATING1=(By.XPATH,'//select[@name="cf_answers[2976][value]"]')
    RATING2=(By.XPATH,'//select[@name="cf_answers[97688][value]"]')
    RATING3 = (By.XPATH, '//select[@name="cf_answers[97689][value]"]')
    RATING4 = (By.XPATH, '//select[@name="cf_answers[97690][value]"]')
    RATING5 = (By.XPATH, '//select[@name="cf_answers[97692][value]"]')
    RATING6 = (By.XPATH, '//select[@name="cf_answers[97693][value]"]')
    RATING7 = (By.XPATH, '//select[@name="cf_answers[97695][value]"]')
    RATING8 = (By.XPATH, '//select[@name="cf_answers[97696][value]"]')
    RATING9 = (By.XPATH, '//select[@name="cf_answers[97697][value]"]')

    RATING10 = (By.XPATH, '//input[@name="cf_answers[97698][value]"]')
    RATING11 = (By.XPATH, '//select[@name="cf_answers[97699][value]"]')
    RATING12   = (By.XPATH, '//select[@name="cf_answers[97700][value]"]')
    RATING13 = (By.XPATH, '//input[@name="cf_answers[97701][value]"]')
    SUBMITRVIEW = (By.XPATH, '//button[@aria-live="polite"]')


    # class ="a8x1wuy a8x1wux _1fragem32 _1fragemq1 _1fragemly _1fragemlo _1fragemp6".

    def clickonreview(self):
        self.scroll_to_element(self.CLICKWRITEREVIEW)
        # time.sleep(100)
        self.click(self.CLICKWRITEREVIEW)

    def closepop(self):
        self.click(self.closepopup)

    def writeareview(self):
        self.click(self.RATING)
        self.send_keys(self.FILLREVIEW,"ok")
        self.scroll_to_element(self.NEXT)
        self.click(self.NEXT)
        time.sleep(8)

    def fillratings(self):
        self.logger.info(f"Attempting to select ratings using dropdowns")
        self.scroll_to_top()
        Select(self.wait_for_element(self.RATING1)).select_by_visible_text("3")
        time.sleep(2)
        Select(self.wait_for_element(self.RATING2)).select_by_visible_text("Poor")
        time.sleep(2)
        Select(self.wait_for_element(self.RATING3)).select_by_visible_text("Somewhat difficult")
        time.sleep(2)
        Select(self.wait_for_element(self.RATING4)).select_by_visible_text("Neutral")
        time.sleep(2)
        Select(self.wait_for_element(self.RATING5)).select_by_visible_text("A bit expensive")
        time.sleep(2)
        Select(self.wait_for_element(self.RATING6)).select_by_visible_text("Poor")
        time.sleep(2)
        Select(self.wait_for_element(self.RATING7)).select_by_visible_text("Neutral")
        time.sleep(2)
        Select(self.wait_for_element(self.RATING8)).select_by_visible_text("Partially – some items were in good condition, others were damaged.")
        time.sleep(2)
        Select(self.wait_for_element(self.RATING9)).select_by_visible_text("No plastic at all")
        self.send_keys(self.RATING10, "no")
        time.sleep(2)
        Select(self.wait_for_element(self.RATING11)).select_by_visible_text("Not important at all")
        time.sleep(3)
        Select(self.wait_for_element(self.RATING12)).select_by_visible_text("Not at all")
        time.sleep(3)
        self.send_keys(self.RATING13, "no")
        self.click(self.SUBMITRVIEW)
        # day_locator = (self.CALENDAR_DAY_LINK[0], self.CALENDAR_DAY_LINK[1].format(target_date.day))
        # self.click(day_locator)

    def scroll_to_top(self):
          self.driver.execute_script("window.scrollTo(0, 0);")
