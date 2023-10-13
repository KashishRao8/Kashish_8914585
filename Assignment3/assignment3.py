# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = (webdriver.Chrome())

# Navigating to the Amazon.ca homepage
driver.get("https://www.dollarama.com/en-CA/")
time.sleep(3)

# Finding the search bar and entering text
search_bar = driver.find_element("xpath","/html/body/header/div[1]/nav/div/div/div/div/div[5]/div/form/div/div[1]/input")
search_bar.send_keys("calculator")
time.sleep(3)

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "calculator" in driver.title
time.sleep(3)

# Selecting a calculator from the search results
calculator_link = driver.find_element("xpath","/html/body/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/a")
calculator_link.click()

# Waiting for the calculator details page to load
time.sleep(5)

# Adding the calculator to the cart
add_to_cart_button = driver.find_element("xpath","/html/body/div[3]/div[1]/div[1]/div[2]/div/div[3]/div/div[2]/span/button")
add_to_cart_button.click()

# Waiting for the cart to update
time.sleep(5)

proceed_to_checkout= driver.find_element("xpath","/html/body/header/div[1]/nav/div/div/div/div/div[4]/ul/li[3]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div[3]/a")
proceed_to_checkout.click()
time.sleep(2)

# Closing the webdriver
driver.close()