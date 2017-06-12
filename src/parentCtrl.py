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

class parentCtrlClass(object):
	"""docstring for parentCtrlClass"""
	def __init__(self, arg):
		self.action = arg['action']

	def parentCtrl(self):
		#adapter.waitandClick
		adapter.clickApp()
		adapter.waitandClick('//*[@id="AppList"]/ul[1]/a[4]/li')
		adapter.alwaysOpenSwitch('//*[@id="SwitchParent"]', 'data-value')
		adapter.waitforDisappear('//*[@id="Pop"]')
		if self.action == 'add':
			self.addRule()
		elif self.action == 'modify':
			self.modifyRule()
		elif self.action == 'delete':
			self.delRule()
		else :
			print("please input right action: add, modify, delete")

	def addRule(self):
		adapter.waitandSendkeys('//*[@id="RuleName"]', '123')
	def delRule(self):
		pass
	def modifyRule(self):
		pass

def main(data):
	log.writeLog(data, 'parentCtrl', 1)
	parentCtrlObj = parentCtrlClass(data)
	parentCtrlObj.parentCtrl()
	log.writeLog(data, 'parentCtrl', 2)
