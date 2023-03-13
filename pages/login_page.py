from selenium.webdriver.common.by import By
class LoginPage:
    MY_ACCOUNT_BUTTON = (By.CSS_SELECTOR, '[class="jsx-9d04a24ff8b4af87 hidden sm:block"]')
    EMAIL_FIELD = (By.CSS_SELECTOR, '[name="email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[name="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[class="button-wrapper leading-20.8 p-12px block w-full inline-block -tracking-0.18"]')
    ERROR_MESSAGE_TEXT = (By.CSS_SELECTOR, 'div.pb-2  div.text-red-brand')


    URL = ('https://altex.ro/cont/intra/')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_my_account_button(self):
        self.browser.find_element(*self.MY_ACCOUNT_BUTTON).click()

    def type_email(self,email):
        self.browser.find_element(*self.EMAIL_FIELD).send_keys(email)

    def type_password(self,password):
        self.browser.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.browser.find_element(*self.ERROR_MESSAGE_TEXT).text
