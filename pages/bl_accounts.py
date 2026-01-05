from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


from pages.base_page import BasePage

import time

class Accounts(BasePage):
    SHOP=(By.CSS_SELECTOR,"a[class='qKN3X Pw7Nz IeWK2 zVVUm']")
    # MAINSHOP=(By.CSS_SELECTOR,".menu__item.text-sm-lg.flex.items-center.font-medium.z-2.relative.cursor-pointer")
    MAINSHOP=(By.XPATH,"(//span[.='Shop'])[3]")
    COPPER_ITEM=(By.XPATH,"//a[.='Copper']")
    REVIEWBTN=(By.XPATH,"//a[.='View my Reviews page']")
    menu=(By.XPATH,"//button[@aria-label='Show Account menu']")
    profile=(By.XPATH,"(//a[@class='qKN3X Pw7Nz tzYzK T0H0Y zVVUm'])[1]")



    def select_shop(self):
        shop_element = self.wait_for_element(self.SHOP)
        shop_element.click()
        # time.sleep(20)

        shop_hover = self.wait_for_element(self.MAINSHOP)
        ActionChains(self.driver).move_to_element(shop_hover).perform()

    def select_copper(self):
        self.click(self.COPPER_ITEM)

    def select_review(self):
        self.click(self.REVIEWBTN)


    def select_shop1(self):
        shop_element = self.wait_for_element(self.SHOP)
        shop_element.click()

    def selct_menu(self):
        self.click(self.menu)

    def click_on_profile(self):
        self.click(self.profile)


