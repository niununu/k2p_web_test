# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   
# VERSION    :   1.0
# DESCRIPTION:   上网设置
#
# CREATE DATE:   
#
##############################################################
import sys 
sys.path.append('../api')
from api import *
import time

class networkSetClass(object):
	def __init__(self, arg):
		self.dns1 = arg['dns1']
		self.dns2 = arg['dns2']
		self.mtu = arg['mtu']
		self.pppoePwd = arg['pppoePwd']
		self.pppoeUser = arg['pppoeUser']
		self.ip = arg['ip']
		self.subMask = arg['subMask']
		self.gateway = arg['gateway']
		self.mode = arg['mode']
		self.moreSet = arg['moreSet']

	def networkSet(self):
		web.clickApp()
		web.executeJS("var q = document.getElementById('Content').scrollTop=0")

		web.waitandClick('//*[@id="AppList"]/ul[1]/a[2]/li')
		web.waitandClick('//*[@id="WanType"]')

		if self.mode == 'dhcp':#dhcp
			self.networkSet_dhcp()
		elif self.mode == 'pppoe':#pppoe
			self.networkSet_pppoe()
		elif self.mode == 'static':#static
			self.networkSet_static()
		else:
			web.wirteWebErrToLog('networkSet', 'input data error')
			print("please input right mode: dhcp, pppoe, static")
			return

		if self.moreSet == 'True':
			if self.mode == 'static':
				self.SeniorSet(flag = False)
			else:
				self.SeniorSet()

		web.executeJS("var q = document.getElementById('Content').scrollTop=10000")
		web.waitandClick('//*[@id="Save"]')

	def networkSet_dhcp(self):
		web.waitandClick('//*[@id="sel-opts-ulWanType"]/li[1]')

	def networkSet_pppoe(self):
		web.waitandClick('//*[@id="sel-opts-ulWanType"]/li[2]')
		web.waitandSendkeys('//*[@id="PppoeUser"]', self.pppoeUser )
		web.waitandSendkeys('//*[@id="PppoePwd"]', self.pppoePwd )

	def networkSet_static(self):
		web.waitandClick('//*[@id="sel-opts-ulWanType"]/li[3]')
		web.waitandSendkeys('//*[@id="WanIpaddr"]', self.ip)
		web.waitandSendkeys('//*[@id="WanMask"]', self.subMask)
		web.waitandSendkeys('//*[@id="WanGw"]', self.gateway)
		web.waitandSendkeys('//*[@id="PrimDns"]', self.dns1)
		web.waitandSendkeys('//*[@id="SecDns"]', self.dns2)

	def SeniorSet(self, flag = True):
		web.executeJS("var q = document.getElementById('Content').scrollTop=10000")
		web.waitandClick('//*[@id="SeniorSet"]')
		web.waitandSendkeys('//*[@id="Mtu"]', self.mtu)
		web.executeJS("var q = document.getElementById('Content').scrollTop=10000")

		if flag:
			web.alwaysOpenSwitch('//*[@id="Switch"]', 'data-value')
			web.executeJS("var q = document.getElementById('Content').scrollTop=10000")
			web.waitandSendkeys('//*[@id="SeniorPrimDns"]', self.dns1)
			web.waitandSendkeys('//*[@id="SeniorSecDns"]', self.dns2)

def main(data):
	log.wirteLog(data, 'networkSet', 1)
	data_1 = networkSetClass(data)
	data_1.networkSet()
	log.wirteLog(data, 'networkSet', 2)


