from pages.base_page import BasePage # Import the BasePage
from selenium.webdriver.common.by import By

class AddToCart(BasePage): # Make LoginPage inherit from BasePage
    Search_input = (By.XPATH, '(//input[@id="Search-In-Modal"])[1]')
    Search_button = (By.XPATH, '(//button[@class="button search__button field__button focus-inset"])[1]')
    SEARCHED_ITEM=(By.XPATH,'(//div[@class="card-product__wrapper"])[7]')
    ADD_TO_BAG=(By.XPATH,'(//button[contains(text(),"Add to bag")])[1]')
    CART=(By.XPATH,'(//a[@id="cart-icon-bubble"])[1]')
    CHECKOUT=(By.XPATH,'//div[@style="width:100%"]')
    UPI=(By.ID,'flo__payments__UPI')
    PHONEPE=(By.XPATH,'(//div[@class="listItemContainer "])[3]')
    UPI_ID=(By.ID,'upi2IdRow')

    def __init__(self, driver):
        # This calls the constructor of the BasePage to set up the driver, logger, etc.
        super().__init__(driver)

    def add_to_cart(self, search_prod,upi_id):
        """
        Performs a full login action using methods inherited from BasePage.
        """
        # self.logger.info(f"Attempting to log in with username: {username}")
        self.send_keys(self.Search_input,search_prod)
        self.click(self.Search_input)
        self.click(self.SEARCHED_ITEM)
        self.click(self.ADD_TO_BAG)
        self.click(self.CART)
        self.click(self.CHECKOUT)
        self.click(self.UPI)
        self.click(self.PHONEPE)
        self.send_keys(self.UPI_ID,upi_id)

