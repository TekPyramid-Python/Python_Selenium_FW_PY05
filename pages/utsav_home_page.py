from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from pages.utsav_methods_page import UtsavMethodPage

class UtsavHomePage(UtsavMethodPage):

    UTSAV_ICON = (By.XPATH, '//a[@class="logo"]')
    SEARCH_BOX = (By.XPATH, '(//input[@type="text"])[1]')
    SEARCH_BUTTON = (By.XPATH, "//button[@class='button']")
    WISHLIST_BUTTON=(By.XPATH, "(//a[@class='guestwishlist'])[1]")
    ACCOUNT = (By.XPATH, "(//a[text()='Account'])[2]")

    SAREE_CATEGORY = (By.ID, "ui-id-2")
    MEN_CATEGORY = (By.ID, "ui-id-107")
    KURTA=(By.XPATH,'(//span[text()="Kurta"])[1]')
    KURTA_NAME=(By.XPATH,'(//a[@class="product-item-link"])[1]')
    JEWELLERY_CATEGORY = (By.ID, "ui-id-207")
    RINGS=(By.XPATH,'//span[text()="Rings"]')
    RING_NAME=(By.XPATH,'(//a[@class="product-item-link"])[3]')

    def __init__(self, driver):
        super().__init__(driver)

    def is_login_successful(self):
        """
        Checks if login was successful by looking for an element on the inventory page.
        Uses the is_visible method inherited from BasePage.
        """
        return self.is_visible(self.UTSAV_ICON, timeout=5)

    def search_product(self,saree):
        self.send_keys(self.SEARCH_BOX,saree)

    def click_search(self):
        self.click(self.SEARCH_BUTTON)

    def click_wishlist(self):
        self.click(self.WISHLIST_BUTTON)

    def mouse_hover_men(self):
        self.mouse_hover(self. MEN_CATEGORY)

    def click_on_subcategory(self):
        self.click(self.KURTA)

    def click_on_kurta_name(self):
        self.click(self.KURTA_NAME)

    def mouse_hover_jewellery(self):
        self.mouse_hover(self.JEWELLERY_CATEGORY)

    def click_on_rings(self):
        self.click(self.RINGS)

    sleep(2)
    def scroll_to_ring_name(self):
        self.scroll_to_element(self.RING_NAME)

    def click_on_ring_name(self):
        self.click(self.RING_NAME)












