from selenium.webdriver.common.by import By
from Pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")


    def search(self, search_word):
        self.input_text('tea', *self.SEARCH_FIELD).click()
        self.click(*self.SEARCH_BTN)
