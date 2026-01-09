from selenium.webdriver.common.by import By
from pages.vanalaya_methods_page import VanalayaMethods


class ReviewPage(VanalayaMethods):

    CLICK_DROP_DOWN = (By.XPATH,'(//div[@class="col-10"]/ul/li)[2]')
    LOGO = (By.CSS_SELECTOR,'div.description.rte.lh-sm')
    SELECT_PRODUCT = (By.XPATH,"(//li/h6[contains(text(),'Instant Coffee')])[1]")
    CLICK_PRODUCT_IMAGE = (By.XPATH,'(//div[@class="product-image-wrapper"]//img)[1]')
    SCROLL_2_REVIEW = (By.XPATH,"//h2[text()='Customer Reviews']")
    CLICK_WRITE_REVIEW = (By.XPATH, "//a[text()='Write a review']")
    RATING_3_STAR_1 = (By.XPATH,'(//div[@aria-label="Rating"]/a)[3]')
    WRITE_REVIEWS_1 = (By.CSS_SELECTOR,'textarea#jdgm-review-body-input')
    CLICK_NEXT_1 = (By.XPATH,"//button[contains(text(),'Next')]")
    ENTER_EMAIL = (By.CSS_SELECTOR,"input#jdgm-email-input")
    TEXT_VISIBLE = (By.XPATH,"//div[contains(text(),'About you')]")
    SHARE_PICTURE = (By.XPATH,"//div[contains(text(),'Share a picture')]")
    CLICK_TO_UPLOAD = (By.XPATH,"//b[text()='Click to upload']")
    SHARE_DUMMY_IMAGE = (By.XPATH, "//input[@type='file']")
    UPLOAD_COMPLETE = (By.XPATH,'//div[@data-type="image"]')

    # SHARE_DUMMY_IMAGE = (By.CSS_SELECTOR, "div[class$='form-group--share-media']")
    CLICK_NEXT_2 = (By.XPATH,'''//div[@class="jdgm-write-review-modal__content"]//button[contains(text(),'Next')]''')
    THANKYOU_TEXT = (By.XPATH,"//div[contains(text(),' Thanks for your review!')]")
    RATING_3_STAR_2 = (By.XPATH,'(//a[@title="3 stars"])[4]')
    CLICK_CLOSE_BUTTON = (By.XPATH,"//button[contains(text(),'Close')]")
    WRITE_REVIEWS_2 = (By.CSS_SELECTOR, 'textarea#jdgm-review-body-input')
    CLICK_NEXT_3 = (By.XPATH, "//button[contains(text(),'Next')]")
    CLICK_NEXT_4 = (By.XPATH, "//button[contains(text(),'Next')]")

    def __init__(self,driver):
        super().__init__(driver)

    # def review_page(self,review_text,email,path):

    def click_drop_down(self):
        self.click(self.CLICK_DROP_DOWN)
        self.logger.info('Dropdown is displayed')

    def select_product(self):
        self.click(self.SELECT_PRODUCT)
        self.logger.info('Selecting a product')

    def click_product_image(self):
        self.click(self.CLICK_PRODUCT_IMAGE)
        self.logger.info('Click product image')

    def scroll_towards_element(self):
        self.scroll_to_elements(self.SCROLL_2_REVIEW)
        self.logger.info('Scroll to write a review and click')

    def click_to_write_review(self):
        self.click(self.CLICK_WRITE_REVIEW)
        self.logger.info('click Write a Review button')

    def click_for_rating(self):
        self.click(self.RATING_3_STAR_1)
        self.logger.info('Giving Rating 3')

    def write_review(self,review_text):
        self.send_keys(self.WRITE_REVIEWS_1,review_text)
        self.logger.info(f'Enter a Review: {review_text}')

    def click_next_btn_from_review_page(self):
        self.click(self.CLICK_NEXT_1)
        self.logger.info('Click button from review page')

    def wait_and_enter_email_id(self,email):
        self.wait_for_dom_ready()
        self.send_keys(self.ENTER_EMAIL,email)
        self.logger.info(f'Enter a Email: {email}')

    def click_next_btn_from_email_id(self):
        self.wait_for_dom_ready()
        self.click(self.CLICK_NEXT_1)
        self.logger.info('click next button')

    def upload_dummy_image(self,path):
        self.upload_file(self.SHARE_DUMMY_IMAGE,path)
        self.logger.info(f'Enter Dummy Image Path: {path}')

    def wait_and_click_next_btn_from_dummy_image(self):
        self.wait_and_click(self.CLICK_NEXT_2)
        self.logger.info('click next button')

    def wait_and_give_rating(self):
        self.click(self.RATING_3_STAR_2)
        self.logger.info('Giving Rating 3')

    def enter_review_text(self,review_text):
        self.send_keys(self.WRITE_REVIEWS_2, review_text)
        self.logger.info(f'Enter a Review: {review_text}')

    def click_next_from_review_page(self):
        self.click(self.CLICK_NEXT_3)
        self.logger.info('Check review and click next')

    def click_to_confirm_review(self):
        self.click(self.CLICK_NEXT_4)
        self.logger.info('Confirm click to END the review')

    def click_to_close(self):
        self.click(self.CLICK_CLOSE_BUTTON)
        self.logger.info('Click Close and get confirmation e-mail')


    def is_review_successful(self):
        return self.is_visible(self.LOGO, timeout=5)





