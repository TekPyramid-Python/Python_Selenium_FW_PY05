from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

class HomePage(BasePage):
    login_button = (By.XPATH, ' //button[contains(text(),"Login")]')
    cart_button = (By.XPATH, "//div[@class='hidden lg:block']//div[@class='px-3 py-1 bg-secondary rounded-md']")
    search_button=(By.XPATH,'//div[@class="relative left-0 text-gray-800 w-full"]')
    profile_button=(By.XPATH,'(//div[@class="sc-81107bf9-5 hKdpwQ"]/child::div[@class="sc-81107bf9-12 clYEAG"])[1]')
    product=(By.XPATH,'//a[@class="aspect-square flex items-center justify-center"]/child::img[@class="sc-dd46849a-3 lGkyU"]')
    wishlist_button = (By.XPATH,"//div[@class='hidden lg:block']//div[@class='sc-81107bf9-3 gRhygG']//div[2]//*[name()='svg']")
    category=(By.XPATH,"//div[@class='hidden lg:block']//button[@class='sc-ded8ba7e-2 kfXnqk'][normalize-space()='Category']")
    category_option=(By.XPATH,'//div[@class="flex flex-col bg-[#d7e7fa]"]//div[text()="Pharmacy "]')
    rating=(By.XPATH,"//div[@class='sc-e77cfdd3-2 jIBKUd'][normalize-space()='Rating']")
    rating_dropdown=(By.XPATH,'(//div[text()="Rating"])[2]')
    rating_checkbox=(By.XPATH,"//div[@class='sc-8e1a5422-2 kMWnaS']//div[2]//div[1]//div[1]//div[1]")
    rating_apply=(By.XPATH,"//div[@class='sc-892bc00b-0 sc-892bc00b-11 sc-1eccdb0f-8 cymOrW bbwQnM gHJRMC']")
    product_by_rating=(By.XPATH,"//a[text()='Abbott Flagyl - 400 mg Tablets']")
    brand_button=(By.XPATH,"//div[@class='hidden lg:block']//button[@class='sc-ded8ba7e-2 kfXnqk'][normalize-space()='Brand']")
    brand_option=(By.XPATH,"//body/div/div/div/div/div/div/div/div/div/div[1]/img[1]")
    recommended_button = (By.XPATH, "//div[contains(@class,'sc-62f8ef91-1 gFMkVV')]")
    sort = (By.XPATH, "//div[normalize-space()='Price- High to Low']")
    product_by_brand = (By.XPATH, "//a[normalize-space()='Waldent Intra Vue 800 Intraoral Scanner']")
    best_seller=(By.XPATH,"//div[@class='hidden lg:block']//button[@class='sc-ded8ba7e-2 kfXnqk'][normalize-space()='Best Seller']")


    def __init__(self,driver):
        super().__init__(driver)

    def is_user_logged_in(self, timeout=5):
        """
        Returns True if user is logged in, else False
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.profile_button)
            )
            return True
        except TimeoutException:
            return False

    def click_login(self):
        self.click(self.login_button)

    def click_cart(self):
        self.is_visible(self.cart_button)
        self.click(self.cart_button)

    def click_search(self):
        self.is_visible(self.search_button)
        self.click(self.search_button)

    def click_profile(self):
        self.click(self.profile_button)

    def click_product(self):
        sleep(3)
        self.scroll_to_element(self.product)
        self.is_visible(self.product)
        sleep(3)
        self.click(self.product)
        sleep(3)

    def open_wishlist(self):
        self.click(self.wishlist_button)

    def selection_by_category(self):
        self.is_visible(self.category)
        self.click(self.category)
        self.is_visible(self.category_option)
        self.click(self.category_option)
        self.is_visible(self.rating)
        self.click(self.rating)
        self.click(self.rating_checkbox)
        self.click(self.rating_apply)
        sleep(3)
        self.scroll_to_element(self.rating)
        self.click(self.product_by_rating)

    def brand_selection(self):
        self.is_visible(self.brand_button)
        self.click(self.brand_button)

        self.is_visible(self.brand_option)
        self.click(self.brand_option)
        self.click(self.recommended_button)
        self.click(self.sort)
        sleep(2)
        self.is_visible(self.product_by_brand)
        self.click(self.product_by_brand)

    def click_best_seller(self):
        self.is_visible(self.best_seller)
        self.click(self.best_seller)
        self.click(self.recommended_button)
        self.click(self.sort)





