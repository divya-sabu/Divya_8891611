from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#
driver = webdriver.Chrome()

driver.get("https://www.amazon.ca/")
time.sleep(6)
driver.maximize_window()
time.sleep(2)
search_bar = driver.find_element("id", "twotabsearchtextbox")
time.sleep(5)
search_bar.send_keys("beauty")
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

product_Link = driver.find_element("id", "nav-orders")
time.sleep(5)
product_Link.click()
time.sleep(4)

create_account = driver.find_element("id", "createAccountSubmit")
time.sleep(4)
create_account.click()
time.sleep(3)

business_account = driver.find_element("id", "ab-registration-link")
business_account.click()
time.sleep(4)

sign_in = driver.find_element("id", "sign-in")
sign_in.click()
time.sleep(8)
# # Closing the webdriver
driver.close()

