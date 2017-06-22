# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   
# VERSION    :   1.0
# DESCRIPTION:   上网设置
# AUTHOR     :   LiuLu <lu.liu@phicomm.com>
# CREATE DATE:   
#
##############################################################
import time
import adapter, log
class networkSetClass(object):
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

	def networkSet(self):
		adapter.clickApp()
		adapter.srcollAction('top')

		adapter.waitandClick('//*[@id="AppList"]/ul[1]/a[2]/li')
		adapter.waitandClick('//*[@id="WanType"]')

		if self.mode == 'dhcp':#dhcp
			self.networkSet_dhcp()
		elif self.mode == 'pppoe':#pppoe
			self.networkSet_pppoe()
		elif self.mode == 'static':#static
			self.networkSet_static()
		else:
			adapter.writeadapterErrToLog('networkSet', 'input data error')
			print("please input right mode: dhcp, pppoe, static")
			return

		if self.moreSet == 'True':
			if self.mode == 'static':
				self.SeniorSet(flag = False)
			else:
				self.SeniorSet()

		adapter.srcollAction('bottom')
		adapter.waitandClick('//*[@id="Save"]')

	def networkSet_dhcp(self):
		adapter.waitandClick('//*[@id="sel-opts-ulWanType"]/li[1]')

	def networkSet_pppoe(self):
		adapter.waitandClick('//*[@id="sel-opts-ulWanType"]/li[2]')
		adapter.waitandSendkeys('//*[@id="PppoeUser"]', self.pppoeUser )
		adapter.waitandSendkeys('//*[@id="PppoePwd"]', self.pppoePwd )

	def networkSet_static(self):
		adapter.waitandClick('//*[@id="sel-opts-ulWanType"]/li[3]')
		adapter.waitandSendkeys('//*[@id="WanIpaddr"]', self.ip)
		adapter.waitandSendkeys('//*[@id="WanMask"]', self.subMask)
		adapter.waitandSendkeys('//*[@id="WanGw"]', self.gateway)
		adapter.waitandSendkeys('//*[@id="PrimDns"]', self.dns1)
		adapter.waitandSendkeys('//*[@id="SecDns"]', self.dns2)

	def SeniorSet(self, flag = True):
		adapter.srcollAction('bottom')
		adapter.waitandClick('//*[@id="SeniorSet"]')
		adapter.waitandSendkeys('//*[@id="Mtu"]', self.mtu)
		adapter.srcollAction('bottom')

		if flag:
			adapter.alwaysOpenSwitch('//*[@id="Switch"]', 'data-value')
			adapter.srcollAction('bottom')
			adapter.waitandSendkeys('//*[@id="SeniorPrimDns"]', self.dns1)
			adapter.waitandSendkeys('//*[@id="SeniorSecDns"]', self.dns2)

def main(data):
	log.writeLog(data, 'networkSet', 1)
	data_1 = networkSetClass(data)
	data_1.networkSet()
	log.writeLog(data, 'networkSet', 2)


