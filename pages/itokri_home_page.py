# pages/itokri_home_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage # Import the BasePage

class ItokriHomePage(BasePage):
    """
        Page Object for the itokri homepage page (itokri.com).
        """
    # --- Element Locators for itokri.com ---
    CROSS_BUTTON=(By.XPATH,"//div[@class='flex flex-col justify-center']")
    LOGIN_LOGO = (By.XPATH, "(//a[@onclick='window.otpOpen(event)'])[3]")
    SEARCH_BOX=(By.XPATH,"(//input[@name='st'])[1]")
    NEW_MENU=(By.XPATH,"//a[@data-submenu='new']")
    SAREES_MENU=(By.XPATH,"//a[@data-submenu='sarees']")
    HOME_DECOR_MENU=(By.XPATH,"//a[@data-submenu='home-decor']")
    DUPATTAS_MENU = (By.XPATH, "//a[@data-submenu='dupattas-stoles']")
    BANARARI_SAREE=(By.XPATH,"//a[text()='Banarasi Saree']")
    AJRAKH_DUPATTA=(By.XPATH,"//a[text()='Ajrakh Dupatta']")
    KALAMKARI_CUSHION_COVERS=(By.XPATH,"//a[text()='Kalamkari Cushion Covers']")
    def __init__(self, driver):
        # This calls the constructor of the BasePage to set up the driver, logger, etc.
        super().__init__(driver)
    def click_cross_button(self):
        self.click(self.CROSS_BUTTON)
    def login_icon(self):
        self.click(self.LOGIN_LOGO)
    def is_home_page_visible(self):
        """Verifies if the login page is displayed by checking for the title."""
        if "iTokri l Authentic Indian Textiles & Handicrafts Online l Since 2012" in self.get_title():
            return True
        return False
    def product_select(self):
        self.hover(self.SAREES_MENU)
        self.click(self.BANARARI_SAREE)
    def search_product(self,product):
        self.send_keys(self.SEARCH_BOX,product)
    def dupatta_select(self):
        self.hover(self.DUPATTAS_MENU)
        self.click(self.AJRAKH_DUPATTA)
    def home_decor_select(self):
        self.hover(self.HOME_DECOR_MENU)
        self.click(self.KALAMKARI_CUSHION_COVERS)
