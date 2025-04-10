from selenium.webdriver.common.by import By
from Pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGN_IN_BTN = (By.XPATH, "//a[@aria-label='Account, sign in']")
    sign_in_header = (By.XPATH, "//h1[contains(@class, 'Heading')]")

    def search(self, search_word):
        self.input_text('tea', *self.SEARCH_FIELD).click()
        self.click(*self.SEARCH_BTN)

    def sign_in_button(self):
        self.click(*self.SIGN_IN_BTN)

    def verify_signin_page(self):
        actual_text = self.find_element(*self.sign_in_header).text
        assert 'Sign in or create account' in actual_text, f'Error, Sign-in Page not found'
