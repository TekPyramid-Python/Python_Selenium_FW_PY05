from pages.base_page import BasePage

class HimadriCartPage(BasePage):
    AQUARIUM_ACCESSORIES =('xpath','//a[text()="Aquarium Accessories"]')
    PAGE_HEADER = ('xpath','//header[@class="page-header"]')
    AQUARIUM_BLACK_LAVA_ROCK = ('xpath','//a[text()="Aquarium Black Lava Rock (1kg)"]')
    PRODUCT_ADD_TO_CART = ('xpath','(//button[@name="add-to-cart"])[2]')
    CART_ICON = ('xpath','(//a[text()="Shopping Cart"])[1]')
    CART_PRODUCT = ('xpath','//td[@class="product-name"]')
    CART_ITEMS = ('xpath','//tr[contains(@class,"cart_item")]')
    CART_ITEMS_COUNT = ('xpath','(//span[@class="wcmenucart-details count"])[2]')


    def __init__(self, driver):
        super().__init__(driver)

    def click_on_aquarium_accessories(self):
        self.click(self.AQUARIUM_ACCESSORIES)

    def click_on_aquarium_accessories_sucessful(self):
        return self.is_visible(self.PAGE_HEADER, timeout=10)

    def click_on_aquarium_black_lava_rock_product(self):
        self.click(self.AQUARIUM_BLACK_LAVA_ROCK)
        self.click(self.PRODUCT_ADD_TO_CART)

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def get_expected_product_name(self):
        return self.get_text(self.AQUARIUM_BLACK_LAVA_ROCK)

    def get_cart_product_name(self):
        return self.get_text(self.CART_PRODUCT)

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))



