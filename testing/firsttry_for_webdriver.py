from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
browser = webdriver.Firefox()
browser.get('https://www.google.com/search?client=firefox-b-d&q=%22leodahal%22')

data = browser.find_element_by_css_selector("div#result-stats")
print(data.text)
browser.quit()
