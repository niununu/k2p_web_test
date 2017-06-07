# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   luci.sh
# VERSION    :   1.0
# DESCRIPTION:   K2P旧UI升级到新UI时，etc/config/luci文件配置适配
#
# CREATE DATE:   04/06/2017
#
##############################################################
import sys 
sys.path.append('../api')
from api import *
import web
import sys
import time

class portForwardClass(object):
	"""docstring for portForwardClass"""
	def __init__(self, arg):
		#super(portForwardClass, self).__init__()
		self.enable = arg['enable']
		self.ruleName = arg['ruleName']
		self.serverIP = arg['serverIP']
		self.outerPort = arg['outerPort']
		self.innerPort = arg['innerPort']
		self.protocol = arg['protocol']
		self.action = arg['action']

	def portForward(self):
		web.clickApp()
		web.srcollAction('bottom')
		web.waitandClick('//*[@id="AppList"]/ul[4]/a[4]/li')
		if self.enable == '0':
			web.alwaysCloseSwitch('//*[@id="SwitchFwd"]', 'data-value')
		else :
			web.alwaysOpenSwitch('//*[@id="SwitchFwd"]')
			self.actionFun()

	def actionFun(self):
		if self.action == 'add':
			if web.elementIsDisplayed('//*[@id="FwdTab"]/ul'):
				web.waitandClick('//*[@id="FwdTab"]/ul')

			web.waitandSendkeys('//*[@id="RuleName"]', self.ruleName)
			web.waitandSendkeys('//*[@id="ServerIp"]', self.serverIP)
			web.waitandSendkeys('//*[@id="ExternalPort"]', self.outerPort)
			web.waitandSendkeys('//*[@id="InternalPort"]', self.innerPort)
			web.waitandClick('//*[@id="PortAgreement"]/span')
			if self.protocol == 'TCP':
				web.waitandClick('//*[@id="sel-opts-ulPortAgreement"]/li[1]')
			elif self.protocol == 'UDP':
				web.waitandClick('//*[@id="sel-opts-ulPortAgreement"]/li[2]')
			else:
				web.waitandClick('//*[@id="sel-opts-ulPortAgreement"]/li[3]')

			if web.elementIsDisplayed('//*[@id="SaveAdd"]'):
				web.waitandClick('//*[@id="SaveAdd"]')
			elif web.elementIsDisplayed('//*[@id="SaveEdit"]'):
				web.waitandClick('//*[@id="SaveEdit"]')
		else :
			arr = ["", self.ruleName, self.serverIP, self.outerPort, self.innerPort, self.protocol]
			row = web.getElementInTable('//*[@id="PortfwdTab"]','//*[@id="PortfwdTab"]/tbody', arr)
			if row == 0:
				print('no such line~~~')
			else:
				if self.action == 'del':
					xpath = '//*[@id="PortfwdTab"]/tbody/tr[%d]/td[6]/span[2]' % row
					web.waitandClick(xpath)
				elif self.action == 'modify':
					xpath = '//*[@id="PortfwdTab"]/tbody/tr[%d]/td[6]/span[1]' % row
					web.waitandClick(xpath)
				else:
					print('input right action')
					web.wirteDataErrToLog('portForward', 'action', self.action, sys._getframe().f_lineno,\
					'please input right action: add, del, modify' )

def main(data, newData=""):
	log.wirteLog(data, 'portForward', 1)
	portForwardObj = portForwardClass(data)
	portForwardObj.portForward()
	if newData != "":
		log.wirteLog(newData, 'portForward-modify', 1)
		newData['action'] = 'add'
		newData['enable'] = '1'
		portForwardObj = portForwardClass(newData)
		portForwardObj.actionFun()
	log.wirteLog(data, 'portForward', 2)
