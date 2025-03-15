from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target Main Page')
def open_target(context):
    context.driver.get('https://www.target.com')
    sleep(5)


@when('Click on Sign-In icon')
def sign_in_page(context):
    context.driver.find_element(By.XPATH, "//use[@href='/icons/Account.svg#Account']").click()
    sleep(5)


@when('Click on Second Sign-In icon')
def sign_in_2nd_page(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
    sleep(5)


@then('Verify “Sign into your Target account” message is shown')
def verify_sign_in_page(context):
    context.driver.find_element(By.XPATH, "//h1[contains(@class, 'Heading')]")
    sleep(5)

