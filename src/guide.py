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
import login

sys.path.append('../data')
import loginData
import time

class guideClass(object):
	"""docstring for guideClass"""
	def __init__(self, arg):
		self.login_pwd = arg['login_pwd']
		self.ssid_24G = arg['ssid_24G']
		self.ssid_5G = arg['ssid_5G']
		self.pwd_24G = arg['pwd_24G']
		self.pwd_5G = arg['pwd_5G']
		self.setPwd = arg['setPwd']
		self.network_mode = arg['network_mode']
		self.pppoePwd = arg['pppoePwd']
		self.pppoeUser = arg['pppoeUser']
		self.ip = arg['ip']
		self.subMask = arg['subMask']
		self.gateway = arg['gateway']
		self.dns1 = arg['dns1']

	def guide(self):
		if (self.setPwd == 'True' ):
			web.waitandClick('//*[@id="Start"]')
			web.waitandSendkeys('//*[@id="PwdNew"]', self.login_pwd)
			web.waitandSendkeys('//*[@id="PwdCfm"]', self.login_pwd)
			web.waitandClick('//*[@id="Save"]')
			time.sleep(1)
		else:
			login.main(loginData.login_data_1)

		#web.waitforDisplay('//*[@id="Pop"]')
		web.waitforDisappear('//*[@id="Pop"]')
		web.waitandClick('//*[@id="WanType"]/span')

		if self.network_mode == 'dhcp':
			web.waitandClick('//*[@id="sel-opts-ulWanType"]/li[1]')
		elif self.network_mode == 'pppoe':
			web.waitandClick('//*[@id="sel-opts-ulWanType"]/li[2]')
			web.waitandSendkeys('//*[@id="PppoeUser"]', self.pppoeUser)
			web.waitandSendkeys('//*[@id="PppoePwd"]', self.pppoePwd)
		elif self.network_mode == 'static':
			web.waitandClick('//*[@id="sel-opts-ulWanType"]/li[3]')
			web.waitandSendkeys('//*[@id="WanIpaddr"]', self.ip)
			web.waitandSendkeys('//*[@id="WanMask"]', self.subMask)
			web.waitandSendkeys('//*[@id="WanGw"]', self.gateway)
			web.waitandSendkeys('//*[@id="PrimDns"]', self.dns1)
		else :
			print("please input right mode: dhcp, pppoe, static")
			log.wirteWebErrToLog('guide', 'input data error')

		#web.waitandClick('//*[@id="Save"]')

		web.waitforDisappear('//*[@id="Pop"]')
		web.waitandSendkeys('//*[@id="Ssid2G"]', self.ssid_24G)
		web.waitandSendkeys('//*[@id="Pwd2G"]', self.pwd_24G)
		web.waitandSendkeys('//*[@id="Ssid5G"]', self.ssid_5G)
		web.waitandSendkeys('//*[@id="Pwd5G"]', self.pwd_5G)

		web.waitandClick('//*[@id="SaveReboot"]')

def main(data):
	log.wirteLog(data, 'guide', 1)
	guideObj = guideClass(data)
	web.openDriver()
	guideObj.guide()
	log.wirteLog(data, 'guide', 2)
