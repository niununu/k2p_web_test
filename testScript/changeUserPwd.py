# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   changeUserPwd.py
# VERSION    :   1.0
# DESCRIPTION:   修改管理员密码--覆盖全部测试用例
# AUTHOR     :   LiuLu <lu.liu@phicomm.com>
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
import sys, time
import unittest
import HtmlTestRunner
sys.path.append('../../k2p_web_test')
from src import *
from data import *
reload(sys)
sys.setdefaultencoding('utf-8') 

errcode = ['oldPwdErr', 'lenErr', 'charErr', 'matchErr', 'pwdSameErr',\
	'oldPwdBlankErr', 'newPwdBlankErr']
errTips = {
	'oldPwdErr' :'原密码错误',
	'lenErr' : '新密码长度应为5~63位',
	'charErr' : "新密码包含非法字符",
	'matchErr' : '两次密码输入不一致',
	'pwdSameErr' : '新密码与原密码相同',
	'oldPwdBlankErr' : '请输入原密码',
	'newPwdBlankErr' : '请输入新密码'
}

def checkData(data):#检查顺序跟页面顺序相同
	if data['pwdOld'] == "*" :
		pwd = loginData.login_data['login_pwd']
	else:
		pwd = data['pwdOld']

	#'oldPwdBlankErr'
	if data['pwdOld'] == "":
		log.writeInfo('Old password blank error case')
		return errcode[5]

	#newPwdBlankErr
	if data['pwdNew'] == "":
		log.writeInfo('New password blank error case')
		return errcode[6]

	#charErr
	strTmp = data['pwdNew']
	for x in xrange(0,len(data['pwdNew'])):
		if ord(strTmp[x]) < 33 or ord(strTmp[x]) > 127:#ASCII表示范围:32-127
			log.writeInfo('New password char error case:%s' % data['pwdNew'])
			return errcode[2]

	#lenErr
	if len(data['pwdNew']) > 63 or len(data['pwdNew']) < 5:
		log.writeInfo('New password len error case:%s' % data['pwdNew'])
		return errcode[1]

	#oldPwdErr
	if pwd != loginData.login_data['login_pwd']:
		log.writeInfo('Password wrong error case: %s'% data['pwdOld'])
		return errcode[0]

	if data['pwdNew'] == pwd:
		log.writeInfo('Same password error case:%s' % data['pwdNew'])
		return errcode[4]
	#pwdSameErr
	log.writeInfo('No error in data')
	return None


def matchErrFun():
	log.writeInfo('new password did not match confirm password error case\n')
	adaptor.waitandClick('//*[@id="Con"]/div[1]/ul[2]/li[1]')
	adaptor.waitandClick('//*[@id="Con"]/div[1]/ul[2]/li[1]/ul/li[3]')
	adaptor.waitforDisplay('//*[@id="_Widget"]')
	adaptor.waitandSendkeys('//*[@id="PwdOld"]', loginData.login_data['login_pwd'])
	adaptor.waitandSendkeys('//*[@id="PwdNew"]', '12345678')
	adaptor.waitandSendkeys('//*[@id="PwdCfm"]', 'gdkagkd')
	adaptor.waitandClick('//*[@id="SavePwd"]')

def checkResponse(error):
	if error == None:
		return
	webText = adaptor.getText('//*[@id="PwdTip"]')

	if webText == False:
		log.writeInfo('###Error: no tips on web!')
		pass
	else:
		webText = webText.decode('UTF-8')

	adaptor.waitandClick('//*[@id="ModifyPwd"]/i')
	time.sleep(1)
	return webText

class TestCase(unittest.TestCase):
	data = [
		{"pwdNew" : "12345678","pwdOld" : '8dadla'},#"oldPwdErr"
		{"pwdNew" : "admi","pwdOld" : '*'},#lenErr
		{'pwdNew' : '1  2  3','pwdOld' : '*'},#charErr
		{'pwdNew' : 'admin','pwdOld' : '*'},#pwdSameErr
		{'pwdNew' : "",'pwdOld' : ""},#oldPwdBlank
		{'pwdNew' : "",'pwdOld' : "*"}#newPwdBlank
	]

	def commonAction(self, arg):
		error = checkData(arg)
		changeUserPwd.main(arg)
		self.assertEqual(checkResponse(error), errTips[error])

	def test_oldPwdErr(self):
		self.commonAction(self.data[0])
	def test_lenErr(self):
		self.commonAction(self.data[1])
	def test_charErr(self):
		self.commonAction(self.data[2])
	def test_pwdSameErr(self):
		self.commonAction(self.data[3])
	def test_oldPwdBlank(self):
		self.commonAction(self.data[4])
	def test_newPwdBlank(self):
		self.commonAction(self.data[5])
	def test_matchErr(self):
		matchErrFun()
		error = checkResponse(errcode[3])
		self.assertEqual(checkResponse(error), errTips[error])

if __name__ == '__main__':
	login.main(loginData.login_data)
	#生成测试报告
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_report',report_title='修改管理员密码试报告'))
	#adaptor.closeDriver()



