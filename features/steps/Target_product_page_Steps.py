from selenium.webdriver.common.by import By
from behave import Given, Then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


COLOR_OPTIONS = (By.CSS_SELECTOR, "[aria-label*='Color']")
SELECTED_COLOR = (By.CSS_SELECTOR, 'div[class*="styles_headerWrapper"]')

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
    actual_colors = []
    expected_colors = ['Dark Green', 'Dark Green', 'Navy Blue', 'Red']
    colors = context.driver.find_elements(*COLOR_OPTIONS) #[green], [navy blue], [red]


    for color in colors:
        color.click()
        sleep(5)
        selected_color = context.driver.find_element(*SELECTED_COLOR).text

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)
    assert actual_colors == expected_colors, f'Actual Colors:{actual_colors} != Expected colors:{expected_colors}'



