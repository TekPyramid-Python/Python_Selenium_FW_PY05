from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomeRemedyPage(BasePage):
    SELECT_ILLNESS=(By.XPATH,"//a[.='Cold & Cough']")
    SCROLL_ElEMENT=(By.XPATH,"(//a[.='Doctors Apps'])[2]")


    def select_ill(self):
        self.logger.info("Get Home remedy for specific illness")
        self.click(self.SELECT_ILLNESS)

    def scorll_bottom(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    def get_doctors_apps(self):
        self.click(self.SCROLL_ElEMENT)