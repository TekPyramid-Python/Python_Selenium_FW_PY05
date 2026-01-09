# tests/test_login.py
import allure
import pytest

from config.environment import Environment
from pages.vanalaya_review_page import ReviewPage
from tests.base_test import BaseTest


# @allure.feature("Authentication")
# @allure.story("User Login")
class TestReviewPage(BaseTest):
    """
    Test class for login functionality against saucedemo.com.
    """

    @allure.title("Test successful login with valid credentials")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_review_successful(self):
        """
        Test Case: Verify successful login using credentials from config.yaml.
        """
        # --- Initialize pages and variables ---
        review_page = ReviewPage(self.driver)
        env = Environment("test")  # Uses ENV=demo by default if not set
        base_url = env.get_base_url()
        username = env.get_username()


        with allure.step("Navigate to Blog page"):
            review_page.navigate_to(base_url)
            # The is_visible method is inherited from BasePagea
            assert review_page.is_visible(review_page.LOGO), "Page did not load properly"

        # with allure.step("Perform blog with valid credentials"):
        #     review_page.review_page('jkl','abcd@gmail.com',r'C:\Users\shoba\OneDrive\Desktop\Python_Selenium_FW_PY05\test_data\dummy_images.png')

        with allure.step("Click Dropdown"):
            review_page.click_drop_down()
            assert review_page.is_visible(review_page.CLICK_DROP_DOWN), "Drop Down is not visible"

        with allure.step("Select a Product from Dropdown"):
            review_page.select_product()
            assert review_page.is_visible(review_page.CLICK_PRODUCT_IMAGE), "Select Product is not visible"

        with allure.step("Click a Product Image"):
            review_page.click_product_image()
            assert review_page.is_visible(review_page.CLICK_PRODUCT_IMAGE),"Can't click the Product Image"

        with allure.step("Scroll to write a review and click"):
            review_page.scroll_towards_element()
            assert review_page.is_visible(review_page.SCROLL_2_REVIEW),"Not Scrolling towards the element"

        with allure.step("Click to write review"):
            review_page.click_to_write_review()
            assert review_page.is_visible(review_page.CLICK_WRITE_REVIEW),"Not able to click to write a Review"

        with allure.step("Click and Give Rating as 3"):
            review_page.click_for_rating()
            assert review_page.is_visible(review_page.RATING_3_STAR_1),"Cant give rating as 3"

        with allure.step("Writing a Review"):
            review_page.write_review("Nice Product")
            assert review_page.is_visible(review_page.WRITE_REVIEWS_1),"Can't Enter any reviews about the product"

        with allure.step("Click the first next button after review"):
            review_page.click_next_btn_from_review_page()
            # assert review_page.is_visible(review_page.ENTER_EMAIL),"First next button after writing review is not clicking"

        with allure.step("Enter Email ID"):
            review_page.wait_and_enter_email_id("abcd@gmail.com")
            assert review_page.is_visible(review_page.ENTER_EMAIL),"Can't enter any input in Email ID"

        with allure.step("Click Next Button after Entering Email:id"):
            review_page.click_next_btn_from_email_id()
            assert review_page.is_visible(review_page.SHARE_PICTURE),"Image upload page is not open"

        with allure.step("Uploading a Dummy Image"):
            review_page.upload_dummy_image(r"C:\Users\shoba\OneDrive\Desktop\Python_Selenium_FW_PY05\test_data\dummy_images.png")
            assert review_page.is_visible(review_page.SHARE_PICTURE)

        with allure.step("Clicking Next button after Uploading Dummy Image"):
            review_page.wait_and_click_next_btn_from_dummy_image()
            assert review_page.is_visible(review_page.THANKYOU_TEXT),"Can't Click Next button after uploading"

        with allure.step("Wait until DOM loads and Click give rating"):
            review_page.wait_and_give_rating()
            assert review_page.is_visible(review_page.CLICK_NEXT_3),"Can't give ratings after uploading the Dummy Image"

        with allure.step("Writing reviews again for the product"):
            review_page.enter_review_text("Other than Delivery delay, Product is good")
            assert review_page.is_visible(review_page.CLICK_NEXT_3),"Entering review after upload of Image"

        with allure.step("Check and Click Next Button"):
            review_page.click_next_from_review_page()
            assert review_page.is_visible(review_page.CLICK_NEXT_4),"Can't click next button after entering the reviews"

        with allure.step("After clicking Next Button Your review is confirmed"):
            review_page.click_to_confirm_review()
            assert review_page.is_visible(review_page.CLICK_NEXT_4),"Can't confirm the review and End Next Button is not Clckable"

        with allure.step("Click close button to get confirm e-mail"):
            review_page.click_to_close()
            assert review_page.is_visible(review_page.THANKYOU_TEXT),'Not clicked and no confirmation email received'
