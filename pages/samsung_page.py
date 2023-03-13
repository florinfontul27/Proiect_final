from selenium.webdriver.common.by import By

class SamsungPage:

    PRODUCT = (By.CSS_SELECTOR, '[alt="Telefon SAMSUNG Z Flip4 5G, 512GB, 8GB RAM, Dual SIM, Blue"]')
    URL = ('https://altex.ro/cauta/?q=samsung')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_on_a_product(self):
        self.browser.find_element(*self.PRODUCT).click()


