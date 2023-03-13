from pages.login_page import LoginPage
from time import sleep


def test_login_functionality(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.click_my_account_button()
    login_page.type_email('floryn_11_98@yahoo.com')
    login_page.type_password('ceamaitareparola')


def test_login_with_invalid_credentials(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.click_my_account_button()
    login_page.click_login_button()
    assert 'Acest camp este obligatoriu' in login_page.get_error_message()
    sleep(10)



