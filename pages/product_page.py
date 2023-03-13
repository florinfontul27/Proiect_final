from selenium.webdriver.common.by import By

class ProductPage:

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#__next > div.content-wrapper.relative.grow.flex.flex-col.justify-between > div.container > main > div.jsx-8f410c0b503f5d3f.relative > div.jsx-8f410c0b503f5d3f.flex.items-start.flex-col.space-y-2.md\:space-y-0.md\:flex-row.md\:space-x-8.justify-center.lg\:-mx-3.my-3.mb-14 > div.jsx-8f410c0b503f5d3f.w-full.md\:w-\[434px\].lg\:min-w-\[530px\] > div > div.jsx-8f410c0b503f5d3f.mt-2.mb-\[30px\] > div.jsx-8f410c0b503f5d3f.flex.flex-col.items-center.space-y-2.\!mt-5.md\:mt-0.lg\:flex-row.lg\:space-y-0.lg\:space-x-4 > div:nth-child(1) > div > button > span')
    RESERVE_IN_STORE_BUTTON = (By.CSS_SELECTOR, '#__next > div.content-wrapper.relative.grow.flex.flex-col.justify-between > div.container > main > div.jsx-8f410c0b503f5d3f.relative > div.jsx-8f410c0b503f5d3f.flex.items-start.flex-col.space-y-2.md\:space-y-0.md\:flex-row.md\:space-x-8.justify-center.lg\:-mx-3.my-3.mb-14 > div.jsx-8f410c0b503f5d3f.w-full.md\:w-\[434px\].lg\:min-w-\[530px\] > div > div.jsx-8f410c0b503f5d3f.mt-2.mb-\[30px\] > div.jsx-8f410c0b503f5d3f.flex.flex-col.items-center.space-y-2.\!mt-5.md\:mt-0.lg\:flex-row.lg\:space-y-0.lg\:space-x-4 > div:nth-child(2) > button > span')
    STORAGE_CAPACITY = (By.CSS_SELECTOR, '')
    URL = ('https://altex.ro/telefon-samsung-z-flip4-5g-512gb-8gb-ram-dual-sim-blue/cpd/SMTZFLIP45BL/')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def add_to_cart(self):
        self.browser.find_element(*self.ADD_TO_CART_BUTTON).click()

    def reserve_in_store(self):
        self.browser.find_element(*self.RESERVE_IN_STORE_BUTTON).click()
