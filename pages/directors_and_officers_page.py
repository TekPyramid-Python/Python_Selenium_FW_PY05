import allure
from selenium.webdriver.common.by import By

from pages.digit_home_page import Digit_home_page
from tests.base_test import BaseTest


class Directors_and_Officers(Digit_home_page):
    D_and_O_name_textfiled=(By.XPATH,"//input[@id='garage-city']")
    D_and_O_mobile_number_textfield = (By.XPATH, "//input[@placeholder='Mobile Number']")
    D_and_O_email_textfield = (By.XPATH, "//input[@placeholder='Enter Your Email']")
    D_and_O_next_button = (By.XPATH, "//button[@class='btn next']")
    D_and_O_company_name=(By.XPATH,"//input[@placeholder='Company Name']")
    D_and_O_pincode=(By.XPATH,"//input[@placeholder='Pincode']")
    D_and_O_number_of_employee=(By.XPATH,"//input[@placeholder='Number Of Employee']")
    D_and_O_industry_category_drop_down=(By.XPATH,"//div[@class='arrow-cus']")
    D_and_O_select_banking_and_finance=(By.XPATH,"//label[normalize-space()='Banking Finance and Insurance']")
    D_and_O_sum_insured=(By.XPATH,"//input[@placeholder='Liability/Sum Insured']")
    D_and_O_yes_registered_india_radio_button=(By.XPATH,"//label[normalize-space()='Yes']//span[@class='check']")
    D_and_O_no_registered_india_radio_button = (By.XPATH, "//label[normalize-space()='No']//span[@class='check']")
    D_and_O_confirmation_text=(By.XPATH,"//p[@class='mail-content']")
    
    
    
    input_user_name='lavanya'
    input_mobile_number='9876789990'
    input_email='lavanya@gmail.com'
    input_company_name='indegene'
    input_pincode='561203'
    input_number_of_employee='900'
    input_sum_insured='100000'

    def __init__(self, driver):
        super().__init__(driver)
    
    def send_user_name(self):
        self.send_keys(self.D_and_O_name_textfiled,self.input_user_name)
        
    def send_mobile_number(self):
        self.send_keys(self.D_and_O_mobile_number_textfield,self.input_mobile_number)
        
    def send_email(self):
        self.send_keys(self.D_and_O_email_textfield,self.input_email)
        
    def click_on_next_button(self):
        self.click(self.D_and_O_next_button)
        
    def send_company_name(self):
        self.send_keys(self.D_and_O_company_name,self.input_company_name)
        
    def send_pincode(self):
        self.send_keys(self.D_and_O_pincode,self.input_pincode)
        
    def send_number_employee(self):
        self.send_keys(self.D_and_O_number_of_employee,self.input_number_of_employee)
        
    def select_industry_category(self):
        self.click(self.D_and_O_industry_category_drop_down)
        self.click(self.D_and_O_select_banking_and_finance)
        
    def send_sum_insured(self):
        self.send_keys(self.D_and_O_sum_insured,self.input_sum_insured)
        
    def click_on_no(self):
        self.click(self.D_and_O_no_registered_india_radio_button)
        
    def confirmation_text(self):
        return self.get_text(self.D_and_O_confirmation_text)
        
    
        
        
    
        
    
    