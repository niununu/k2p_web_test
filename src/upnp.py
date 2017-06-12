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
import time

class upnpClass(object):
	"""docstring for upnpClass"""
	def __init__(self, arg):
		self.enable = arg['enable']

	def upnp(self):
		adapter.clickApp()
		time.sleep(1)
		adapter.executeJS("var q = document.getElementById('Content').scrollTop=10000")
		adapter.waitandClick('//*[@id="AppList"]/ul[5]/a[2]/li')

		if self.enable == '1':
			adapter.alwaysOpenSwitch('//*[@id="UpnpSwitch"]', 'data-value')
		else :
			adapter.alwaysCloseSwitch('//*[@id="UpnpSwitch"]', 'data-value')

def main(data):
	log.writeLog(data, 'upnp', 1)
	upnpObj = upnpClass(data)
	upnpObj.upnp()
	log.writeLog(data, 'upnp', 2)
