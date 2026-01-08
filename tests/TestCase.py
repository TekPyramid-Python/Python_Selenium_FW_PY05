from pages.login_page import LoginPage
class TestLogin:
    def test_create_account(browser_setup):
        login = LoginPage(browser_setup)

        login.click_profile()
        login.enter_firstname("xyz")
        login.enter_lastname("parvatham")
        login.enter_email("test123@gmail.com")
        login.enter_phone("9876543210")
        login.enter_password("Test@123")
        login.click_create_account()
        login.click_login_using_email()
        login.scroll_down()
        login.click_contactus()
        login.enter_search_text()
        login.search_bt()
        login.sel_prod()
        login.add_()
        login.checkout()