from selenium.webdriver.common.by import By
from Pages.base_page import Page

class MainPage(Page):
    ADD_TO_CART = (By.XPATH, "//button[contains(@aria-label, 'Add to cart')]")


    def open_main_page(self):
        self.open_url('https://www.target.com/')

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART)

