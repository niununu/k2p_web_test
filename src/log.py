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
import adapter
import time
localtime = time.asctime( time.localtime(time.time()))
logDir = '../log/log-%s.txt' % (time.strftime('%Y-%m-%d',time.localtime(time.time())))

def writeLog(data, moduleName, mode, errName="", xpath=""):
	fileObject = open(logDir, 'a')
	if mode == 1:#moduleBegin
		fileObject.write('\n%s, %s begin\n'%(localtime, moduleName))
		fileObject.write("Set Data :\n")
		for key in data:
			fileObject.write('		%s = %s\n' % (key, data[key]))
	else:#modulEnd
		fileObject.write('%s, %s end\n\n'%(localtime, moduleName))

def writewebErrToLog(funcName, errName="", xpath=""):
	fileObject = open(logDir, 'a')
	fileObject.write('webError:\nfunName:%s, error:%s, xpath:%s, \ntime:%s\n' % (funcName, errName, xpath, localtime))
	fileObject.close()
	try:
		adapter.closeDriver()
		os._exit(0)
	except :
		print('catch error, exit!!')

def writeDataErrToLog(funcName, data, value, line, tips=""):
	fileObject = open(logDir, 'a')
	fileObject.write('DataError:\nfunName:%s, data:%s, value:%s, line:%s\ntips:%s'\
		%(funcName, data, value, line, tips))
	fileObject.close()
	try:
		adapter.closeDriver()
		os._exit(0)
	except :
		print('catch error, exit!!')