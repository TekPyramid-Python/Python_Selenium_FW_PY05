
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PhilosophyPage(BasePage):

    page_title = (By.XPATH,  "//h1[contains(text(),'Philosophy')]")
    content_section= (By.XPATH, "(//div[contains(@class,'philosophy-article')])[1]//a")
    images=(By.TAG_NAME, "img")
    testimonies_menu=("xpath","//a[contains(text(),'Testimonies')]")
    PHILOSOPHY_SECTION = ("xpath", "//*[contains(text(),'Philosophy') or contains(text(),'philosophy')]")

    def __init__(self,driver):
        super().__init__(driver)

    def is_page_loaded(self):
        return self.is_visible(self.PHILOSOPHY_SECTION,timeout=10)

    def is_content_visible(self):
        return self.is_visible(self.content_section)

    def has_images(self):
        images=(self.find_elements(self.images))>0

    def click_testimonies(self):
        self.click(self.testimonies_menu)





