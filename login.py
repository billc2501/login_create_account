from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

Str = input("Word: ")


browser = webdriver.Chrome('/Users/billy/Desktop/login_create_account/chromedriver')
browser.get(('https://www.dictionary.com/browse/that'))
item = browser.find_element_by_name("override_query")
item.send_keys(Str)
button = browser.find_element_by_id("search-submit")
button.click()
