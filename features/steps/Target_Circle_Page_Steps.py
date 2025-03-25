from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import Given, When, Then
# from time import sleep


# SEARCH_BTN = (By.XPATH, "//*[@data-test='@web/CartLink']")
SEARCH_VERIFY = (By.XPATH, "//div[@class='filmstrip-with-storyblocks-ie-11-fix']")


@Given('Open Target Circle Page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')
#    sleep(5)

#@When()
#def xx_xx_xx)(context):
#   context.driver.get('https://www.target.com/circle')
#   sleep(5)


@Then('Verify there are 10 benefit cells minimum')
def verify_benefit_cells(context):
    Benefits = context.driver.find_elements(*SEARCH_VERIFY)
    assert len(SEARCH_VERIFY) <= 10, f'Expected 10 benefit cells, found {len(SEARCH_VERIFY)}'
    print(Benefits)

#    context.driver.wait.until(EC.element_to_be_clickable((By.NAME, '')))