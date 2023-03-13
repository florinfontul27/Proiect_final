from selenium.webdriver.common.by import By


class PhonesPage:
    RESIGILATE = (By.CSS_SELECTOR, '#catalog-filters-container > ul > li:nth-child(1) > ul > li:nth-child(1) > a > span.checkbox-control.inline-block.align-top.w-5.h-5.p-1.mr-2.border-gray-light.border.rounded-4px.bg-white')
    URL = ('https://altex.ro/telefoane/cpl/')


    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_on_reaseld_button(self):
        self.browser.find_element(*self.RESIGILATE).click()
