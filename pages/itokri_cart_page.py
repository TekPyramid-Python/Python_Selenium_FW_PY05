# pages/itokri_cart_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage # Import the BasePage

class ItokriHomePage(BasePage):
    """
        Page Object for the itokri cart page (itokri.com/cart).
        """
    # --- Element Locators for itokri.com/cart ---
    CHECKOUT=(By.XPATH,"(//button[@id='checkout'])[1]")
    ITEMS_PRESENT=(By.XPATH,"//div[@class='cart-item']//div[@class='cart-item__name-cart-wrapper']/a")