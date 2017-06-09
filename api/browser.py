# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   browser.py
# VERSION    :   1.0
# DESCRIPTION:   浏览器通用操作接口
#
# AUTHOR     :   LiuLu <lu.liu@phicomm.com>
# CREATE DATE:   04/06/2017
#
##############################################################
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = "http://p.to"

def openDriver():
	driver.get(url)
	driver.maximize_window()
	openConsole('/html/body')

def closeDriver():
	#time.sleep(15) 
	time.sleep(1)
	driver.quit()

def refresh():
	driver.refresh()

def openConsole(xpath):
	pass
	elem = driver.find_element_by_xpath(xpath)#缩小窗口
	elem.send_keys(Keys.COMMAND,Keys.ALT, 'i')
	#elem.send_keys(Keys.CONTROL,'-')
	#elem.send_keys(Keys.CONTROL,'-')

def main():
	openDriver()
