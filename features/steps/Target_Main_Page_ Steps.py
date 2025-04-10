from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from behave import Given, When, Then
from time import sleep


@Given('Open Target Main Page')
def open_target(context):
    context.app.main_page.open_main_page()
#    context.driver.get('https://www.target.com')
#    sleep(5)


@When('Click on cart icon')
def search_for_target(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/CartLink']").click()
#    sleep(10)


@When('Click on Add to cart icon')
def add_to_cart(context):
   context.app.main_page.add_to_cart()
#   sleep(5)


@When('Click on Add to cart icon on side')
def add_to_cart_2nd_page(context):
    context.app.side_page.add_to_cart_side()
#    sleep(1)


@When('Click on Sign-In icon')
def sign_in_page(context):
    context.app.header.sign_in_button()
#    sleep(5)


@When('Click on Second Sign-In icon')
def sign_in_2nd_page(context):
    context.app.side_page.sign_in_side()
#    sleep(5)

@When('Click on View Cart icon')
def view_cart_2nd_page(context):
    context.app.side_page.view_cart_side_page()
#    sleep(2)

@Then('Verify “Sign in or create account” message is shown')
def verify_sign_in_page(context):
    context.app.header.verify_signin_page()
    sleep(2)


@Then('Verify “Added to Cart” message is shown on side page')
def verify_add_to_cart(context):
    context.app.side_page.item_added_side()
#    sleep(2)

#    context.driver.wait.until(EC.element_to_be_clickable((By.NAME, '')))


