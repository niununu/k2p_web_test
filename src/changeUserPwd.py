# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   
# VERSION    :   1.0
# DESCRIPTION:   修改管理员密码
#
# CREATE DATE:   04/06/2017
#
##############################################################
import sys 
sys.path.append('../api')
from api import *

class changePwdClass(object):
	"""docstring for changePwdClass"""
	def __init__(self, arg):
		self.pwdNew = arg['pwdNew']
		self.pwdOld = arg['pwdOld']

	def changeUserPwd(self):
		web.waitandClick('//*[@id="Con"]/div[1]/ul[2]/li[1]')
		web.waitandClick('//*[@id="Con"]/div[1]/ul[2]/li[1]/ul/li[2]')
		web.waitforDisplay('//*[@id="_Widget"]')
		web.waitandSendkeys('//*[@id="PwdOld"]', self.pwdOld)
		web.waitandSendkeys('//*[@id="PwdNew"]', self.pwdNew)
		web.waitandSendkeys('//*[@id="PwdCfm"]', self.pwdNew)

		web.waitandClick('//*[@id="SavePwd"]')

def main(data):
	log.wirteLog(data, 'changeUserPwd', 1)
	changePwdObj = changePwdClass(data)
	changePwdObj.changeUserPwd()
	log.wirteLog(data, 'changeUserPwd', 2)