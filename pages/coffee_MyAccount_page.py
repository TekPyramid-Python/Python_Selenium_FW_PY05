# pages/MyAccount_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage # Import the BasePage

class MyAccount(BasePage): # Make MyAccount inherit from BasePage
    """
    Page Object for the total.coffee.com login page.
    """
    # --- Element Locators for total.coffee.com ---
   # Element on the page after successful login
    HELLO_USER = (By.XPATH, '//span[@class="nm-username"]')
    LOGOUT = (By.XPATH,'//li/a[contains(text(),"Log out")]')



    def is_login_successful(self):
        """
        Checks if login was successful by looking for an element on the My Account page.
        Uses the is_visible method inherited from BasePage.
        """
        return self.is_visible(self.HELLO_USER, timeout=10)

    def logout(self):
        self.click(self.LOGOUT)


