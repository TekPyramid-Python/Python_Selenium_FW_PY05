# pages/coffee_subscription_page.py
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage



class SubscriptionPage(BasePage): # Make SubscriptionPage inherit from BasePage

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    BREW_METHOD = (By.XPATH, '(//span/span[@class="sod_label"])[1]')
    COFFEE_ADDITIVES = (By.XPATH, '(//span/span[@class="sod_label"])[2]')
    ROAST_LEVEL = (By.XPATH, '(//span/span[@class="sod_label"])[3]')
    COFFEE_TASTE = (By.XPATH, '(//span/span[@class="sod_label"])[4]')
    GRIND_SIZE = (By.XPATH, '(//span/span[@class="sod_label"])[5]')
    PACK_SIZE = (By.XPATH, "(//li[@class='nm-variation-option'])[1]")
    FREQUENCY = (By.XPATH, '(//span/span[@class="sod_label"])[6]')
    SUBSCRIPTION_PERIOD = (By.XPATH,'(//span/span[@class="sod_label"])[7]')
    SIGNUP_BTN = (By.XPATH,'//div/button[contains(text(),"Sign up now")]')
    # OPTIONS
    POUR_OVER = (By.XPATH,'(//span[@class="sod_list"]/span)[3]')
    WATER = (By.XPATH, '(//span[@class="sod_list"])[2]/span[2]')
    LEAVE_IT_TO_U = (By.XPATH, '(//span[@class="sod_list"])[3]/span[5]')
    SURPRISE = (By.XPATH, '(//span[@class="sod_list"])[4]/span[7]')
    GROUND = (By.XPATH, '(//span[@class="sod_list"])[5]/span[2]')
    TWICE = (By.XPATH, '(//span[@class="sod_list"])[6]/span[3]')
    THREE_MONTH = (By.XPATH, '(//span[@class="sod_list"])[7]/span[2]')
    VIEW_BASKET = (By.XPATH, '(//a[contains(text(),"View basket")])[2]')


    # Dropdown selection methods
    def coffee_preparation(self):
        self.click(self.BREW_METHOD)
        time.sleep(2)
        self.click(self.POUR_OVER)
        self.click(self.COFFEE_ADDITIVES)
        self.click(self.WATER)
        time.sleep(2)
        self.click(self.ROAST_LEVEL)
        self.click(self.LEAVE_IT_TO_U)
        time.sleep(2)
        self.click(self.COFFEE_TASTE)
        self.click(self.SURPRISE)
        time.sleep(2)
        self.click(self.GRIND_SIZE)
        self.click(self.GROUND)
        time.sleep(2)
        self.click(self.PACK_SIZE)
        time.sleep(2)
        self.click(self.FREQUENCY)
        self.click(self.TWICE)
        time.sleep(2)
        self.click(self.SUBSCRIPTION_PERIOD)
        self.click(self.THREE_MONTH)
        self.scroll_to_element(self.SIGNUP_BTN)
        self.wait_for_element(self.SIGNUP_BTN)
        time.sleep(5)
        self.click(self.SIGNUP_BTN)
        self.scroll_to_element(self.VIEW_BASKET)
        self.wait_for_element(self.VIEW_BASKET)
        self.click(self.VIEW_BASKET)
        time.sleep(2)

    def get_selected_brew_method(self):
        element = self.driver.find_element(*self.BREW_METHOD)
        return Select(element).first_selected_option.text

    def get_selected_pack_size(self):
        element = self.driver.find_element(*self.PACK_SIZE)
        return Select(element).first_selected_option.text





