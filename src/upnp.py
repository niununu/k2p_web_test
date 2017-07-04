# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   upnp.py
# VERSION    :   1.0
# DESCRIPTION:   upnp功能
# AUTHOR     :   LiuLu <lu.liu@phicomm.com>
# CREATE DATE:   04/06/2017
#
##############################################################
import adaptor, log
import time

class upnpClass(object):
	"""docstring for upnpClass"""
	def __init__(self, arg):
		self.enable = arg.get('enable', '')

	def upnp(self):
		adaptor.clickApp()
		adaptor.srcollAction('bottom')
		adaptor.waitandClick('//*[@id="AppList"]/ul[5]/a[2]/li')

		if self.enable == '1':
			adaptor.alwaysOpenSwitch('//*[@id="UpnpSwitch"]', 'data-value')
		else :
			adaptor.alwaysCloseSwitch('//*[@id="UpnpSwitch"]', 'data-value')

@log.writeFuncLog
def main(data):
	upnpObj = upnpClass(data)
	upnpObj.upnp()
