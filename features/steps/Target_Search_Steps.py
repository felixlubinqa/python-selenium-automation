from selenium.webdriver.common.by import By
from behave import Given, When, Then
from time import sleep
from features.steps.product_search import click_search_icon


@Given('Open Target Main Page')
def open_target(context):
    context.driver.get('https://www.target.com')
    sleep(5)


@When('Click on cart icon')
def search_for_target(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/CartLink']").click()
    sleep(10)

@Then('Verify “Your cart is empty” message is shown')
def verify_cart_is_empty(context):
    context.driver.find_element(By.XPATH, "//h1[contains(@class, 'Heading')]")
    sleep(5)

