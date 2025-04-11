from selenium.webdriver.common.by import By
from Pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    OBJECT_IN_CART = (By.XPATH, "//div[@aria-label='cart item ready to fulfill']")

    # HW-6 Updated
    def verify_cart_empty(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def verify_cart_function(self):
        self.find_element(*self.OBJECT_IN_CART)

        # actual_result = self.find_element(*self.CART_EMPTY_MSG).text
        # assert expected_result == actual_result, f'Expected "{expected_result}" but got "{actual_result}"'

