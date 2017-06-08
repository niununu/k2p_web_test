# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   web.py
# VERSION    :   1.0
# DESCRIPTION:   web页面通用操作接口
#
# CREATE DATE:   
#
##############################################################
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
import os
import log as log

import browser as browser
networkRestartTime = 40
rebootTime = 70
driver = browser.driver

#点击页面元素
def waitandClick(xpath):
	try:
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
	except TimeoutException as e:
		print('Error:waitandClick, TimeoutException, xpath = %s\n' % xpath)
		log.wirteWebErrToLog('waitandClick', 'TimeoutException', xpath)
		return False

	driver.find_element_by_xpath(xpath).click()

#输入框输入值
def waitandSendkeys(xpath, keys):
	try:
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
	except TimeoutException as e:
		print('Error:waitandSendkeys, TimeoutException, xpath = %s\n' % xpath)
		log.wirteWebErrToLog('waitandSendkeys', 'TimeoutException', xpath)
		return False

	driver.find_element_by_xpath(xpath).clear()
	driver.find_element_by_xpath(xpath).send_keys(keys)

#点击功能设置
def clickApp():
	time.sleep(1)
	waitforDisplay('//*[@id="Con"]/div[1]/ul[1]/a[4]/li')
	waitandClick('//*[@id="Con"]/div[1]/ul[1]/a[4]/li')
	waitforDisplay('//*[@id="Content"]')

def executeJS(js):
	driver.execute_script(js)

#操作滚动条
def srcollAction(site):
	scrollTop = '0'
	if site == 'top':
		scrollTop = '0'
	elif site == 'bottom':
		scrollTop = '10000'
	#web.executeJS("var q = document.getElementById('Content').scrollTop=10000")
	driver.execute_script("var q = document.getElementById('Content').scrollTop=%s" % scrollTop)

#开启开关
def alwaysOpenSwitch(xpath, switchValue='data-value'):
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
	button = driver.find_element_by_xpath(xpath)
	if button.get_attribute(switchValue) == '0':
		button.click()

#关闭开关
def alwaysCloseSwitch(xpath, switchValue='data-value'):
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
	button = driver.find_element_by_xpath(xpath)
	if button.get_attribute(switchValue) == '1':
		button.click()

#等待页面消失
def waitforDisappear(xpath):
	#waitforDisplay(xpath)
	try:
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
	except TimeoutException as e:
		print('Error:waitforDisappear, TimeoutException, xpath = %s\n' % xpath)
		log.wirteWebErrToLog('waitforDisappear', 'TimeoutException', xpath)
		return False

	try:
		process = driver.find_element_by_xpath(xpath)
		WebDriverWait(driver, 20).until_not(lambda driver: process.is_displayed())
	except NoSuchElementException as e:
		print('Error:waitforDisappear, NoSuchElementException, xpath = %s\n' % xpath)
		log.wirteWebErrToLog('waitforDisappear', 'NoSuchElementException', xpath)
		return False

#等待页面出现
def waitforDisplay(xpath):
	try:
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
	except TimeoutException as e:
		print('Error:waitforDisplay, TimeoutException, xpath = %s\n' % xpath)
		log.wirteWebErrToLog('waitforDisplay', 'TimeoutException', xpath)
		return False

	try:
		process = driver.find_element_by_xpath(xpath)
		WebDriverWait(driver, 10).until(lambda driver: process.is_displayed())
	except NoSuchElementException as e:
		print('Error:waitforDisplay, NoSuchElementException, xpath = %s\n' % xpath)
		log.wirteWebErrToLog('waitforDisplay', 'NoSuchElementException', xpath)
		return False

#检查某个元素时候出现
def elementIsDisplayed(xpath):
	try:
		driver.find_element_by_xpath(xpath)
	except NoSuchElementException as e:
		return False
	return True

#在表格中查找输入数据
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