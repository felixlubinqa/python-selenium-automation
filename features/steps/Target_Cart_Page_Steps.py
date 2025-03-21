from pydoc import pager

from selenium.webdriver.common.by import By
from behave import Then
from time import sleep


#@Given('')
#def xx(context):
#    context.driver.find_element(By."['')]")
#    sleep(0)
#
#
#@When('')
#def xx(context):
#    context.driver.find_element(By."['')]")
#    sleep(0)
#
#
@Then('Verify item added to cart')
def verify_cart_is_empty(context):
    context.driver.find_element(By.CSS_SELECTOR, ".sc-93ec7147-3")
    text_to_check = "1 item"
    content = context.driver.page_source
    assert text_to_check in content, f"Text '{text_to_check}' not found on the page"
    sleep(5)


@Then('Verify “Your cart is empty” message is shown')
def verify_cart_is_empty(context):
    context.driver.find_element(By.XPATH, "//h1[contains(@class, 'Heading')]")
    sleep(5)
