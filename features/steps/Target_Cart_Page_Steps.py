from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import Given, When, Then
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
def verify_cart_function(context):
    context.driver.find_element(By.CSS_SELECTOR, ".sc-93ec7147-3")
    text_to_check = "1 item"
    content = context.driver.page_source
    assert text_to_check in content, f"Text '{text_to_check}' not found on the page"
#    sleep(5)


@Then('Verify “Your cart is empty” message is shown')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()
#    context.driver.find_element(By.XPATH, "//h1[contains(@class, 'Heading')]")
    sleep(3)

#    context.driver.wait.until(EC.element_to_be_clickable((By.NAME, '')))
