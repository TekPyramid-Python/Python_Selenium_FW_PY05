from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.new_health_insurance_page import Purchase_insurance


class Digit_insurance_plan(Purchase_insurance):
    infinity_wallet_plan=(By.XPATH,"//p[contains(text(),'Infinity Wallet Plan')]")
    world_wide_treatment_plan=(By.XPATH,"//p[contains(text(),'World Wide Treatment Plan ')]")
    infinity_wallet_plan_rate=(By.XPATH,"(//p[@class='plan-amount ng-star-inserted'])[1]")
    world_wide_treatment_plan_rate = (By.XPATH, "(//p[@class='plan-amount ng-star-inserted'])[2]")
    
    def scroll_to_health_insurance(self):
        action_object=ActionChains(self.driver)
        health=self.driver.find_element(*self.world_wide_treatment_plan)
        action_object.scroll_to_element(health).perform()
        
    def prize_of_world_wide_treatment_plan(self):
        return self.get_text(self.world_wide_treatment_plan_rate)
        