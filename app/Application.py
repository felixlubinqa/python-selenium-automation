from Pages.base_page import Page
from Pages.cart_page import CartPage
from Pages.header import Header
from Pages.main_page import MainPage
from Pages.search_results import SearchResults
from Pages.side_page import SidePage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results = SearchResults(driver)
        self.cart_page = CartPage(driver)
        self.side_page = SidePage(driver)
