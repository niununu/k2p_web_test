# -*- coding: UTF-8 -*-
#!/usr/bin/env python

#pwdOld为*时自动获取正确用户密码
data_list_1 = [
	{
		"pwdNew" : "12345678",#"oldPwdErr"
		"pwdOld" : '8dadla'
	},
	{
		"pwdNew" : "admi",#lenErr
		"pwdOld" : '*'
	},
	{
		'pwdNew' : '1  2  3',#charErr
		'pwdOld' : '*'
	},
	{
		'pwdNew' : '12345678',#pwdSameErr
		'pwdOld' : '*'
	},
	{
		'pwdNew' : "",#oldPwdBlank
		'pwdOld' : ""
	},
	{
		'pwdNew' : "",#newPwdBlank
		'pwdOld' : "*"
	}
]