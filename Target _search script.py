from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
#driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

driver.find_element(By.ID, 'search').send_keys("tea")

driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

sleep(3)

#verification by finding 1 element
#driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']")

#verification by checking text
actual_text: str = driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
print('Actual text:\n', actual_text)

assert 'tea' in actual_text, f'Error, Text tea not found in Actual text: {actual_text}'

print("Test Case Passed")

# sleep(10)

#Note: make sure it fails!!!

# From Lesson 2:
#       File "C:\Users\felix\python-selenium-automation\Target _search script.py", line 32, in <module>
#           assert 'teajojjbhbib' in actual_text, f'Error, Text tea not found in Actual text: {actual_text}'
#                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#Assertions over if else statements