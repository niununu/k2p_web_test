# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   portForward.py
# VERSION    :   1.0
# DESCRIPTION:   端口转发
# AUTHOR     :   LiuLu <lu.liu@phicomm.com>
# CREATE DATE:   04/06/2017
#
##############################################################
import adaptor, log, login
import sys
sys.path.append('../../k2p_web_test')
from data import loginData, portForwardData
import time

class baseClass(object):
	"""docstring for baseClass"""
	def __init__(self, arg):
		self.enable = arg.get('enable', '1')
		self.ruleName = arg.get('ruleName', '')
		self.serverIP = arg.get('serverIP', '')
		self.outerPort = arg.get('outerPort', '')
		self.innerPort = arg.get('innerPort', '')
		self.protocol = arg.get('protocol', '')
		self.action = arg.get('action', '')

	def portForward(self):
		adaptor.clickApp()
		adaptor.srcollAction('bottom')
		adaptor.waitandClick('//*[@id="AppList"]/ul[4]/a[4]/li')
		if self.enable == '0':
			adaptor.alwaysCloseSwitch('//*[@id="SwitchFwd"]', 'data-value')
		else :
			adaptor.alwaysOpenSwitch('//*[@id="SwitchFwd"]')
			self.actionFun()
		time.sleep(1)

	def getElement(self):
		arr = ["", self.ruleName, self.serverIP, self.outerPort, self.innerPort, self.protocol]
		return (adaptor.getElementInTable('//*[@id="PortfwdTab"]','//*[@id="PortfwdTab"]/tbody', arr))

	def actionFun(self):
		raise NotImplementedError

class addRuleClass(baseClass):
	"""docstring for addClass"""
	def actionFun(self):
		pass
		if adaptor.elementIsDisplayed('//*[@id="FwdTab"]/ul'):
			adaptor.waitandClick('//*[@id="FwdTab"]/ul')

		adaptor.waitandSendkeys('//*[@id="RuleName"]', self.ruleName)
		adaptor.waitandSendkeys('//*[@id="ServerIp"]', self.serverIP)
		adaptor.waitandSendkeys('//*[@id="ExternalPort"]', self.outerPort)
		adaptor.waitandSendkeys('//*[@id="InternalPort"]', self.innerPort)

		adaptor.waitandClick('//*[@id="PortAgreement"]/span')
		if self.protocol == 'TCP':
			adaptor.waitandClick('//*[@id="sel-opts-ulPortAgreement"]/li[1]')
		elif self.protocol == 'UDP':
			adaptor.waitandClick('//*[@id="sel-opts-ulPortAgreement"]/li[2]')
		else:
			adaptor.waitandClick('//*[@id="sel-opts-ulPortAgreement"]/li[3]')

		if adaptor.elementIsDisplayed('//*[@id="SaveAdd"]'):
			adaptor.waitandClick('//*[@id="SaveAdd"]')
		elif adaptor.elementIsDisplayed('//*[@id="SaveEdit"]'):
			adaptor.waitandClick('//*[@id="SaveEdit"]')

class delRuleClass(baseClass):
	"""docstring for delRuleClass"""
	def actionFun(self):
		pass
		row = self.getElement()
		if row != 0:
			xpath = '//*[@id="PortfwdTab"]/tbody/tr[%d]/td[6]/span[2]' % row
			adaptor.waitandClick(xpath)
class modifyRuleClass(baseClass):
	"""docstring for modifyRuleClass"""
	def actionFun(self):
		pass
		row = self.getElement()
		if row != 0:
			xpath = '//*[@id="PortfwdTab"]/tbody/tr[%d]/td[6]/span[1]' % row
			adaptor.waitandClick(xpath)

def classSelector(data):
	subClass = {
		'add': (lambda data: addRuleClass(data)),
		'del': (lambda data: delRuleClass(data)),
		'modify': (lambda data: modifyRuleClass(data))
	}
	return subClass.get(data['action'], None)(data)

@log.writeFuncLog
def main(data, newData=""):
	portForwardObj = classSelector(data)
	portForwardObj.portForward()
	if newData != "":
		newData['action'] = 'add'
		newData['enable'] = '1'
		portForwardObj = classSelector(newData)
		portForwardObj.actionFun()

if __name__ == '__main__':
	login.main(loginData.login_data)
	main(portForwardData.port_forward_data_1)

