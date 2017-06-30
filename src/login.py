# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   login.py
# VERSION    :   1.0
# DESCRIPTION:   登陆
# AUTHOR     :   LiuLu <lu.liu@phicomm.com>
# CREATE DATE:   04/06/2017
#
##############################################################
import adaptor, log

class loginClass(object):
	"""docstring for login"""
	def __init__(self, arg):
		self.login_pwd = arg.get('login_pwd', '')

	def login(self):
		adaptor.waitandSendkeys('//*[@id="Pwd"]', self.login_pwd)
		adaptor.waitandClick('//*[@id="Save"]')

def main(data):
	log.writeFuncLog(data, 1)
	adaptor.openDriver()
	test1 = loginClass(data)
	test1.login()
	log.writeFuncLog(data, 2)
