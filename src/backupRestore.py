# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   backupRestore.py
# VERSION    :   1.0
# DESCRIPTION:   备份恢复
# AUTHOR     :   LiuLu <lu.liu@phicomm.com>
# CREATE DATE:   04/06/2017
#
##############################################################
import sys 
sys.path.append('../../k2p_web_test')
from data import loginData, backupRestoreData
import adaptor, log, login

class baseClass(object):
	"""docstring for baseClass"""
	def actionFun(self):
		raise NotImplementedError

	def backupRestore(self):
		adaptor.clickApp()
		adaptor.waitandClick('//*[@id="AppList"]/ul[2]/a[1]/li')
		self.actionFun()

class getBackupFileClass(baseClass):
	"""docstring for getBackupFileClass"""
	def actionFun(self):
		adaptor.waitandClick('//*[@id="BackupCfg"]')

class backupRestoreClass(baseClass):
	"""docstring for backupRestoreClass"""
	def __init__(self, arg):
		self.backupFileDir = arg.get('backupFileDir', "")

	def actionFun(self):
		adaptor.waitandSendkeys('//*[@id="ScanFile"]', self.backupFileDir)
		adaptor.waitandClick('//*[@id="RecoverCfg"]')

class resetClass(baseClass):
	"""docstring for resetClass"""
	def actionFun(self):
		adaptor.waitandClick('//*[@id="Reset"]')
		adaptor.waitforDisplay('//*[@id="Pop"]')
		adaptor.waitandClick('//*[@id="Pop"]/div/div/input[2]')

def classSelector(data):
	subClass = {
		'1' : (lambda data: getBackupFileClass()),
		'2' : (lambda data: backupRestoreClass(data)),
		'3' : (lambda data: resetClass())
	}
	return subClass.get(data['mode'], None)(data)

@log.writeFuncLog
def main(data):
	backupObj = classSelector(data)
	backupObj.backupRestore()

if __name__ == '__main__':
	login.main(loginData.login_data)
	main(backupRestoreData.backupRestore_data_1)

