#1 Practice with locators
from http.cookiejar import HEADER_TOKEN_RE


# Url = https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dap_frn_logo%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0

# Your name ---------------------------------------------------
$$("#ap_customer_name")

# Number / Email ---------------------------------------------------
$$("#ap_email")
$$("input.a-input-text[name='email']")

# Password Field-----------------------------------------------
$$("input.auth-require-password-validation")


# Password Characters----------------------------------------
$$("#auth-password-requirement-info")

# Re-Enter Password-------------------------------------------
$$("input.auth-require-fields-match[name=passwordCheck]")

# Continue Button ------------------------------------------------
$$("#continue")

# Conditions of Use-------------------------------------
$$("a[href$='=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")

# Privacy Notice--------------------------------
$$("a[href*='ap_register_notification_privacy_notice']")

# Already have an account-----------------------------
$$("a.a-link-emphasis")


#2 Create a test case for empty Cart

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


#3 Create a test case for the SignIn page

from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep


# @given('Open Target Main Page')
# def open_target(context):
#     context.driver.get('https://www.target.com')
#     sleep(5)


@when('Click on Sign-In icon')
def sign_in_page(context):
    context.driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']").click()
    sleep(5)


@when('Click on Second Sign-In icon')
def sign_in_2nd_page(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
    sleep(5)


@then('Verify “Sign into your Target account” message is shown')
def verify_sign_in_page(context):
    context.driver.find_element(By.XPATH, "//h1[contains(@class, 'Heading')]")
    sleep(5)
