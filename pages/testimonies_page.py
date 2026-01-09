from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TestimoniesPage(BasePage):

    page_title = (By.XPATH, "//h1[contains(text(),'Testimonies')]")
    youtube_icon= ("xpath","//a[contains(@href,'youtube.com')]")
    # social_icon=("xpath","//a[contains(@href,'facebook') or contains(@href,'instagram') or contains(@href,'youtube')]")
    home_logo=("xpath","//a[contains(@class,'logo')")
    # testimonies_cards=("xpath","//a[contains(@class,'logo')")





    def is_page_loaded(self):
        return self.is_visible(self.page_title)

    def click_youtube_link(self):
        self.click(self.youtube_icon)

    def youtube_opened(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return "youtube" in self.driver.current_url.lower()

    def click_home_logo(self):
        self.click(self.home_logo)














