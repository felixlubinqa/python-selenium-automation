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
    context.app.cart_page.verify_cart_function()
#    sleep(5)

# HW-6 Updated
@Then('Verify “Your cart is empty” message is shown')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()
    sleep(3)

#    context.driver.wait.until(EC.element_to_be_clickable((By.NAME, '')))
