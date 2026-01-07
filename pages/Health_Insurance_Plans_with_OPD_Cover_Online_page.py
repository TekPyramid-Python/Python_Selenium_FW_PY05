from pages.digit_home_page import Digit_home_page
from selenium.webdriver.common.by import By

class OPD_cover_online(Digit_home_page):
    OPD_name_textfield=(By.ID,"userName")
    OPD_mobile_number_textfield = (By.ID, "userMobile")
    OPD_lets_connect_button = (By.ID, "btn-connect")
    OPD_confirmation_message=(By.ID,'btn-connect')
    
    input_OPD_name='lava'
    input_OPD_mobile_number='9998988876'
    
    def send_keys_to_OPD_name(self):
        self.send_keys(self.OPD_name_textfield,self.input_OPD_name)
        
    def send_keys_to_OPD_mobile_number(self):
        self.send_keys(self.OPD_mobile_number_textfield,self.input_OPD_mobile_number)
        
    def click_on_lets_connect(self):
        self.click(self.OPD_lets_connect_button)
        
    def get_confirmation_message_OPD(self):
        return self.get_text(self.OPD_confirmation_message)
        
        
        
    
    