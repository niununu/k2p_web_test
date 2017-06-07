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
import time
class dmzClass(object):
	"""docstring for dmzClass"""
	def __init__(self, arg):
		self.ip = arg['ip']

	def setDmz(self):
		web.clickApp()
		time.sleep(1)

		web.srcollAction('bottom')
		web.waitandClick('//*[@id="AppList"]/ul[5]/a[1]/li')
		web.alwaysOpenSwitch('//*[@id="Switch"]', 'data-value')
		web.waitandSendkeys('//*[@id="DmzIp"]', self.ip)
		web.waitandClick('//*[@id="Save"]')

def main(data):
	log.wirteLog(data, 'dmz', 1)
	dmzObj = dmzClass(data)

	dmzObj.setDmz()
	log.wirteLog(data, 'dmz', 2)
