from ..pages.base_page import BasePage


class Furniture_Module(BasePage):
    #MODULE
    FURNITURE_MODULE_BTN=("css selector","div.rm-category__home>div>div:nth-child(2)>div>ul>li:nth-child(2)>a")
    #Sub Module
    ROOM_TYPE_BEDROOM_BTN=("css selector","div.category-block-filterBlocks>div>div")
    #product
    BEDROOM_PRODUCT=("css selector","div.rm-category__container>div:nth-child(1)>a>div")
    PRODUCT_NAME=('css selector','div.rm-category__container>div>a>div>p')


    CART_BTN = ("css selector", "div.rm-section__flex-row>button")
    VIEW_CART_BTN = ("css selector", "div.rm-sticky__other-cta-btns>span:nth-child(2)>a")
    GO_TO_CART_BTN=('css selector','a.header-cart')
    CART_PRODUCT_NAMES=('css selector','div.rm-products__container>div>div.rm-product__item>div>div>div>div.rm-product__content>h2>strong')
    CART_PRODUCT_DELETE_BTN=('css selector','div.rm-products__container>div>div.rm-product__item>div>div>div>div.rm-product__content>h2>img')
    CONFIRM_DELETE_PRODUCT=('css selector','div.rm-dialog__btns>ul>li>button.rm-btn__red')
    DELIVERY_PINCODE_BOX = ("css selector", "input.rm-pincode__input")
    DELIVERY_PINCODE_BTN = ("css selector", "button.rm-pincode__apply-btn")




    def adding_furniture_product(self):
        self.click(self.FURNITURE_MODULE_BTN)
        self.click(self.ROOM_TYPE_BEDROOM_BTN)
        self.scroll_to_element(self.BEDROOM_PRODUCT)
        self.click(self.BEDROOM_PRODUCT)
        product_name=self.get_text(self.PRODUCT_NAME)
        self.logger.info(product_name)
        self.switch_to_window(1)
        self.click(self.CART_BTN)
        try:
            self.send_keys(self.DELIVERY_PINCODE_BOX,"515005")
            self.click(self.DELIVERY_PINCODE_BTN)
        except Exception as e:
            self.logger.info("Delivery pincode not needed")
        self.navigate_to('https://www.rentomojo.com/bangalore')
        actual_product_name=self.searching_for_product_cart(product_name)
        assert product_name==actual_product_name,'product not added to cart'
        self.logger.info(f'{product_name} is present in cart')


    def clearing_cart(self):
        self.navigate_to('https://www.rentomojo.com/bangalore')
        self.click(self.GO_TO_CART_BTN)
        for i in self.driver.find_elements(*self.CART_PRODUCT_DELETE_BTN):
            self.click(i)
            self.wait_till_pageload()
            self.click(self.CONFIRM_DELETE_PRODUCT)


    def searching_for_product_cart(self,product_name):
        self.logger.info('searching for product to compare')
        self.click(self.GO_TO_CART_BTN)
        for i in self.driver.find_elements(*self.CART_PRODUCT_NAMES):
            result=i.text
            self.logger.info(f'expexted product name: {product_name} and actual product name:{result}')
            if product_name in result:
                return product_name
        else:
            return None


