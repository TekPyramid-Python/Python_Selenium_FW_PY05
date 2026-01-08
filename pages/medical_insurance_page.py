
from selenium.webdriver.common.by import By
from pages.digit_home_page import Digit_home_page


class Medical_insurance_page(Digit_home_page):
    pin_code_textfield=(By.XPATH,"//input[@id='resident-pincode-input']")
    mobile_number_textfield=(By.XPATH,"//input[@id='health-mob']")
    view_prize_button=(By.XPATH,"//button[@class='getquote-btn-primary'][normalize-space()='View Prices']")
    
    pin_code_text=560073
    mobile_number=8073036315
    
    def send_keys_to_pincode(self):
        self.send_keys(self.pin_code_textfield,self.pin_code_text)
        
    def send_keys_to_mobile_number(self):
        self.send_keys(self.mobile_number_textfield,self.mobile_number)
        
    def click_on_view_prize(self):
        self.click(self.view_prize_button)
        
    
        
    
    
    