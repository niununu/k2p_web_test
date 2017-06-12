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
import login
import sys
import adapter, log
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
			adapter.waitandClick('//*[@id="Start"]')
			adapter.waitandSendkeys('//*[@id="PwdNew"]', self.login_pwd)
			adapter.waitandSendkeys('//*[@id="PwdCfm"]', self.login_pwd)
			adapter.waitandClick('//*[@id="Save"]')
			time.sleep(1)
		else:
			login.main(loginData.login_data_1)

		#adapter.waitforDisplay('//*[@id="Pop"]')
		adapter.waitforDisappear('//*[@id="Pop"]')
		adapter.waitandClick('//*[@id="WanType"]/span')

		if self.network_mode == 'dhcp':
			adapter.waitandClick('//*[@id="sel-opts-ulWanType"]/li[1]')
		elif self.network_mode == 'pppoe':
			adapter.waitandClick('//*[@id="sel-opts-ulWanType"]/li[2]')
			adapter.waitandSendkeys('//*[@id="PppoeUser"]', self.pppoeUser)
			adapter.waitandSendkeys('//*[@id="PppoePwd"]', self.pppoePwd)
		elif self.network_mode == 'static':
			adapter.waitandClick('//*[@id="sel-opts-ulWanType"]/li[3]')
			adapter.waitandSendkeys('//*[@id="WanIpaddr"]', self.ip)
			adapter.waitandSendkeys('//*[@id="WanMask"]', self.subMask)
			adapter.waitandSendkeys('//*[@id="WanGw"]', self.gateway)
			adapter.waitandSendkeys('//*[@id="PrimDns"]', self.dns1)
		else :
			print("please input right mode: dhcp, pppoe, static")
			log.writeadapterErrToLog('guide', 'input data error')

		#adapter.waitandClick('//*[@id="Save"]')

		adapter.waitforDisappear('//*[@id="Pop"]')
		adapter.waitandSendkeys('//*[@id="Ssid2G"]', self.ssid_24G)
		adapter.waitandSendkeys('//*[@id="Pwd2G"]', self.pwd_24G)
		adapter.waitandSendkeys('//*[@id="Ssid5G"]', self.ssid_5G)
		adapter.waitandSendkeys('//*[@id="Pwd5G"]', self.pwd_5G)

		adapter.waitandClick('//*[@id="SaveReboot"]')

def main(data):
	log.writeLog(data, 'guide', 1)
	guideObj = guideClass(data)
	adapter.openDriver()
	guideObj.guide()
	log.writeLog(data, 'guide', 2)
