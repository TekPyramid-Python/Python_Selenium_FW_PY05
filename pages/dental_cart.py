from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
class Cart(BasePage):
    home_button = (By.XPATH, '//a[@aria-label="Go to homepage"]')
    remove_icon=(By.XPATH,'//div[contains(@class,"absolute -top-0.5 -left-0.5 cursor-pointer bg-gray-800 rounded-full")]')
    add_wishlist=(By.XPATH,"//span[@class='text-xs font-medium mr-1.5']")
    popup_remove=(By.XPATH,"//button[normalize-space()='Remove']")
    wishlist_button=(By.XPATH,'(//div[@class="sc-81107bf9-5 hyqkWj"])[2]')
    confirmation_message=(By.XPATH,"//p[@class='text-sm font-medium']")
    def click_home_page(self):
        self.click(self.home_button)

    def add_product_to_wishlist(self):
        self.click(self.remove_icon)
        self.click(self.add_wishlist)

    def confirmation_message_is_displayed(self):
        self.is_visible(self.confirmation_message)

    def clicking_wishlist(self):
        self.is_visible(self.wishlist_button)
        self.click(self.wishlist_button)
        sleep(3)


    def remove_product(self):
        self.click(self.remove_icon)
        self.click(self.popup_remove)


    def remove_all_items_from_cart(self):
        items=self.driver.find_elements(*self.remove_icon)
        if len(items)>0:
            for item in items:
                self.click(item)
                self.click(self.driver.find_element(*self.popup_remove))
        else:
            self.click(self.home_button)







