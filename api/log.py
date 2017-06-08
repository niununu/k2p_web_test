# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   log.py
# VERSION    :   1.0
# DESCRIPTION:   将运行结果写入log
#
# CREATE DATE:   04/06/2017
#
##############################################################
import time
import browser as browser

localtime = time.asctime(time.localtime(time.time()))
logDir = '../log/log-%s.txt' % (time.strftime('%Y-%m-%d',time.localtime(time.time())))

def wirteLog(data, moduleName, mode, errName="", xpath=""):
	fileObject = open(logDir, 'a')
	if mode == 1:#moduleBegin
		fileObject.write('\n%s, %s begin\n'%(localtime, moduleName))
		if data != "":
			fileObject.write("Set Data :\n")
			for key in data:
				fileObject.write('		%s = %s\n' % (key, data[key]))
	else:#modulEnd
		fileObject.write('%s, %s end\n\n'%(localtime, moduleName))

def wirteWebErrToLog(funcName, errName="", xpath=""):
	fileObject = open(logDir, 'a')
	fileObject.write('WebError:\nfunName:%s, error:%s, xpath:%s, \ntime:%s\n' % (funcName, errName, xpath, localtime))
	fileObject.close()
	try:
		browser.closeDriver()
		os._exit(0)
	except :
		print('catch error, exit!!')

def wirteDataErrToLog(funcName, data, value, line="", tips=""):
	fileObject = open(logDir, 'a')
	fileObject.wirte('DataError:\nfunName:%s, data:%s, value:%s, line:%s\ntips:%s'\
		%(funcName, data, value, line, tips))
	fileObject.close()
	try:
		browser.closeDriver()
		os._exit(0)
	except :
		print('catch error, exit!!')