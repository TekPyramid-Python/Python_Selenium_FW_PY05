# pages/itokri_product_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage # Import the BasePage

class ItokriProductPage(BasePage):
    """
        Page Object for the itokri create account page (itokri.com/products/zari-work-chiniya-silk-banarasi-saree-16-2025-990-1-16).
        """
    # --- Element Locators for itokri.com/products/zari-work-chiniya-silk-banarasi-saree-16-2025-990-1-16 ---
    CRAFT_TYPE=(By.XPATH,"(//div[@class='item_text'])[4]/p")
    ADD_TO_CART=(By.XPATH,"(//button[@type='submit'])[2]")
    PLUS_BUTTON=(By.NAME,"plus")
    MINUS_BUTTON = (By.NAME, "minus")
    ARTISAN=(By.XPATH,"//li[@data-id='artisan']")
    VERIFIED_TEXT=(By.XPATH,"//div[@class='collection_content_information']//span")
    MATERIAL=(By.XPATH,"//div[@class='item_container material_items_container']//p")
    FIRST_PRODUCT_PLUS_BUTTON=(By.XPATH,"(//div[@id='CartItem-1']//button[@name='plus'])[2]")
    def __init__(self, driver):
        # This calls the constructor of the BasePage to set up the driver, logger, etc.
        super().__init__(driver)
    def get_craft_type(self):
        return self.get_text(self.CRAFT_TYPE)
    def get_artisan_text(self):
        self.scroll_to_element(self.ARTISAN)
        self.click(self.ARTISAN)
        return self.get_text(self.VERIFIED_TEXT)
    def get_meterial_text(self):
        self.scroll_to_element(self.MATERIAL)
        return self.get_text(self.MATERIAL)
    def back_to_list(self):
        self.driver.back()
    def click_on_add_to_tokri(self):
        self.click(self.ADD_TO_CART)


