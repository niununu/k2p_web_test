# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   luci.sh
# VERSION    :   1.0
# DESCRIPTION:   K2P旧UI升级到新UI时，etc/config/luci文件配置适配
#
# CREATE DATE:   04/06/2017
#
##############################################################
import sys 
sys.path.append('../api')
from api import *



class loginClass(object):
	"""docstring for login"""
	login_pwd = ""
	def __init__(self, arg):
		self.login_pwd = arg['login_pwd']

	def login(self):
		web.waitandSendkeys('//*[@id="Pwd"]', self.login_pwd)
		web.waitandClick('//*[@id="Save"]')


def main(data):
	log.wirteLog(data, 'login', 1)
	browser.openDriver()
	test1 = loginClass(data)
	test1.login()
	log.wirteLog(data, 'login', 2)
