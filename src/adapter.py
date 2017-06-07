# -*- coding: UTF-8 -*-
#!/usr/bin/env python
from selenium import webdriver
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
networkRestartTime = 40
rebootTime = 70
localtime = time.asctime( time.localtime(time.time()))
logDir = '../testLog/testLog.txt'

def openDriver():
	driver.get("http://p.to")
	driver.maximize_window()

def waitandClick(xpath):
	try:
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
	except TimeoutException as e:
		print('Error:waitandClick, TimeoutException, xpath = %s\n' % xpath)
		wirteWebErrToLog('waitandClick', 'TimeoutException', xpath)
		return False

	driver.find_element_by_xpath(xpath).click()

def waitandSendkeys(xpath, keys):
	try:
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
	except TimeoutException as e:
		print('Error:waitandSendkeys, TimeoutException, xpath = %s\n' % xpath)
		wirteWebErrToLog('waitandSendkeys', 'TimeoutException', xpath)
		return False

	driver.find_element_by_xpath(xpath).clear()
	driver.find_element_by_xpath(xpath).send_keys(keys)

def clickApp():
	time.sleep(1)
	waitforDisplay('//*[@id="Con"]/div[1]/ul[1]/a[4]/li')
	waitandClick('//*[@id="Con"]/div[1]/ul[1]/a[4]/li')
	waitforDisplay('//*[@id="Content"]')

def executeJS(js):
	driver.execute_script(js)

def srcollAction(site):
	scrollTop = '0'
	if site == 'top':
		scrollTop = '0'
	elif site == 'bottom':
		scrollTop = '10000'
	#adapter.executeJS("var q = document.getElementById('Content').scrollTop=10000")
	driver.execute_script("var q = document.getElementById('Content').scrollTop=%s" % scrollTop)

def alwaysOpenSwitch(xpath, switchValue='data-value'):
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
	button = driver.find_element_by_xpath(xpath)
	if button.get_attribute(switchValue) == '0':
		button.click()

def alwaysCloseSwitch(xpath, switchValue='data-value'):
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
	button = driver.find_element_by_xpath(xpath)
	if button.get_attribute(switchValue) == '1':
		button.click()

def closeDriver():
	#time.sleep(15) 
	time.sleep(1)
	driver.quit()

def refresh():
	driver.refresh()

def waitforDisappear(xpath):
	waitforDisplay(xpath)
	try:
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
	except TimeoutException as e:
		print('Error:waitforDisappear, TimeoutException, xpath = %s\n' % xpath)
		wirteWebErrToLog('waitforDisappear', 'TimeoutException', xpath)
		return False

	try:
		process = driver.find_element_by_xpath(xpath)
		WebDriverWait(driver, 20).until_not(lambda driver: process.is_displayed())
	except NoSuchElementException as e:
		print('Error:waitforDisappear, NoSuchElementException, xpath = %s\n' % xpath)
		wirteWebErrToLog('waitforDisappear', 'NoSuchElementException', xpath)
		return False

def waitforDisplay(xpath):
	try:
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
	except TimeoutException as e:
		print('Error:waitforDisplay, TimeoutException, xpath = %s\n' % xpath)
		wirteWebErrToLog('waitforDisplay', 'TimeoutException', xpath)
		return False

	try:
		process = driver.find_element_by_xpath(xpath)
		WebDriverWait(driver, 10).until(lambda driver: process.is_displayed())
	except NoSuchElementException as e:
		print('Error:waitforDisplay, NoSuchElementException, xpath = %s\n' % xpath)
		wirteWebErrToLog('waitforDisplay', 'NoSuchElementException', xpath)
		return False

def wirteLog(data, moduleName, mode, errName="", xpath=""):
	fileObject = open(logDir, 'a')
	if mode == 1:#moduleBegin
		fileObject.write('\n%s, %s begin\n'%(localtime, moduleName))
		fileObject.write("Set Data :\n")
		for key in data:
			fileObject.write('		%s = %s\n' % (key, data[key]))
	else:#modulEnd
		fileObject.write('%s, %s end\n\n'%(localtime, moduleName))

def wirteWebErrToLog(funcName, errName="", xpath=""):
	fileObject = open(logDir, 'a')
	fileObject.write('WebError:\nfunName:%s, error:%s, xpath:%s, \ntime:%s\n' % (funcName, errName, xpath, localtime))
	fileObject.close()
	try:
		closeDriver()
		os._exit(0)
	except :
		print('catch error, exit!!')

def wirteDataErrToLog(funcName, data, value, line, tips=""):
	fileObject = open(logDir, 'a')
	fileObject.wirte('DataError:\nfunName:%s, data:%s, value:%s, line:%s\ntips:%s'\
		%(funcName, data, value, line, tips))
	fileObject.close()
	try:
		closeDriver()
		os._exit(0)
	except :
		print('catch error, exit!!')

def elementIsDisplayed(xpath):
	try:
		driver.find_element_by_xpath(xpath)
	except NoSuchElementException as e:
		return False
	return True

def getElementInTable(tableXpath, baseXpath, arrData,):
	table = driver.find_element_by_xpath('//*[@id="PortfwdTab"]')
	#table的总行数，包含标题
	table_rows = len(table.find_elements_by_tag_name('tr'))
	#tabler的总列数
	table_cols = len(arrData) - 1
	flag = False
	for row in range(2,table_rows + 1):
		for col in xrange(1,table_cols + 1):
			xpath = '%s/tr[%d]/td[%d]' %(baseXpath, row, col)
			if arrData[col] == driver.find_element_by_xpath(xpath).text:
				if col == table_cols:
					flag = True
			else:
				break
		if flag == True:
			return row
	return 0





