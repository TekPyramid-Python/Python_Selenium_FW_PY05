# pages/itokri_searched_product_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage # Import the BasePage

class ItokriSearchedProductPage(BasePage):
    """
        Page Object for the itokri create account page (https://itokri.com/search?q=ikat%20silk%20saree).
        """
    # --- Element Locators for https://itokri.com/search?q=ikat%20silk%20saree ---
    TOTAL_COUNT=(By.XPATH,"(//div[@class='st-toolbox-left st-mr-2.5']//span)[3]")
    FIRST_PRODUCT=(By.XPATH,"//a[@class='st-leading-none st-title']/span")
    # PRODUCT_NAMES=(By.XPATH,"(//div[@class='media media--transparent media--hover-effect'])[1]")
    def get_total_count(self):
        return int(self.get_text(self.TOTAL_COUNT))

    # def click_first_product(self):
    #     self.scroll_to_element(self.PRODUCT_NAMES)
    #     self.click(self.PRODUCT_NAMES)
    def get_first_product_name(self):
        return self.get_text(self.FIRST_PRODUCT)
