# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   guide.py
# VERSION    :   1.0
# DESCRIPTION:   快速向导
# AUTHOR     :   LiuLu <lu.liu@phicomm.com>
# CREATE DATE:   04/06/2017
#
##############################################################
import login
import sys
import adaptor, log, configApi, debug
sys.path.append('../data')
import loginData, guideData
import time

class baseClass(object):
	"""docstring for guideClass"""
	def __init__(self, arg):
		self.login_pwd = arg.get('login_pwd', '')
		self.setPwd = arg.get('setPwd', '')
		self.ssid_24G = arg.get('ssid_24G', '')
		self.pwd_24G = arg.get('pwd_24G', "")
		self.ssid_5G = arg.get('ssid_5G', '')
		self.pwd_5G = arg.get('pwd_5G', '')

	def mode_guide(self):
		raise NotImplementedError

	def pwdSet(self):
		if (self.setPwd != 'False' ):
			adaptor.waitandClick('//*[@id="Start"]')
			adaptor.waitandSendkeys('//*[@id="PwdNew"]', self.login_pwd)
			adaptor.waitandSendkeys('//*[@id="PwdCfm"]', self.login_pwd)
			adaptor.waitandClick('//*[@id="Save"]')
			time.sleep(1)
			configApi.cfgSet('loginData', 'login_data', 'login_pwd', self.login_pwd)
		else:
			login.main(loginData.login_data)

	def networkSet(self):
		adaptor.waitforDisplay('//*[@id="Pop"]')
		adaptor.waitforDisappear('//*[@id="Pop"]')
		adaptor.waitandClick('//*[@id="WanType"]/span')
		self.mode_guide()
		adaptor.waitandClick('//*[@id="Save"]')

	def wifiSet(self):
		adaptor.waitforDisappear('//*[@id="Pop"]')
		adaptor.waitandSendkeys('//*[@id="Ssid2G"]', self.ssid_24G)
		adaptor.waitandSendkeys('//*[@id="Pwd2G"]', self.pwd_24G)
		adaptor.waitandSendkeys('//*[@id="Ssid5G"]', self.ssid_5G)
		adaptor.waitandSendkeys('//*[@id="Pwd5G"]', self.pwd_5G)

	def guide(self):
		self.pwdSet()
		self.networkSet()
		self.wifiSet()
		adaptor.waitandClick('//*[@id="SaveReboot"]')

class dhcpClass(baseClass):
	"""docstring for dhcpClass"""
	def mode_guide(self):
		adaptor.waitandClick('//*[@id="sel-opts-ulWanType"]/li[1]')

class pppoeClass(baseClass):
	"""docstring for ppoeClass"""
	def __init__(self, arg):
		super(pppoeClass, self).__init__(arg)#调用基类构造函数
		self.pppoePwd = arg.get('pppoePwd', '')
		self.pppoeUser = arg.get('pppoeUser', '')
	def mode_guide(self):
		adaptor.waitandClick('//*[@id="sel-opts-ulWanType"]/li[2]')
		adaptor.waitandSendkeys('//*[@id="PppoeUser"]', self.pppoeUser)
		adaptor.waitandSendkeys('//*[@id="PppoePwd"]', self.pppoePwd)

class staticClass(baseClass):
	"""docstring for staticClass"""
	def __init__(self, arg):
		super(staticClass, self).__init__(arg)
		self.ip = arg.get('ip', '')
		self.subMask = arg.get('subMask', '')
		self.gateway = arg.get('gateway','')
		self.dns1 = arg.get('dns1', '')
	def mode_guide(self):
		adaptor.waitandClick('//*[@id="sel-opts-ulWanType"]/li[3]')
		adaptor.waitandSendkeys('//*[@id="WanIpaddr"]', self.ip)
		adaptor.waitandSendkeys('//*[@id="WanMask"]', self.subMask)
		adaptor.waitandSendkeys('//*[@id="WanGw"]', self.gateway)
		adaptor.waitandSendkeys('//*[@id="PrimDns"]', self.dns1)


def classSelector(data):
	subClass = {
		'pppoe' : (lambda data: pppoeClass(data)),
		'dhcp' : (lambda data: dhcpClass(data)),
		'static' : (lambda data: staticClass(data))
	}
	return subClass.get(data['network_mode'], None)(data)

@log.writeFuncLog
def main(data):
	guideObj = classSelector(data)
	adaptor.openDriver()
	guideObj.guide()

if __name__ == '__main__':
	main(guideData.guide_data_1)
	main(guideData.guide_data_2)
	main(guideData.guide_data_3)
