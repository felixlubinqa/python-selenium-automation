from selenium.webdriver.common.by import By
from behave import Given, Then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from features.steps.product_search_file import click_search_icon


@Given('Open Target Product A-82711059 Page')
def open_product_page(context):
    context.driver.get('https://www.target.com/p/levi-s-women-s-high-rise-wedgie-straight-cropped-jeans/-/A-82711059')


@Given('Open Target Product A-93370753 Page')
def open_product_page(context):
    context.driver.get('https://www.target.com/p/women-s-high-rise-seamless-skort-all-in-motion/-/A-93370753')


#@When('')
#
#


@Then('Verify color selection is shown on A-82711059 page')
def click_and_verify_colors(context):
    color_options = "[aria-label*='Color']"
    #context.driver.find_element(By.CSS_SELECTOR, color_options).click()
    color_count = len(context.driver.find_elements(By.CSS_SELECTOR, color_options))
    print(color_count)

    for i in range(color_count):
        context.driver.find_element(By.CSS_SELECTOR, color_options).click()
        sleep(2)

@Then('Verify color selection is shown on A-93370753 page')
def click_and_verify_colors(context):
    color_options2 = "[aria-label*='Color']"
    context.driver.find_element(By.CSS_SELECTOR, color_options2).click()
    color_count2 = len(context.driver.find_elements(By.CSS_SELECTOR, color_options2))
    print(color_count2)

    for i in range(color_count2):
        context.driver.find_element(By.CSS_SELECTOR, color_options2).click()
        sleep(2)
