from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import Given, When, Then
# from time import sleep



@Given('Open Target Main Page')
def open_target(context):
    context.driver.get('https://www.target.com')
#    sleep(5)


@When('Click on cart icon')
def search_for_target(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/CartLink']").click()
#    sleep(10)


@When('Click on Add to cart icon')
def add_to_cart(context):
    context.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Add to cart')]").click()
 #   sleep(5)


@When('Click on Add to cart icon on side')
def add_to_cart_2nd_page(context):
    context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButtonOrTextIdFor9313']").click()
#    sleep(5)


@When('Click on Sign-In icon')
def sign_in_page(context):
    context.driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']").click()
#    sleep(5)


@When('Click on Second Sign-In icon')
def sign_in_2nd_page(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
#    sleep(5)

@When('Click on View Cart icon')
def view_cart_2nd_page(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href='/cart']").click()
#    sleep(5)

@Then('Verify “Sign into your Target account” message is shown')
def verify_sign_in_page(context):
    context.driver.find_element(By.XPATH, "//h1[contains(@class, 'Heading')]")
#    sleep(5)


@Then('Verify “Added to Cart” message is shown on side page')
def verify_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, ".sc-cd7ce3f4-0")
#    sleep(5)

#    context.driver.wait.until(EC.element_to_be_clickable((By.NAME, '')))


