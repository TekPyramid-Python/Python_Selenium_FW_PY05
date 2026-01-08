import re
from pages.base_page import BasePage


class ShopAll_Validation(BasePage):

    SHOP_ALL = ('xpath','//span[text()="Shop All"]')
    PRODUCT_LIST = ('xpath','// ul[ @class ="product-categories"]//a')
    PRODUCT_CATEGORY_HEADER = ('xpath','//h4[text()="Product categories"]')
    PRODUCT_TITLE = ('xpath', '//h1[@class="page-header-title clr"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_shopall(self):
        self.click(self.SHOP_ALL)

    def is_clickon_shopall_successful(self):
        return self.is_visible(self.PRODUCT_CATEGORY_HEADER, timeout=5)

    def validating_productname_in_productcategories(self):
        products = self.wait_for_presence(self.PRODUCT_LIST)
        product_count = len(products)
        # print(product_count)

        for index in range(product_count):
            products = self.wait_for_presence(self.PRODUCT_LIST)
            product_name = products[index].text.upper()
            only_text = re.sub(r'[^A-Za-z0-9]+$', '', product_name).strip()
            # print(only_text)
            products[index].click()
            opened_product = self.wait_for_visibility(self.PRODUCT_TITLE)
            opened_text = opened_product.text.upper()
            # print(opened_text)
            try:
                assert only_text in opened_text
            except AssertionError:
                print(f"Expected {only_text}, but opened {opened_text}")
            self.driver.back()
