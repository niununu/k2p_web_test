# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   debug.py
# VERSION    :   1.0
# DESCRIPTION:   debug接口
# AUTHOR     :   LiuLu <lu.liu@phicomm.com>
# CREATE DATE:   04/06/2017
#
##############################################################

#打印函数堆栈调用
# 使用
# @findcaller
# functionName
def findcaller(func):
    def wrapper(*args,**kwargs):
        import sys
        f=sys._getframe()
        filename=f.f_back.f_code.co_filename
        lineno=f.f_back.f_lineno
        print '######################################'
        print 'caller filename is ',filename
        print 'caller lineno is',lineno
        print 'the passed args is',args,kwargs
        print '######################################'
        func(*args,**kwargs)
    return wrapper