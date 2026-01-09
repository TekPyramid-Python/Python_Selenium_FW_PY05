from webdriver_manager.core.driver import Driver

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.dental_home_page import HomePage
from time import sleep
class Search(BasePage):
    search_box=(By.XPATH,'(//input)[1]')
    home_button=(By.XPATH,'//a[@aria-label="Go to homepage"]')
    enter_button=(By.XPATH,'//div[@class="ml-[20px] w-[22px] h-[22px] overflow-hidden"]')
    product=(By.XPATH,'(//a[@class="aspect-square flex items-center justify-center"])[1]')


    def enter_item(self,item):
        base=BasePage(self.driver)
        self.is_visible(self.search_box)
        self.send_keys(self.search_box,item)

        self.click(self.enter_button)
        sleep(3)

        self.click(self.product)

    def click_homepage(self):
        self.click(self.home_button)




