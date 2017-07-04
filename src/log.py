# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   log.py
# VERSION    :   1.0
# DESCRIPTION:   将运行结果写入log
#
# AUTHOR     :   LiuLu <lu.liu@phicomm.com>
# CREATE DATE:   04/06/2017
#
##############################################################
import adaptor
import time, sys
localtime = time.asctime( time.localtime(time.time()))
logDir = '../log/operation_log-%s.md' % (time.strftime('%Y-%m-%d',time.localtime(time.time())))
unitTestLogDir = '../log/unitTest-%s.md'% (time.strftime('%Y-%m-%d',time.localtime(time.time())))

def writeFuncLog(fun):
	def wrapper(*args, **kwargs):
		f=sys._getframe()
		moduleName=f.f_back.f_code.co_filename
		moduleName = moduleName.split('/')[-1]#去除文件路径
		moduleName = moduleName.split('.')[-2]#去除.py后缀

		with open(logDir, 'a') as fileObject:
			fileObject.write('\n# %s begin\n%s \n'%(moduleName, localtime))
			fileObject.write("### Set Data\n")
			for x in args:
				fileObject.write('\t%s\n' % x)
			for key in kwargs:
				fileObject.write('\t%s = %s\n' % (key, kwargs[key]))

		fun(*args, **kwargs)

		with open(logDir, 'a') as fileObject:
			fileObject.write('%s, %s end\n\n'%(moduleName, localtime))
	return wrapper

def writewebErrToLog(funcName="",errName="", xpath=""):
	with open(logDir, 'a') as fileObject:
		fileObject.write('**WebError**\n- funName:%s\n- error:%s\n- xpath:%s\n- time:%s\n' 
			% (funcName, errName, xpath, localtime))
	try:
		adaptor.closeDriver()
		sys.exit()
	except Exception as e:
		print e.__class__

def writeDataErrToLog(data, value, tips=""):
	f = sys._getframe()
	funcName = f.f_back.f_code.co_name
	line = f.f_back.f_lineno
	with open(logDir, 'a') as fileObject:
		fileObject.write('**DataError**\n- funName:%s\n- data:%s, value:%s\n- line:%s\n- tips:%s\n'
			%(funcName, data, value, line, tips))
	try:
		adaptor.closeDriver()
		sys.exit()
	except Exception as e:
		print e.__class__

def writeInfo(info):
	with open(logDir, 'a') as fileObject:
		fileObject.write(info)

def unitTestLog(title):
	strw = '#Unit Test:%s\n\n##Start Time:%s\n\n'%(title, localtime)
	strw = strw + '| TestCase%s| Status%s|\n| %s | %s |\n'%('\t'*4, '\t'*4, '-'*(9*4), '-'*(9*4))#数字实验打印效果得出
	with open(unitTestLogDir, 'a') as fileObject:
		fileObject.write(strw)

if __name__ == '__main__':
	pass