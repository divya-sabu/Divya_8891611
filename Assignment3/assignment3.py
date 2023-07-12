# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.ubereats.com/ca")
time.sleep(3)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
search_bar = driver.find_element("id","location-typeahead-home-input")
search_bar.send_keys("107 Ellis Cresent South")
time.sleep(5)

find_food = driver.find_element("xpath","//button[contains(.,'Find Food')]")
find_food.click()
time.sleep(5)
driver.maximize_window()
time.sleep(3)

search_food = driver.find_element("id","search-suggestions-typeahead-input")
search_food.send_keys("pasta")
search_food.send_keys(Keys.RETURN)
time.sleep(5)

sort_food = driver.find_element("xpath","//span[contains(.,'  Most popular')]")
sort_food.click()
time.sleep(3)

select_Rest = driver.find_element("xpath","//img[contains(@src,'https://d1ralsognjng37.cloudfront.net/d7f84e37-798e-4928-963d-5ae4c953f94f.jpeg')]")
select_Rest.click()
time.sleep(3)

select_pasta = driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/main/div[5]/div/div[4]/ul/li[1]/ul/li[1]/div/div/div[2]/div[1]/span")
select_pasta.click()
time.sleep(3)

select_cart = driver.find_element("xpath","//button[contains(@aria-label,'Add 1 to order')]")
select_cart.click()
time.sleep(3)


# Closing the webdriver
driver.close()


