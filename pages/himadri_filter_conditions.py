from pages.base_page import BasePage

class HimadriProductPage(BasePage):
    SORT_DROPDOWN = ('xpath', '//select[@name="orderby"]')
    FIRST_PRODUCT_PRICE = ('xpath',"((//ul[contains(@class,'products')]//li)[1]//span[contains(@class,'amount')])[2]")
    SECOND_PRODUCT_PRICE = ('xpath', "(//ul[contains(@class,'products')]//li)[9]//ins//span[contains(@class,'amount')]")

    def __init__(self, driver):
        super().__init__(driver)


    def sort_by_price_low_to_high(self):
        self.select_dropdown_by_visible_text(self.SORT_DROPDOWN,"Sort by price: low to high")

    def get_first_product_price(self):
        return self.get_text(self.FIRST_PRODUCT_PRICE)

    def get_second_product_price(self):
        return self.get_text(self.SECOND_PRODUCT_PRICE)

