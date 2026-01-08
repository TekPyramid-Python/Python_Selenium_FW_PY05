from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BlogPage(BasePage):

    BLOG_BUTTON = (By.XPATH,'(//a[contains(text(),"Blog")])[1]')
    BLOG_IMAGE = (By.CSS_SELECTOR,"div.col-4 img")
    SCROLL_DOWN = (By.CSS_SELECTOR,'div#footer-copyright div.fs-sm.text-center')
    ENTER_EMAIL_ID = (By.XPATH,'//div[@id="footer-desktop"]//form')
    CLICK_SUBMIT = (By.XPATH,'(//button[@aria-label="Subscribe"])[3]')
    BLOG_PAGE_HEADER = (By.XPATH,'(//nav[@id="navbar-desktop"]/descendant::a)[1]')  # Element on the page after successful login
    # POP_UP = (By.XPATH,'(//button[@aria-label="Close"])[1]')
    BUY_THEME = (By.XPATH,"(//a[contains(text(),'Buy Theme')])[1]")
    def __init__(self,driver):
        super().__init__(driver)
    def click_blog_button(self):
        self.click(self.BLOG_BUTTON)
        self.logger.info("Clicked the Blog button.")

    def click_blog_image(self):
        self.click(self.BLOG_IMAGE)
        self.logger.info("Clicked the Blog image")

    def scroll_down(self):
        self.scroll_to_element(self.SCROLL_DOWN)
        self.logger.info("Scroll to bottom of the Submit button")

    def enter_email(self,email):
        self.js_send_keys(self.ENTER_EMAIL_ID, email) #enter email in test
        self.logger.info(f"Entered the Email ID:{email}")

    def click_submit(self):
        self.click(self.CLICK_SUBMIT)
        self.logger.info("Clicked the Submit button")
    def is_subscribe_successful(self):
        """
        Checks if login was successful by looking for an element on the inventory page.
        Uses the is_visible method inherited from BasePage.
        """
        return self.is_visible(self.BLOG_PAGE_HEADER, timeout=5)






