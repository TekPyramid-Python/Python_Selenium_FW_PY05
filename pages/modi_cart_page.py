from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ModiCartPage(BasePage):
    view_cart=(By.XPATH,"//a[text()='View cart']")
    size_button=(By.XPATH,'//button[@class="plus qib-button"]')
    cupon=(By.ID,'coupon_code')
    cupon_button=(By.XPATH,'//button[text()="Apply coupon"]')
    check_out=(By.LINK_TEXT,'Proceed to Checkout')

    def modi_view_cart_page(self):
      self.click(self.view_cart)
      sleep(2)

    def modi_size_button(self):
        self.click(self.size_button)
        sleep(2)


    def modi_cupon(self):
        self.send_keys(self.cupon,'pa23456')
        self.click(self.cupon)


    def modi_cart_page(self):
      self.click(self.check_out)
      sleep(3)

