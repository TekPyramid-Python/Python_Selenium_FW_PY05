from selenium.webdriver.common.by import By
from pages.digit_policy_page import Policy


class Purchase_insurance(Policy):
    myself_checkbox=(By.XPATH,"//div[@class='family-details']//div[1]//checkbox-field[1]//div[1]//label[1]")
    my_spouse_checkbox=(By.XPATH,"//font[contains(text(),'My Spouse')]")
    my_son_checkbox = (By.XPATH, "//font[contains(text(),'My Son')]")
    my_daughter_checkbox = (By.XPATH, "//font[contains(text(),'My Daughter')]")
    my_father_checkbox = (By.XPATH, "//font[@dir='auto']//font[@dir='auto'][normalize-space()='My Father']")
    my_mother_checkbox = (By.XPATH, "//font[@dir='auto']//font[@dir='auto'][normalize-space()='My Mother']")
    my_father_in_law_checkbox = (By.XPATH, "//font[contains(text(),'My Father in Law')]")
    my_mother_in_law_checkbox = (By.XPATH, "//font[contains(text(),'My Mother in Law')]")
    yes_radio_button = (By.ID, 'inputID-0')
    no_radio_button = (By.ID, "inputID-1")
    continue_button=(By.ID,"continue-btn")
    age_textfield=(By.ID,'familyAge')
    marital_status=(By.XPATH,"//div[@class='marital-status-section ng-star-inserted']//select-field")
    select_unmarried=(By.XPATH,"//li[@aria-label='Unmarried']")
    select_married = (By.XPATH, "//li[@aria-label='Married']")
    select_divorced = (By.XPATH, "//li[@aria-label='Divorced']")
    select_widowed = (By.XPATH, "//li[@aria-label='Widowed']")
    
    input_age=24
    
    def click_on_my_self(self):
        self.click(self.myself_checkbox)
        
    def send_keys_to_age(self):
        self.send_keys(self.age_textfield,self.input_age)
        
    def click_on_marital_status(self):
        self.click(self.marital_status)
        
    def click_on_married(self):
        self.click(self.select_married)
        
    def click_on_no(self):
        self.click(self.no_radio_button)
    
    def click_on_yes(self):
        self.click(self.yes_radio_button)
        
    def click_on_continue(self):
        self.click(self.continue_button)
        
    
    
    
    