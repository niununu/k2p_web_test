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
import sys 
sys.path.append('../api')
from api import *

class diagnodeClass(object):
	"""docstring for diagnodeClass"""
	def __init__(self, arg):
		self.arg = arg
	def diagnose(self):
		web.clickApp()
		web.waitandClick('//*[@id="AppList"]/ul[3]/a[1]/li')
		web.waitandClick('//*[@id="Start"]')

def main():
	log.wirteLog("", 'diagnose', 1)
	diagnoseObj = diagnodeClass("")
	diagnoseObj.diagnose()
	log.wirteLog("", 'diagnose', 2)
