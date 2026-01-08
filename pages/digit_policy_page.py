from selenium.webdriver.common.by import By
from pages.medical_insurance_page import Medical_insurance_page


class Policy(Medical_insurance_page):
    new_health_insurance_link=(By.XPATH,"//div[normalize-space()='Health Insurance Policy']")
    super_top_up_policy_link=(By.XPATH,"//div[@class='health-card-container flex items-center rounded-lg -mt-2_5 p-5 cursor-pointer']//div//span[@class='material-icons-outlined notranslate see-more-icon hide-xs'][normalize-space()='keyboard_arrow_right']")
    existing_policy_link=(By.XPATH,"//div[normalize-space()='Switch Existing health policy']")
    super_top_up_pop_up=(By.XPATH,"//div[@class='font-bold text-base pt-1']")
    super_top_up_enter_mobile_number=(By.XPATH,"//input[@type='text']")
    confirmation_message=(By.XPATH,"//div[@class='font-bold text-base pt-1 text-center']")
    confirmation_ok_button=(By.XPATH,"//button[@type='submit']")
    pop_up_get_a_call_back_button=(By.XPATH,"//button[normalize-space()='Get a Call back']")
    existing_policy_pop_up=(By.XPATH,"//div[@class='font-bold text-base pt-1']")
    existing_policy_enter_mobile_number = (By.XPATH, "//input[@type='text']")
    existing_policy_pop_up_get_a_call_back_button = (By.XPATH, "//button[normalize-space()='Get a Call back']")
    existing_policy_confirmation_message = (By.XPATH, "//div[@class='font-bold text-base pt-1 text-center']")
    existing_policy_confirmation_ok_button = (By.XPATH, "//button[@type='submit']")
    
    
    
    input_mobile_number = 8787899976
    input_existing_policy_enter_mobile_number=9898777776
    
    def click_on_new_health_insurance(self):
        self.click(self.new_health_insurance_link)
        
    def click_on_super_top_up_policy(self):
        self.click(self.super_top_up_policy_link)
        
    def click_on_existing_policy(self):
        self.click(self.existing_policy_link)
        
    def text_super_pop_up(self):
        return self.get_text(self.super_top_up_pop_up)
        
    def send_keys_super_top_up_mobile_number(self):
        self.send_keys(self.super_top_up_enter_mobile_number,self.input_mobile_number)
        
    def click_on_get_a_call_back(self):
        self.click(self.pop_up_get_a_call_back_button)
        
    def text_confirmation_message(self):
        return self.get_text(self.confirmation_message)
    
    def click_on_ok_button(self):
        self.click(self.confirmation_ok_button)
        
    def text_excicting_plan_popup(self):
        return self.get_text(self.existing_policy_pop_up)

    def send_existing_policy_mobile_number(self):
        self.send_keys(self.existing_policy_enter_mobile_number, self.input_existing_policy_enter_mobile_number)

    def click__existing_policy_on_get_a_call_back(self):
        self.click(self.existing_policy_pop_up_get_a_call_back_button)

    def text_confirmation_message_existing_policy(self):
        return self.get_text(self.confirmation_message)

    def click_on_ok_button_existing_policy(self):
        self.click(self.confirmation_ok_button)
    
        
    
        
    
        
        