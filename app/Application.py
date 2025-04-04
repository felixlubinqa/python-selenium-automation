from Pages.base_page import Page
from Pages.header import Header
from Pages.main_page import MainPage
from Pages.search_results import SearchResults


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results = SearchResults(driver)
