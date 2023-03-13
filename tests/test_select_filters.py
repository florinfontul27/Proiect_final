from pages.phones_page import PhonesPage
from time import sleep

def test_select_filters(browser):
    phones_page = PhonesPage(browser)
    phones_page.load_page()
    phones_page.click_on_reaseld_button()
    sleep(10)
