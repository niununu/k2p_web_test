# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   
# VERSION    :   1.0
# DESCRIPTION:   修改管理员密码--覆盖全部测试用例
#
# CREATE DATE:   04/06/2017
#
##############################################################

'''修改管理员密码防呆规则
|输入项		|允许输入|可为空	|格式规范|合法性						   |依赖项
|:----------|:-----	|:------|:------|:-----------------------------|:-------
|原管理员密码	|是 		|否 		|字符串	|长度限制:5-63; 字符集:英文字符集; |需要与管理员密码相同
|新管理员密码	|是 		|否 		|字符串	|长度限制:5-63; 字符集:英文字符集; |
|确认管理员密码|是 	|否 		|字符串	|需要与新管理员密码相同				|
'''
import sys
sys.path.append('../src')
sys.path.append('../data')
sys.path.append('../api')
from src import changeUserpwd
from data import changeUserpwdData
from api import *

usrPwd = 'admin'
errCode = ['oldPwdErr', 'lenErr', 'charErr', 'matchErr']
def checkData(data):
	if data['pwdOld'] != usrPwd:
		log.writeDataErrToLog('checkData', 'pwdOld', data['pwdOld'],"","wrong user password")
		return errcode[0]#"oldPwdErr"

	if len(pwd) > 63 || len(pwd) < 5:
		log.writeDataErrToLog('pwdCheck', 'pwdNew', data['pwdNew'], "", "lenth error")
		return errcode[1]#"lenErr"

	for x in xrange(0,len(pwd) - 1):
		if pwd[x] < 0x20 || pwd[x] > 0x7E:#ASCII表示范围:0x20-0x7E
			log.writeDataErrToLog('pwdCheck', 'pwdNew', data['pwdNew'], "", 'char error')
			return errcode[2]#"charErr"




def main():
	pass
