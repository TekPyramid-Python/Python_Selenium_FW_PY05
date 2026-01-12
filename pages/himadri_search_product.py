from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HimadriProductSearch(BasePage):

    SERACH_ICON = ('xpath','//i[@class=" icon-magnifier"]')
    SEARCH_INPUT = ('id','ocean-search-form-2')
    SEARCH_RESULT_PRODUCTS = ('xpath','//h2[@class="search-entry-title entry-title"]')

    def search_for_product(self, product_name):
        self.click(self.SERACH_ICON)
        self.send_text_and_press_enter(self.SEARCH_INPUT, product_name)

    def result_products_names(self):
        products =  self.wait.until(EC.visibility_of_all_elements_located(self.SEARCH_RESULT_PRODUCTS))
        return [ele.text for ele in products]






