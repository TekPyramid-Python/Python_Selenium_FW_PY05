
from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Digit_home_page(BasePage):
    health_insurance_placeholder=(By.XPATH,'//h3[.="Health Insurance"]')
    health_image_link=((By.XPATH, "//span[@class='text-center font-semibold media768:text-[0.850rem] text-[0.800rem] mb-3'][normalize-space()='Health']"))
    opd_health_insurance_link=(By.XPATH,"//span[normalize-space()='OPD Health Insurance']")
    super_top_up_link=(By.XPATH,"//div[@class='health-card-container flex items-center rounded-lg -mt-2_5 p-5 cursor-pointer']//div//span[@class='material-icons-outlined notranslate see-more-icon hide-xs'][normalize-space()='keyboard_arrow_right']")
    arogya_sanjeevani_policy_link=(By.XPATH,"//span[normalize-space()='Arogya Sanjeevani Policy']")
    port_health_policy_link=(By.XPATH,"//span[@class='text-center font-semibold media768:text-[0.850rem] text-[0.800rem] mb-3'][normalize-space()='Port Health Policy']")
    employee_health_link=(By.XPATH,"//a[@href='https://www.godigit.com/health-insurance/group-medical-health-insurance']//img[@alt='Car']")
    business_insurance_placeholder=(By.XPATH,"//h3[.='Business Insurance']")
    D_and_O_insurance_link=(By.XPATH,"//span[.='D&O Insurance']")
    
    def __init__(self,driver):
        super().__init__(driver)
        
    def scroll_to_health_insurance(self):
        action_object=ActionChains(self.driver)
        health=self.driver.find_element(*self.health_insurance_placeholder)
        action_object.scroll_to_element(health).perform()
    
    def click_health_insurance(self):
        self.click(self.health_image_link)
        
    def click_on_OPD_health_insurance(self):
        self.click(self.opd_health_insurance_link)
    
        
        
        
    
        