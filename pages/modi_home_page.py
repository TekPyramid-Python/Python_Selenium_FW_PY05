from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
class ModiHomePage(BasePage):
    search_product = (By.XPATH, '//input[@name="s"]')
    button = (By.XPATH, '//a[@class="shopengine-search-more-btn"]')
    brand_hover=(By.XPATH,'//span[@class="e-n-menu-dropdown-icon-closed"]')
    brand_product=(By.XPATH,'(//div[@class="elementor-image-box-content"])[2]//a')
    blog=(By.XPATH,'(//span[@class="e-n-menu-title-text"])[2]')
    recipes=(By.XPATH,'(//span[@class="e-n-menu-title-text"])[3]')
    cart_icon=(By.XPATH,'//a[@id="elementor-menu-cart__toggle_button"]')
    login_icon=(By.XPATH,'//a[@class="elementor-icon"]')

    def nav_to_login(self):
        self.click(self.login_icon)

    def modi_home_page(self):
        self.send_keys(self.search_product,'olive oil')
        self.click(self.button)

    def brand_hover_method(self):
        self.hover_to_element(self.brand_hover)
        self.click(self.brand_product)

    def blog_method(self):
        self.click(self.blog)

    def recepi_method(self):
        self. click( self.recipes)
        # self.click(self.cart_icon)

