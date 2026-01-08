from ..pages.base_page import BasePage
from time import sleep

class RentomojoHomepage(BasePage):
    PROD_LOCATION = ("css selector", 'div.rm-listicle__block div div div:nth-child(1) a')
    PROD_LOCATION_TEXT = ("css selector", 'div.rm-listicle__block div div div:nth-child(1) a h3')
    CART_BTN = ("css selector", "div.rm-section__flex-row>button")
    DELIVERY_PINCODE_BOX = ("css selector", "input.rm-pincode__input")
    DELIVERY_PINCODE_BTN = ("css selector", "button.rm-pincode__apply-btn")
    IFREAME_DIALOG_LOCATOR = ("css selector", "div#skip")
    AC_DIALOG_PROCEED_BTN = ("css selector", "div.rm-ac-rental__dialog>div.rm-dialog__footer>button.rm-button__proceed")
    AC_INSTALLATION_BTN = ("css selector", "div.rm-ac__container>div>button.rm-btn__red")
    INSTALLATION_EXTRAINFO_PROCEED_BTN = ("css selector", "div.rm-ac__popup-container>button")
    VIEW_CART_BTN = ("css selector", "div.rm-sticky__other-cta-btns>span:nth-child(2)>a")
    GO_TO_CART_BTN = ('css selector', 'a.header-cart')
    CART_PRODUCT_NAMES = ('css selector',
                          'div.rm-products__container>div>div.rm-product__item>div>div>div>div.rm-product__content>h2>strong')
    CART_PRODUCT_DELETE_BTN = ('css selector',
                               'div.rm-products__container>div>div.rm-product__item>div>div>div>div.rm-product__content>h2>img')
    CONFIRM_DELETE_PRODUCT = ('css selector', 'div.rm-dialog__btns>ul>li>button.rm-btn__red')
    HOME_BUTTON=('css selector','div.navbar-header a')

    def redirect_to_website(self):
        self.click(self.HOME_BUTTON)

    def get_expected_product_name(self):
        expected_product_name=self.get_text(self.PROD_LOCATION_TEXT)
        return expected_product_name

    def get_actual_product_name(self):
        expected_prod_name=self.get_expected_product_name()
        self.selecting_product(self.PROD_LOCATION)
        self.switch_to_window(1)
        sleep(5)
        self.click(self.CART_BTN)
        try:
            self.send_keys(self.DELIVERY_PINCODE_BOX, "515005")
            self.click(self.DELIVERY_PINCODE_BTN)
        except Exception as e:
            self.logger.info("Delivery pincode not needed")
        try:
            self.click(self.AC_DIALOG_PROCEED_BTN)
            sleep(2)
            self.click(self.AC_INSTALLATION_BTN)
            sleep(2)
            self.click(self.INSTALLATION_EXTRAINFO_PROCEED_BTN)
            sleep(2)
        except Exception as e:
            self.logger.info("Dialog box is only for AC Products")
        self.click(self.VIEW_CART_BTN)
        sleep(15)
        actual_product_name=self.searching_for_product_cart(expected_prod_name)
        return actual_product_name


    def clearing_cart(self):
        self.redirect_to_website()
        self.click(self.GO_TO_CART_BTN)
        for i in self.driver.find_elements(*self.CART_PRODUCT_DELETE_BTN):
            self.click(i)
            self.click(self.CONFIRM_DELETE_PRODUCT)


    def searching_for_product_cart(self,product_name):
        self.redirect_to_website()
        self.logger.info('searching for product to compare')
        self.click(self.GO_TO_CART_BTN)
        for i in self.driver.find_elements(*self.CART_PRODUCT_NAMES):
            result=i.text
            self.logger.info(f' expexted product name: {product_name} and actual product name:{result}')
            if product_name in result:
                return product_name
        else:
            return None






