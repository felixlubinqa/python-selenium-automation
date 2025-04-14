from time import sleep

from selenium.webdriver.common.by import By
from Pages.base_page import Page

class MainPage(Page):
    ADD_TO_CART = (By.CSS_SELECTOR, '[id*="addToCartButtonOrTextId"]')


    def open_main_page(self):
        self.open_url('https://www.target.com/')

    def add_to_cart(self):
        sleep(10)
        self.click(*self.ADD_TO_CART)
        sleep(5)
