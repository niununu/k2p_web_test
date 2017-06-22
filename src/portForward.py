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
	def __init__(self, arg):·
		self.enable = arg.get('enable', '1')
		self.ruleName = arg.get('ruleName', '')
		self.serverIP = arg.get('serverIP', '')
		self.outerPort = arg.get('outerPort', '')
		self.innerPort = arg.get('innerPort', '')
		self.protocol = arg.get('protocol', '')
		self.action = arg.get('action', '')

	def portForward(self):
		adapter.clickApp()
		adapter.srcollAction('bottom')
		adapter.waitandClick('//*[@id="AppList"]/ul[4]/a[4]/li')
		if self.enable == '0':
			adapter.alwaysCloseSwitch('//*[@id="SwitchFwd"]', 'data-value')
		else :
			adapter.alwaysOpenSwitch('//*[@id="SwitchFwd"]')
			self.actionFun()
		time.sleep(1)

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
			if row != 0:
				if self.action == 'del':
					xpath = '//*[@id="PortfwdTab"]/tbody/tr[%d]/td[6]/span[2]' % row
					adapter.waitandClick(xpath)
				elif self.action == 'modify':
					xpath = '//*[@id="PortfwdTab"]/tbody/tr[%d]/td[6]/span[1]' % row
					adapter.waitandClick(xpath)
				else:
					print('input right action')
					adapter.writeDataErrToLog('portForward', 'action', self.action, sys._getframe().f_lineno,
					'please input right action: add, del, modify' )

def main(data, newData=""):
	log.writeLog(data, ('portForward-%s'%data['action']), 1)
	portForwardObj = portForwardClass(data)
	portForwardObj.portForward()
	if newData != "":
		log.writeLog(newData, 'newData:', 1)
		newData['action'] = 'add'
		newData['enable'] = '1'
		portForwardObj = portForwardClass(newData)
		portForwardObj.actionFun()
	log.writeLog(data, 'portForward', 2)
