# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   
# VERSION    :   1.0
# DESCRIPTION:   备份恢复
# AUTHOR     :   LiuLu <lu.liu@phicomm.com>
# CREATE DATE:   04/06/2017
#
##############################################################
import adapter, log
class backupClass(object):
	"""docstring for backupClass"""
	def __init__(self, arg):
		self.mode = arg.get('mode', "")
		self.backupFileDir = arg.get('backupFileDir', "")

	def backupRestore(self):
		adapter.clickApp()
		adapter.waitandClick('//*[@id="AppList"]/ul[2]/a[1]/li')
		if self.mode == '1':#generate backup file
			adapter.waitandClick('//*[@id="BackupCfg"]')
		elif self.mode == '2':#backup restore
			adapter.waitandSendkeys('//*[@id="ScanFile"]', self.backupFileDir)
		elif self.mode == '3':#reset
			adapter.waitandClick('//*[@id="Reset"]')
			adapter.waitforDisplay('//*[@id="Pop"]')
			adapter.waitandClick('//*[@id="Pop"]/div/div/input[2]')
		else:
			print ("please set right mode: 1-generate backup file, 2-backup restore, 3-reset")
			log.writeDataErrToLog(backupRestore, 'mode', self.mode, '', 
				"please set right mode: 1-generate backup file, 2-backup restore, 3-reset")

def main(data):
	log.writeLog(data, 'backupRestore', 1)
	backupObj = backupClass(data)
	backupObj.backupRestore()
	log.writeLog(data, 'backupRestore', 2)

