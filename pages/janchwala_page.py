from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PathologyPage(BasePage):
    BOOK_TEST_LINK= (By.XPATH,"//a[.='Book a Test']")
    HEALTH_PACKAGE_LINK= (By.XPATH,"//a[.='Health Packages']")
    FULL_BODY_Link=(By.XPATH,"//a[@href='https://www.janchwala.com/janch/pack/79']")
    BOOK_NOW_BTN=(By.XPATH,"//a[@type='button']")
    ADD_PACKAGE=(By.XPATH,"//strong[.='FULL BODY EXTENSIVE JANCH']")
    ADD_PRESCIPTION=(By.ID,"fileUploader")
    CONTINUE_BTN=(By.XPATH,"//button[contains(.,'Continue')]")

    def on_click_booktest(self):
        self.logger.info(f"Attempting to select lab test")
        self.click(self.BOOK_TEST_LINK)

    def on_click_healthpackage(self):
        self.click(self.HEALTH_PACKAGE_LINK)

    def select_fullbody_package(self):
        self.click(self.FULL_BODY_Link)

    def on_click_booknow(self):
        self.click(self.BOOK_NOW_BTN)

    def enter_package(self):
        self.click(self.ADD_PACKAGE)

    def file_upload(self,file_path):

        dropzone = self.driver.find_element(*self.ADD_PRESCIPTION)

        # Execute JS to simulate a drop event
        self.driver.execute_script("""
                   var filePath = arguments[0];
                   var dropZone = arguments[1];

                   // Create a fake File object (most JS uploaders require a real file object)
                   var file = new File(['dummy content'], filePath.split('/').pop());

                   // Create a DataTransfer to simulate dropping
                   var dataTransfer = new DataTransfer();
                   dataTransfer.items.add(file);

                   // Dispatch the drop event
                   var event = new DragEvent('drop', {
                       dataTransfer: dataTransfer,
                       bubbles: true,
                       cancelable: true
                   });
                   dropZone.dispatchEvent(event);
               """, file_path, dropzone)

    def on_click_continue(self):
        self.click(self.CONTINUE_BTN)
