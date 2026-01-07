from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    HOME_LINK = (By.XPATH, "//a[normalize-space()='Home']")
    COACHES_LINK = (By.XPATH, "//a[normalize-space()='Coaches']")
    BLOG_MENU = (By.XPATH, "//a[contains(@href,'blog')]")
    EVENTS_MENU = (By.XPATH, "//a[contains(@href,'event')]")
    CONTACT_US_LINK = (By.LINK_TEXT, "Contact Us")
    PHILOSOPHY_LINK = (By.XPATH, "//a[normalize-space()='Philosophy']")
    TESTIMONIES_LINK = (By.XPATH, "//a[normalize-space()='Testimonies']")
    HOME_LOGO = (By.XPATH, "//a[@class='logo']")

    def is_home_loaded(self):
        return self.is_visible(self.HOME_LINK, timeout=20)

    def click_home(self):
        self.click(self.HOME_LINK)

    def click_coaches(self):
        self.click(self.COACHES_LINK)

    def click_blog(self):
        self.click(self.BLOG_MENU)

    def click_events(self):
        self.click(self.EVENTS_MENU)

    def click_contact_us(self):
        self.scroll_to_element(self.CONTACT_US_LINK)
        self.click(self.CONTACT_US_LINK)

    def click_philosophy(self):
        self.click(self.PHILOSOPHY_LINK)

    def click_testimonies(self):
        self.click(self.TESTIMONIES_LINK)



