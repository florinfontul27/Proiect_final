from pages.product_page import ProductPage
from time import sleep


def test_add_to_cart(browser):
    product_page = ProductPage(browser)
    product_page.load_page()
    product_page.add_to_cart()
    sleep(10)

def test_reserve_in_store(browser):
    product_page = ProductPage(browser)
    product_page.load_page()
    product_page.reserve_in_store()
    sleep(10)