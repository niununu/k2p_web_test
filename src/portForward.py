# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   luci.sh
# VERSION    :   1.0
# DESCRIPTION:   K2P旧UI升级到新UI时，etc/config/luci文件配置适配
# AUTHOR     :   LiuLu <lu.liu@phicomm.com>
# CREATE DATE:   04/06/2017
#
##############################################################
import adapter, log
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
		adapter.clickApp()
		adapter.srcollAction('bottom')
		adapter.waitandClick('//*[@id="AppList"]/ul[4]/a[4]/li')
		if self.enable == '0':
			adapter.alwaysCloseSwitch('//*[@id="SwitchFwd"]', 'data-value')
		else :
			adapter.alwaysOpenSwitch('//*[@id="SwitchFwd"]')
			self.actionFun()

	def actionFun(self):
		if self.action == 'add':
			if adapter.elementIsDisplayed('//*[@id="FwdTab"]/ul'):
				adapter.waitandClick('//*[@id="FwdTab"]/ul')

			adapter.waitandSendkeys('//*[@id="RuleName"]', self.ruleName)
			adapter.waitandSendkeys('//*[@id="ServerIp"]', self.serverIP)
			adapter.waitandSendkeys('//*[@id="ExternalPort"]', self.outerPort)
			adapter.waitandSendkeys('//*[@id="InternalPort"]', self.innerPort)
			adapter.waitandClick('//*[@id="PortAgreement"]/span')
			if self.protocol == 'TCP':
				adapter.waitandClick('//*[@id="sel-opts-ulPortAgreement"]/li[1]')
			elif self.protocol == 'UDP':
				adapter.waitandClick('//*[@id="sel-opts-ulPortAgreement"]/li[2]')
			else:
				adapter.waitandClick('//*[@id="sel-opts-ulPortAgreement"]/li[3]')

			if adapter.elementIsDisplayed('//*[@id="SaveAdd"]'):
				adapter.waitandClick('//*[@id="SaveAdd"]')
			elif adapter.elementIsDisplayed('//*[@id="SaveEdit"]'):
				adapter.waitandClick('//*[@id="SaveEdit"]')
		else :
			arr = ["", self.ruleName, self.serverIP, self.outerPort, self.innerPort, self.protocol]
			row = adapter.getElementInTable('//*[@id="PortfwdTab"]','//*[@id="PortfwdTab"]/tbody', arr)
			if row == 0:
				print('no such line~~~')
			else:
				if self.action == 'del':
					xpath = '//*[@id="PortfwdTab"]/tbody/tr[%d]/td[6]/span[2]' % row
					adapter.waitandClick(xpath)
				elif self.action == 'modify':
					xpath = '//*[@id="PortfwdTab"]/tbody/tr[%d]/td[6]/span[1]' % row
					adapter.waitandClick(xpath)
				else:
					print('input right action')
					adapter.writeDataErrToLog('portForward', 'action', self.action, sys._getframe().f_lineno,\
					'please input right action: add, del, modify' )

def main(data, newData=""):
	log.writeLog(data, 'portForward', 1)
	portForwardObj = portForwardClass(data)
	portForwardObj.portForward()
	if newData != "":
		log.writeLog(newData, 'portForward-modify', 1)
		newData['action'] = 'add'
		newData['enable'] = '1'
		portForwardObj = portForwardClass(newData)
		portForwardObj.actionFun()
	log.writeLog(data, 'portForward', 2)
