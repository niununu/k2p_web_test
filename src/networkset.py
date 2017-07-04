# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   network.py
# VERSION    :   1.0
# DESCRIPTION:   上网设置
# AUTHOR     :   LiuLu <lu.liu@phicomm.com>
# CREATE DATE:   
#
##############################################################
import sys 
sys.path.append('../../k2p_web_test')
from data import loginData, networksetData
import login, adaptor, log
import time

class baseClass(object):
	"""docstring for networkSet"""
	def __init__(self, arg):
		self.dns1 = arg.get('dns1', '')
		self.dns2 = arg.get('dns2', '')
		self.mtu = arg.get('mtu', '')
		self.pppoePwd = arg.get('pppoePwd', '')
		self.pppoeUser = arg.get('pppoeUser', '')
		self.ip = arg.get('ip', '')
		self.subMask = arg.get('subMask', '')
		self.gateway = arg.get('gateway', '')
		self.mode = arg.get('mode', '')
		self.moreSet = arg.get('moreSet', '')

	def SeniorSet(self, flag = True):
		adaptor.srcollAction('bottom')
		adaptor.waitandClick('//*[@id="SeniorSet"]')
		adaptor.waitandSendkeys('//*[@id="Mtu"]', self.mtu)
		adaptor.srcollAction('bottom')

		if flag:
			adaptor.alwaysOpenSwitch('//*[@id="Switch"]', 'data-value')
			adaptor.srcollAction('bottom')
			adaptor.waitandSendkeys('//*[@id="SeniorPrimDns"]', self.dns1)
			adaptor.waitandSendkeys('//*[@id="SeniorSecDns"]', self.dns2)

	def mode_networkSet(self):
		raise NotImplementedError

	def networkSet(self):
		adaptor.clickApp()
		adaptor.srcollAction('top')
		adaptor.waitandClick('//*[@id="AppList"]/ul[1]/a[2]/li')
		adaptor.waitandClick('//*[@id="WanType"]')

		self.mode_networkSet()
		if self.moreSet == 'True':
			if self.mode == 'static':
				self.SeniorSet(flag = False)
			else:
				self.SeniorSet()

		adaptor.srcollAction('bottom')
		#adaptor.waitandClick('//*[@id="Save"]')

class dhcp_networkSet(baseClass):
	"""docstring for dhcp_networkSet"""
	def mode_networkSet(self):
		adaptor.waitandClick('//*[@id="sel-opts-ulWanType"]/li[1]')

class pppoe_networkSet(baseClass):
	"""docstring for pppoe_networkSet"""
	def mode_networkSet(self):
		adaptor.waitandClick('//*[@id="sel-opts-ulWanType"]/li[2]')
		adaptor.waitandSendkeys('//*[@id="PppoeUser"]', self.pppoeUser )
		adaptor.waitandSendkeys('//*[@id="PppoePwd"]', self.pppoePwd )

class static_networkSet(baseClass):
	"""docstring for static_networkSet"""
	def mode_networkSet(self):
		adaptor.waitandClick('//*[@id="sel-opts-ulWanType"]/li[3]')
		adaptor.waitandSendkeys('//*[@id="WanIpaddr"]', self.ip)
		adaptor.waitandSendkeys('//*[@id="WanMask"]', self.subMask)
		adaptor.waitandSendkeys('//*[@id="WanGw"]', self.gateway)
		adaptor.waitandSendkeys('//*[@id="PrimDns"]', self.dns1)
		adaptor.waitandSendkeys('//*[@id="SecDns"]', self.dns2)

def classSelector(data):
	subClass = {
		'pppoe' : (lambda data: pppoe_networkSet(data)),
		'dhcp' : (lambda data: dhcp_networkSet(data)),
		'static' : (lambda data: static_networkSet(data))
	}
	return subClass.get(data['mode'], None)(data)

@log.writeFuncLog
def main(data):
	networkSetObj = classSelector(data)
	networkSetObj.networkSet()


if __name__ == '__main__':
	login.main(loginData.login_data)
	main(networksetData.networkset_data_2)
	adaptor.closeDriver()


