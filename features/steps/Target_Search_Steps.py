from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from behave import when, then


SEARCH_INPUT = (By.ID, 'search')
SEARCH_SUBMIT = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
#SEARCH_RESULTS = (By.XPATH, "//div[@data-test='lp-fulfillmentFilterBar']")



@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys("tea")
    sleep(2)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


@then('Verify correct search results shown for {expected_text}')
def verify_search_results(context, expected_text):
    context.app.search_results.verify_search()
    sleep(1)