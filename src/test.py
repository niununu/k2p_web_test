from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


import os
import time
#driver = webdriver.Chrome()
#print(driver.find_element_by_xpath('dja').is_displayed())


from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = "http://p.to"


driver.get(url)
driver.maximize_window()
#penConsole('/html/body')


time.sleep(2)
print("111111")

elem = driver.find_element_by_xpath('//*[@id="Main"]/div[1]')
elem.send_keys(Keys.COMMAND,Keys.ALT, 'i')



