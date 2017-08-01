
# networkset begin
Tue Jul  4 16:07:43 2017 
### Set Data
	{'login_pwd': 'admin'}
networkset, Tue Jul  4 16:07:43 2017 end


# networkset begin
Tue Jul  4 16:07:43 2017 
### Set Data
	{'pppoeUser': '123', 'pppoePwd': '123', 'moreSet': 'True', 'mode': 'pppoe', 'subMask': '255.255.0.0', 'ip': '10.10.10.1', 'dns2': '22.22.22.22', 'dns1': '11.11.11.11', 'gateway': '10.10.10.1', 'mtu': '1480'}
networkset, Tue Jul  4 16:07:43 2017 end


# changeUserPwd begin
Tue Jul  4 16:08:34 2017 
### Set Data
	{'login_pwd': 'admin'}
changeUserPwd, Tue Jul  4 16:08:34 2017 end

New password char error case:1  2  3
# changeUserPwd begin
Tue Jul  4 16:08:34 2017 
### Set Data
	{'pwdOld': '*', 'pwdNew': '1  2  3'}
changeUserPwd, Tue Jul  4 16:08:34 2017 end

New password len error case:admi
# changeUserPwd begin
Tue Jul  4 16:08:34 2017 
### Set Data
	{'pwdOld': '*', 'pwdNew': 'admi'}
changeUserPwd, Tue Jul  4 16:08:34 2017 end

New password blank error case
# changeUserPwd begin
Tue Jul  4 16:08:34 2017 
### Set Data
	{'pwdOld': '*', 'pwdNew': ''}
changeUserPwd, Tue Jul  4 16:08:34 2017 end

Old password blank error case
# changeUserPwd begin
Tue Jul  4 16:08:34 2017 
### Set Data
	{'pwdOld': '', 'pwdNew': ''}
changeUserPwd, Tue Jul  4 16:08:34 2017 end

Password wrong error case: 8dadla
# changeUserPwd begin
Tue Jul  4 16:08:34 2017 
### Set Data
	{'pwdOld': '8dadla', 'pwdNew': '12345678'}
changeUserPwd, Tue Jul  4 16:08:34 2017 end

Same password error case:admin
# changeUserPwd begin
Tue Jul  4 16:08:34 2017 
### Set Data
	{'pwdOld': '*', 'pwdNew': 'admin'}
changeUserPwd, Tue Jul  4 16:08:34 2017 end

