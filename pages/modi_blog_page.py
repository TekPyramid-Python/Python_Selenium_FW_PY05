from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ModiBlogPage(BasePage):
    read_more=(By.XPATH,"(//article[contains(@class,'elementor-post')])[2]")

    def modi_blog_recepi(self):
        self.scroll_to_element(self.read_more)
        self.click(self.read_more)