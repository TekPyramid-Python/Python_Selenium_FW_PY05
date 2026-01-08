# pages/cart_page.py

# from pages.base_page import BasePage
# from selenium.webdriver.common.by import By
#
#
# class CartPage(BasePage):
#     """
#     Page Object for the Sauce Labs Demo Shopping Cart page.
#     """
#     # --- Locators ---
#     CHECKOUT_BUTTON = (By.ID, "checkout")
#
#     # Dynamic locator for a specific item name in the cart
#     ITEM_NAME_TEXT = (By.XPATH, "//div[@class='inventory_item_name' and text()='{}']")
#
#     def __init__(self, driver):
#         super().__init__(driver)
#
#     def is_item_in_cart(self, item_name):
#         """
#         Verifies if a specific item is visible in the cart.
#
#         Args:
#             item_name (str): The name of the item to check for.
#
#         Returns:
#             bool: True if the item is visible, False otherwise.
#         """
#         item_locator = (self.ITEM_NAME_TEXT[0], self.ITEM_NAME_TEXT[1].format(item_name))
#         return self.is_visible(item_locator)
#
#     def click_checkout(self):
#         """Clicks the 'Checkout' button."""
#         self.click(self.CHECKOUT_BUTTON)
#         self.logger.info("Clicked the Checkout button.")

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):

    CART_ITEM = (By.CSS_SELECTOR, ".cart__items, .cart-items")
    CART_ICON = (By.XPATH, "//a[contains(@href,'/cart')]")

    def open_cart(self):
        self.js_click(self.CART_ICON)
        self.wait.until(EC.presence_of_element_located(self.CART_ITEM))

    def is_product_present(self):
        return self.is_visible(self.CART_ITEM)
