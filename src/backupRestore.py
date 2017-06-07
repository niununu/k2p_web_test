# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   
# VERSION    :   1.0
# DESCRIPTION:   备份恢复
#
# CREATE DATE:   04/06/2017
#
##############################################################
import sys 
sys.path.append('../api')
from api import *

class backupClass(object):
	"""docstring for backupClass"""
	def __init__(self, arg):
		self.mode = arg['mode']
		self.backupFileDir = arg['backupFileDir']

	def backupRestore(self):
		web.clickApp()
		web.waitandClick('//*[@id="AppList"]/ul[2]/a[1]/li')
		if self.mode == '1':#generate backup file
			web.waitandClick('//*[@id="BackupCfg"]')
		elif self.mode == '2':#backup restore
			web.waitandSendkeys('//*[@id="ScanFile"]', self.backupFileDir)
		elif self.mode == '3':#reset
			web.waitandClick('//*[@id="Reset"]')
			web.waitforDisplay('//*[@id="Pop"]')
			web.waitandClick('//*[@id="Pop"]/div/div/input[2]')
		else:
			print ("please set right mode: 1-generate backup file, 2-backup restore, 3-reset")

def main(data):
	log.wirteLog(data, 'backupRestore', 1)
	backupObj = backupClass(data)
	backupObj.backupRestore()
	log.wirteLog(data, 'backupRestore', 2)

