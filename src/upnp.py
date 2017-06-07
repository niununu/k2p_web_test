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
import web
import time

class upnpClass(object):
	"""docstring for upnpClass"""
	def __init__(self, arg):
		self.enable = arg['enable']

	def upnp(self):
		web.clickApp()
		time.sleep(1)
		web.executeJS("var q = document.getElementById('Content').scrollTop=10000")
		web.waitandClick('//*[@id="AppList"]/ul[5]/a[2]/li')

		if self.enable == '1':
			web.alwaysOpenSwitch('//*[@id="UpnpSwitch"]', 'data-value')
		else :
			web.alwaysCloseSwitch('//*[@id="UpnpSwitch"]', 'data-value')


def main(data):
	log.wirteLog(data, 'upnp', 1)
	upnpObj = upnpClass(data)
	upnpObj.upnp()
	log.wirteLog(data, 'upnp', 2)
