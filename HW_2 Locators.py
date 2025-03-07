#1 Practice with locators


# Url = https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0

# Amazon logo ---------------------------------------------------
$x("//i[@class='a-icon a-icon-logo']")

# Email field ---------------------------------------------------
$x("//input[@id='ap_email']")

# Continue button -----------------------------------------------
$x("//input[@aria-describedby='legalTextRow']")

# Conditions of use link ----------------------------------------
$x("//a[contains(@href, 'condition')]")

# Privacy Notice link -------------------------------------------
$x("//a[contains(@href, 'notification_p')]")

# Need help link ------------------------------------------------
$x("//span[@class='a-expander-prompt']")

# Forgot your password link -------------------------------------
$x("//a[@id='auth-fpp-link-bottom']")

# Other issues with Sign-In link --------------------------------
$x("//a[@id='ap-other-signin-issues-link']")

# Create your Amazon account button -----------------------------
$x("//a[@id='createAccountSubmit']")

#2 Create a test case for the SignIn page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from re import findall

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
#driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

# click sign-in
driver.find_element(By.XPATH, "//span[@class='sc-58ad44c0-3 cOUViz h-margin-r-x3']").click()

sleep(2)

# click sign-in from side
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

#verification by text
#driver.find_element(By.XPATH, "//span['Sign into your Target account']")

print("Text Found")

#verification by element
driver.find_element(By.XPATH, "//button[contains(class, 'styles_nds']")

sleep(5)

#<h1 class="styles_ndsHeading__HcGpD styles_fontSize2__8Iex_ styles_x2Margin__M5gHh sc-315b8ab9-2 ldgAbd">
#   <span>Sign into your Target account</span></h1>