# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   diagnose.py
# VERSION    :   1.0
# DESCRIPTION:   一键体检
# AUTHOR     :   LiuLu <lu.liu@phicomm.com>
# CREATE DATE:   
#
##############################################################
import adaptor,log
class diagnoseClass(object):
	"""docstring for diagnoseClass"""
	def __init__(self, arg):
		self.arg = arg
	def diagnose(self):
		adaptor.clickApp()
		adaptor.waitandClick('//*[@id="AppList"]/ul[3]/a[1]/li')
		adaptor.waitandClick('//*[@id="Start"]')

def main():
	log.writeFuncLog("", 1)
	diagnoseObj = diagnoseClass("")
	diagnoseObj.diagnose()
	log.writeFuncLog("", 2)
