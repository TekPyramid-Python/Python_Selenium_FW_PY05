from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage

class BlogPage(BasePage):
    PAGE_TITLE = (By.XPATH, "//h1[normalize-space()='Blog']")
    BLOG_IMAGES = (By.XPATH, "//div[contains(@class,'blog')]//img")
    EVENTS_LINK = (By.XPATH, "//a[contains(text(),'Events')]")

    def is_blog_page_loaded(self):
        return self.is_visible(self.PAGE_TITLE)

    def click_all_blog_images(self):
        images = self.driver.find_elements(*self.BLOG_IMAGES)
        for img in images:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", img)
            self.driver.execute_script("arguments[0].click();", img)
            self.driver.back()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.PAGE_TITLE)
            )


