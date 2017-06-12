#API
##上网设置
###数据-networksetData.py
```python
networkset_data_1= {
	'mode' : 'dhcp',
	'dns1': '114.114.114.114',
	'dns2': '8.8.8.8',
	'mtu': '1492',
	'pppoePwd': '',
	'pppoeUser': '',
	'ip': '192.168.2.1',
	'subMask': '255.255.255.0',
	'gateway': '192.168.2.1',
	'moreSet' : False
}
```
| 字段		| 描述
| :-------	| :---------- 
|mode		| 上网方式（dhcp：自动获取，pppoe：宽带拨号，static：静态地址）
|dns1		|首选dns
|dns2		|备用dns
|mtu		|mtu
|pppoePwd 	|pppoe拨号密码
|pppoeUser	|pppoe用户名
|ip			|ip
|subMask	|子网掩码
|gateway	|默认网关
|moreSet	|高级设置（True：进行高级设置， False：不进行高级设置）


##无线设置
###data
##快速向导
###guideData
```python
guide_data_1 = {
	'login_pwd': 'admin',
	'ssid_24G': '@PHICOMM_A9_uill',
	'pwd_24G': '12345678',
	'setPwd' : True
}
```
| 字段			| 描述
| :----------	| :---------- 
|login_pwd		| 登录密码
|ssid_24G		|2.4G无线ssid
|pwd_24G		|2.4G无线密码

##一键体检
##备份恢复
###data
```python
backupRestore_data_1 = {
	'mode' : '1',
	'backupFileDir' : "/Users/Downloads/dhcp.dat"
}
```
|	字段			| 描述
| :-------------| :---------- 
|mode			|功能选择（1:备份配置，2:恢复备份，3:恢复出厂设置）
|backupFileDir	|需要恢复的备份文件目录

##修改管理员密码
```python
changeUserPwd_data_1 = {
	"pwdNew" : "12345678",
	"pwdOld" : 'admin'
}
```
| 字段      	| 描述 
| :---------| :---------------
|pwdNew		|新密码密码
|pwdOld		|原密码