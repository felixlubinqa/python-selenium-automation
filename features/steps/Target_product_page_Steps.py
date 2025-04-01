from selenium.webdriver.common.by import By
from behave import Given, Then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


COLOR_OPTIONS = (By.CSS_SELECTOR, "[aria-label*='Color']")
SELECTED_COLOR1 = (By.CSS_SELECTOR, 'div[class*="styles_headerWrapper"]')
SELECTED_COLOR2 = (By.CSS_SELECTOR, 'div[class*="styles_headerWrapper"]')


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
    actual_colors = []
    expected_colors = ['Cut & Dry', 'Max Effort', 'Soft Black', 'Struck By Lightning', 'Don\'t Fray Me - Out of Stock', 'Indigo Here We go - Out of Stock']
    colors = context.driver.find_elements(By.CSS_SELECTOR, "[height='64px']")

    for color in colors:
        color.click()
        sleep(1)
        selected_color = context.driver.find_element(*SELECTED_COLOR1).text

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert actual_colors == expected_colors, f'Actual Colors:{actual_colors} != Expected colors:{expected_colors}'


@Then('Verify color selection is shown on A-93370753 page')
def click_and_verify_colors(context):
    actual_colors = []
    expected_colors = ['Dark Green', 'Dark Green', 'Navy Blue', 'Red']
    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors:
        color.click()
        sleep(5)
        selected_color = context.driver.find_element(*SELECTED_COLOR2).text

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)
    assert actual_colors == expected_colors, f'Actual Colors:{actual_colors} != Expected colors:{expected_colors}'



