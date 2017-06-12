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
import time
import adapter, log
class dmzClass(object):
	"""docstring for dmzClass"""
	def __init__(self, arg):
		self.ip = arg['ip']

	def setDmz(self):
		adapter.clickApp()
		time.sleep(1)

		adapter.srcollAction('bottom')
		adapter.waitandClick('//*[@id="AppList"]/ul[5]/a[1]/li')
		adapter.alwaysOpenSwitch('//*[@id="Switch"]', 'data-value')
		adapter.waitandSendkeys('//*[@id="DmzIp"]', self.ip)
		adapter.waitandClick('//*[@id="Save"]')

def main(data):
	log.writeLog(data, 'dmz', 1)
	dmzObj = dmzClass(data)

	dmzObj.setDmz()
	log.writeLog(data, 'dmz', 2)
