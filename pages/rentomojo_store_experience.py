from ..pages.base_page import BasePage

class RentomojoStoresPage(BasePage):

    # clicking from homepage :NEAREST_STORES_BTN=("css selector","div.rm-experince-store__container div a")
    NEAREST_STORES_BTN = ("css selector", "a.rm-exp-store__footer")
    EXPECTED_STORE_NAME=("css selector","body > div:nth-child(4) > div:nth-child(8) > main:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > p:nth-child(3)")
    STORE1=("css selector","div.rm-store-listing__container>div>div>div>div>div>div>img")
    ACTUAL_STORE_NAME=("css selector","div[class='rm-store-address-first__container'] h1[class='rm-heading']")

    def rentomojo_get_expected_name(self):
        self.click(self.NEAREST_STORES_BTN)
        self.wait_till_pageload()
        store_name=self.get_text(self.EXPECTED_STORE_NAME)
        return store_name
    def rentomojo_get_actual_name(self):
        self.click(self.STORE1)
        actual_store_name=self.get_text(self.ACTUAL_STORE_NAME)
        self.logger.info("store details page displaying successfully")
        return actual_store_name

