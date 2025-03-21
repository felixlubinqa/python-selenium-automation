from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# By ID
driver.find_element(By.ID,'twotabsearchtextbox')
driver.find_element(By.ID,'nav-search-submit-button')

# Xpath
#XPath=”//tagname[@attribute='value']'

Xpath = '//input[@aria-label='Search Amazon']'

driver.find_element(By.XPATH,"//div[contains(text(), "Black N")]")

# partial
# driver.find_element(By.XPATH,

# Class Example -----------------------------------------------------
driver.find_element(By.ID, "//select[@id='searchDropdownBox']")
driver.find_element(By.XPATH,"//select[@style='display: block; top: 2.5px;']")
driver.find_element(By.XPATH, "//select[contains(text(), 'searchD')]")

# Script Example -----------------------------------------------------





