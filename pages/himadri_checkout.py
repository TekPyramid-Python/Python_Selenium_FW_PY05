from pages.base_page import BasePage

class HimadriCheckout(BasePage):
    CHECKOUT_BUTTON = ('xpath','//a[contains(text(),"Proceed to checkout")]')
    CHECKOUT_PAGE_HEADER = ('xpath', '//h1[text()="Checkout"]')
    FIRST_NAME = ('id','billing_first_name')
    LAST_NAME = ('id','billing_last_name')
    STREET_1= ('id','billing_address_1')
    STREET_2= ('id','billing_address_2')
    CITY = ('id','billing_city')
    STATE = ('id','select2-billing_state-container')
    STATE_SEARCH_INPUT = ('xpath','//input[@class="select2-search__field"]')
    KERALA = ('id','select2-billing_state-result-7qa0-KL')
    PINCODE = ('id','billing_postcode')
    PHONE = ('id','billing_phone')
    EMAIL = ('id','billing_email')
    TERMS_AND_CONDITION = ('xpath','//span[contains(text(),"I have read and agree")]')


    def click_on_checkout_button(self):
        self.click(self.CHECKOUT_BUTTON)

    def is_click_on_checkout_button_sucessful(self):
        return self.is_visible(self.CHECKOUT_PAGE_HEADER, timeout=10)

    def fill_shipping_address(self,first_name,last_name,street1,street2,city,state,pincode,phone,email):
        self.send_keys(self.FIRST_NAME,first_name)
        self.send_keys(self.LAST_NAME,last_name)
        self.send_keys(self.STREET_1,street1)
        self.send_keys(self.STREET_2,street2)
        self.send_keys(self.CITY,city)
        self.select_from_custom_dropdown(self.STATE,self.STATE_SEARCH_INPUT,state)
        self.send_keys(self.PINCODE,pincode)
        self.send_keys(self.PHONE,phone)
        self.send_keys(self.EMAIL,email)

    def click_on_termsandcondition(self):
        self.click(self.TERMS_AND_CONDITION)

