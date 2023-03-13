from pages.samsung_page import SamsungPage
from time import sleep

def test_click_on_a_product(browser):
    samsung_page = SamsungPage(browser)
    samsung_page.load_page()
    samsung_page.click_on_a_product()
    sleep(10)