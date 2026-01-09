from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DoctorListPage(BasePage):
    SPECIALITY_CHECKBOX= (By.ID, "chkSpl2")
    SELECT_DOCTOR_PROFILE= (By.XPATH, "//small[contains(text(),'PROFILE')]")
    SELECT_DATE= (By.XPATH, "(//button)[4]")
    CONTINUE_BTN= (By.ID, "docConf")

    def select_speciality(self):
        self.logger.info(f"Attempting to select speciality")
        self.click(self.SPECIALITY_CHECKBOX)

    def select_doctor_profile(self):
        self.logger.info(f"Attempting to view doctor profile")
        self.click(self.SELECT_DOCTOR_PROFILE)

    def select_appointment_date(self):
        self.click(self.SELECT_DATE)

    def click_continue(self):
        self.click(self.CONTINUE_BTN)