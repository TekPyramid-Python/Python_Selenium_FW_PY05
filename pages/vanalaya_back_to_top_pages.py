from selenium.webdriver.common.by import By

from pages.vanalaya_methods_page import VanalayaMethods

class BackTopPages(VanalayaMethods):
    BACK_TO_TOP_BUTTON = (By.ID,'footer-btn-scroll-top')
    LOGO = (By.CSS_SELECTOR,'div.description.rte.lh-sm')
    BLOG_BUTTON = (By.XPATH, '(//a[contains(text(),"Blog")])[1]')
    CONTACT_CLICK = (By.CSS_SELECTOR, 'div.col-10>ul li.nav-item.dropdown:nth-child(5)')
    HOME_PAGE = (By.XPATH,"(//a[contains(text(),'Home')])[1]")



    def __init__(self,driver):
        super().__init__(driver)

    # def back_top(self):

    def scroll_down_home(self):
        self.scroll_to_elements(self.BACK_TO_TOP_BUTTON)
        self.logger.info("Scroll to Back to Top button.")

    def click_b2top_button_from_home(self):
        self.click(self.BACK_TO_TOP_BUTTON)
        self.logger.info("Clicked back to top button from home page")

    def click_blog_button(self):
        self.click(self.BLOG_BUTTON)
        self.logger.info("Clicked Blog Page Back To Top Button")

    def scroll_down_from_blog(self):
        self.scroll_to_elements(self.BACK_TO_TOP_BUTTON)
        self.logger.info("Scroll to Back to Top button.")

    def click_b2top_button_from_blog(self):
        self.click(self.BACK_TO_TOP_BUTTON)
        self.logger.info("Clicked back to top button from blog page")

    def click_contact_button(self):
        self.click(self.CONTACT_CLICK)
        self.logger.info("Clicked Blog Page Back To Top Button")

    def scroll_down_contact(self):
        self.scroll_to_elements(self.BACK_TO_TOP_BUTTON)
        self.logger.info("Scroll to Back to Top button.")

    def click_b2top_button_from_contact(self):
        self.click(self.BACK_TO_TOP_BUTTON)
        self.logger.info("Clicked back to top button from contact page")

    def is_logo_successful(self):
        return self.is_visible(self.LOGO, timeout=5)




