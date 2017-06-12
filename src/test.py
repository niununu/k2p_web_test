from selenium import adapterdriver
from selenium.common.exceptions import NoSuchElementException


import os
import time
#driver = adapterdriver.Chrome()
#print(driver.find_element_by_xpath('dja').is_displayed())


from selenium.adapterdriver.common.keys import Keys

driver = adapterdriver.Chrome()
url = "http://p.to"


driver.get(url)
driver.maximize_window()
#penConsole('/html/body')


time.sleep(2)
print("111111")

elem = driver.find_element_by_xpath('//*[@id="Main"]/div[1]')
elem.send_keys(Keys.COMMAND,Keys.ALT, 'i')



