from pages.base_page import BasePage
import re
from selenium.webdriver.common.by import By
from pages.dental_home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep


class Product(BasePage):
    add=(By.XPATH,'(//div[text()="Add"])[1]')
    minus=(By.XPATH,'(//div[@class="sc-892bc00b-0 sc-27787fb3-2 cymOrW MQqgI"]/child::div)[1]')
    cart=(By.XPATH,'(//div[@class="flex flex-col"]/child::span)[1]')
    feedback=(By.XPATH,"//span[@class='sc-3f12ad5a-0 sc-6fb080ab-3 jwXQhM ifPTeN']")
    profile_button = (By.XPATH, '(//div[@class="sc-81107bf9-5 hKdpwQ"]/child::div[@class="sc-81107bf9-12 clYEAG"])[1]')
    product_quality=(By.XPATH,"//input[@id='product_quality']")
    product_price=(By.XPATH,"//input[@id='product_price']")
    product_feedback=(By.XPATH,"//input[@id='other_feedback']")
    product_prices = (By.XPATH, '//span[@class="text-[16px] font-semibold text-primary"]')
    def is_add_present(self):
        try:
            WebDriverWait(self.driver, timeout=5).until(
                EC.visibility_of_element_located(self.add)
            )
            return True
        except TimeoutException:
            return False

    def add_product(self):
        self.click(self.add)

    def click_cart(self):
        self.click(self.cart)
        sleep(3)

    def click_minus(self):
        self.click(self.minus)

    def enter_feedback(self,text,price,feed):
        self.click(self.feedback)
        self.send_keys(self.product_quality,text)
        self.send_keys(self.product_price,price)
        self.send_keys(self.product_feedback,feed)


    def click_profile(self):
        self.click(self.profile_button)

    def get_all_product_prices(self):
        prices = self.driver.find_elements(*self.product_prices)

        price_list = []

        for price in prices:
            text = price.text  # ₹1,299
            amount = int(re.sub(r"[^\d]", "", text))
            price_list.append(amount)


        return price_list


