from ..pages.base_page import BasePage
from ..config.environment import Environment
import allure
from time import sleep


class RentomojoStoresPage(BasePage):

    # clicking from homepage :NEAREST_STORES_BTN=("css selector","div.rm-experince-store__container div a")
    NEAREST_STORES_BTN = ("css selector", "a.rm-exp-store__footer")
    EXPECTED_STORE_NAME=("css selector","body > div:nth-child(4) > div:nth-child(8) > main:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > p:nth-child(3)")
    STORE1=("xpath","//a[@href='/bangalore/stores/cunningham-road-mojostore']")
    ACTUAL_STORE_NAME=("css selector","div[class='rm-store-address-first__container'] h1[class='rm-heading']")

    def rentomojo_srtores(self):
        with allure.step("near by rentomojo stores around you"):
            env=Environment()
            base_url=env.get_base_url()
            self.navigate_to(base_url)
            self.wait_till_pageload()
        self.click(self.NEAREST_STORES_BTN)
        self.wait_till_pageload()
        store_name=self.get_text(self.EXPECTED_STORE_NAME)
        self.click(self.STORE1)
        assert store_name==self.get_text(self.ACTUAL_STORE_NAME)
        print("store details page displaying successfully")


