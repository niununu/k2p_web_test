# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   
# VERSION    :   1.0
# DESCRIPTION:   一键体检
# AUTHOR     :   LiuLu <lu.liu@phicomm.com>
# CREATE DATE:   
#
##############################################################
import adapter,log
class diagnodeClass(object):
	"""docstring for diagnodeClass"""
	def __init__(self, arg):
		self.arg = arg
	def diagnose(self):
		adapter.clickApp()
		adapter.waitandClick('//*[@id="AppList"]/ul[3]/a[1]/li')
		adapter.waitandClick('//*[@id="Start"]')

def main():
	log.writeLog("", 'diagnose', 1)
	diagnoseObj = diagnodeClass("")
	diagnoseObj.diagnose()
	log.writeLog("", 'diagnose', 2)
