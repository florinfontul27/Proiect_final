from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


class HomePage:

    SEARCH_INPUT = (By.CSS_SELECTOR, '[type="text"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[width="17"]')
    ERROR_MESSAGE_TEXT = (By.CSS_SELECTOR, 'p.text-xl')

    URL = ('https://altex.ro/')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)


    def type_search_input(self, product):
        self.browser.find_element(*self.SEARCH_INPUT).send_keys(product)

    def make_a_search(self):
        self.browser.find_element(*self.SEARCH_BUTTON).click()

    def get_error_message(self):
        return self.browser.find_element(*self.ERROR_MESSAGE_TEXT).text















