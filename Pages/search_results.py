from selenium.webdriver.common.by import By
from Pages.base_page import Page



class SearchResults(Page):
    search_results_text = (By.XPATH, "//span[contains(text(),'tea')]")

    def verify_search(self):
        actual_text = self.find_element(*self.search_results_text).text
        assert 'tea' in actual_text, f'Error, Text tea not found in Actual text: {actual_text}'
