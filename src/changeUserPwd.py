# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   changeUserPwd.py
# VERSION    :   1.0
# DESCRIPTION:   修改管理员密码
# AUTHOR     :   LiuLu <lu.liu@phicomm.com>
# CREATE DATE:   04/06/2017
#
##############################################################
import adaptor, log, configApi
import time, sys
sys.path.append('../data')
import loginData, changeUserPwdData

class changePwdClass(object):
	"""docstring for changePwdClass"""
	def __init__(self, arg):
		self.pwdNew = arg.get('pwdNew', '')
		if arg['pwdOld'] != "*":
			self.pwdOld = arg.get('pwdOld', '')
		else:
			self.pwdOld = loginData.login_data['login_pwd']

	def changeUserPwd(self):
		adaptor.waitandClick('//*[@id="Con"]/div[1]/ul[2]/li[1]')
		adaptor.waitandClick('//*[@id="Con"]/div[1]/ul[2]/li[1]/ul/li[3]')
		adaptor.waitforDisplay('//*[@id="_Widget"]')
		adaptor.waitandSendkeys('//*[@id="PwdOld"]', self.pwdOld)
		adaptor.waitandSendkeys('//*[@id="PwdNew"]', self.pwdNew)
		adaptor.waitandSendkeys('//*[@id="PwdCfm"]', self.pwdNew)

		adaptor.waitandClick('//*[@id="SavePwd"]')
		time.sleep(1)
		if adaptor.elementIsDisplayed('//*[@id="Pwd"]'):
			configApi.cfgSet('loginData', 'login_data', 'login_pwd', self.pwdNew)

def main(data):
	log.writeFuncLog(data, 1)
	changePwdObj = changePwdClass(data)
	changePwdObj.changeUserPwd()
	log.writeFuncLog(data, 2)

if __name__ == '__main__':
	login.main(loginData.login_data)
	main(changeUserPwdData.changeUserPwd_data_1)
