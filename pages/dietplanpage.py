from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DietPlanPage(BasePage):
    SELECT_HEALTHCONDITION=(By.XPATH,"(//div[contains(.,'BREAST CANCER')])[7]")
    SCROLL_ELEMENT=(By.XPATH,"//span[.='Monday']")
    SELECT_DIETPLAN=(By.XPATH,"//a[.='Scrambled cauliflower']")
    BACK_BUTTON=(By.XPATH,"//a[.='Back to Recipes']")

    def selct_health_condition(self):
        self.logger.info(f"Selecting specific health condition")
        self.click(self.SELECT_HEALTHCONDITION)

    def select_reciepe(self):

            # 🔹 Find the element FIRST
        element = self.driver.find_element(*self.SCROLL_ELEMENT)

            # 🔹 Scroll to it
        self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                element
            )

            # 🔹 Now click the diet plan
        self.click(self.SELECT_DIETPLAN)

    def on_click_back(self):
        self.click(self.BACK_BUTTON)
