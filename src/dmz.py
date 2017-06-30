# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   dmz.py
# VERSION    :   1.0
# DESCRIPTION:   dmz主机
# AUTHOR     :   LiuLu <lu.liu@phicomm.com>
# CREATE DATE:   04/06/2017
#
##############################################################
import time
import adaptor, log
class dmzClass(object):
	"""docstring for dmzClass"""
	def __init__(self, arg):
		self.ip = arg.get('ip', '')

	def setDmz(self):
		adaptor.clickApp()
		adaptor.srcollAction('bottom')
		adaptor.waitandClick('//*[@id="AppList"]/ul[5]/a[1]/li')
		adaptor.alwaysOpenSwitch('//*[@id="Switch"]', 'data-value')
		adaptor.waitandSendkeys('//*[@id="DmzIp"]', self.ip)
		adaptor.waitandClick('//*[@id="Save"]')

def main(data):
	log.writeFuncLog(data, 1)
	dmzObj = dmzClass(data)

	dmzObj.setDmz()
	log.writeFuncLog(data, 2)
