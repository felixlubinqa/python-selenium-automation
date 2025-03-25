from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from behave import Given, When, Then
from time import sleep

@Given('Open Target Product A-54551690 Page')
def open_product_page(context):
    context.driver.get('https://www.target.com/p/A-54551690')


@Given('Open Target Product A-93370753 Page')
def open_product_page(context):
    context.driver.get('https://www.target.com/p/women-s-high-rise-seamless-skort-all-in-motion/-/A-93370753')


#@When('')
#
#


@Then('Verify color selection is shown on A-54551690 page')
def verify_color_selection(context):
    color_options = "[class='styles_hasWidth__r08uu styles_hasHeight__0XmVc']"
    colors = context.driver.find_elements(By.CSS_SELECTOR, color_options)
    print(colors)

    for color in colors:
        color.click()
        sleep(1)


@Then('Verify color selection is shown on A-91511634 page')
def verify_color_selection(context):
    color_options2 = "[class='styles_hasWidth__r08uu styles_hasHeight__0XmVc']"
    colors = context.driver.find_elements(By.CSS_SELECTOR, color_options2)
    print(colors)

    for color in colors:
        color.click()
        sleep(1)
