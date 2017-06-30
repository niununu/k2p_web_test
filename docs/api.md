[TOC]
# 通用接口函数
## src/adaptor.py
### 数据
```python
driver = webdriver.Chrome() #驱动的浏览器
#driver = webdriver.Firefox()
networkRestartTime = 40 #重启网络时间
rebootTime = 70 #路由器重启时间
```
### 函数
#### 浏览器操作
```python
- def openDriver() #打开浏览器
- def closeDriver() #关闭浏览器
- def refresh() #刷新浏览器
```
#### 页面操作
```python
- def waitandClick(xpath) # 点击元素
- def waitandSendkeys(xpath, keys) #用keys填充元素空格
- def clickApp() #点击页面“功能设置”
- def srcollAction(site) #滚动条操作函数
#参数site=='top'滚到顶部，site=='bottom'滚到底部
- def alwaysOpenSwitch(xpath, switchValue='data-value') #保持元素的开关为开启
#switchValue:开关属性值，默认为'data-value'
- def alwaysCloseSwitch(xpath, switchValue='data-value') #保持xpath的开关为关闭
#switchValue:开关属性值，默认为'data-value'
- def waitforDisappear(xpath) #等待元素消失
- def waitforDisplay(xpath) #等待元素出现
- def elementIsDisplayed(xpath) #检查某个元素时候可见
#返回值：True-可见，False-不可见
- def getElementInTable(tableXpath, baseXpath, arrData) #检查arrData是否在表格tableXpath中
#baseXpath为该表格通用的xpath部分；存在返回行号，不存在返回0
- def getText(xpath) #返回页面元素的文本
```

## src/log.py
### 数据
```python
logDir = '../log/log-%s.txt' % (time.strftime('%Y-%m-%d',time.localtime(time.time())))
#日志文件存放目录，默认以日期命名
```
### 函数
```python
- def writeFuncLog(data, mode) #模块运行记录
#data:数据，moduleName:模块名, mode: 1-模块开始运行，2-模块运行结束
- def writewebErrToLog(errName="", xpath="") #页面错误记录
#funcName:出现错误的函数名, errName:错误名(可选), xpath:错误元素xpath(可选)
- def writeDataErrToLog(data, value, tips="") #输入数据错误记录
#funcName:出现错误的函数名，data:数据名称，value:输入的数据值，line:出现错误数据的行号，tips:提示(可选)
- def writeInfo(info) #写入信息到日志
#info:需要写入的信息
```

## src/configApi.py
### 函数
```python
- def cfgSet(fileName, section, key, value) #data目录下数据设置函数
#fileName:文件名,section:需要设置的数据结构名称,key:需要设置的字段，value：设置的值
```
举例: 修改'login_data'中'login_pwd'为'admin'
```python
login_data = {
	'login_pwd' : '12345678'
}

cfgSet('loginData', 'login_data', 'login_pwd', 'admin')
```

# 功能模块
## 上网设置
### 数据
路径: k2p_web_test/data/networksetData.py
```python
{
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

| 字段		|描述													|
|-----------|-------------------------------------------------------|
|mode		|上网方式（dhcp：自动获取，pppoe：宽带拨号，static：静态地址) |
|dns1		|首选dns													|
|dns2		|备用dns													|
|mtu		|mtu													|
|pppoePwd 	|pppoe拨号密码											|
|pppoeUser	|pppoe用户名												|
|ip			|ip 													|
|subMask	|子网掩码													|
|gateway	|默认网关													|
|moreSet	|高级设置（True：进行高级设置， False：不进行高级设置)		|

## 快速向导
### 数据
路径: k2p_web_test/data/guideData.py
```python
{
	'login_pwd': 'admin',
	'ssid_24G': '@PHICOMM_A9_uill',
	'pwd_24G': '12345678',
	'setPwd' : True
}
```

| 字段			| 描述		 |
|-------------- |------------|
|login_pwd		| 登录密码	 |
|ssid_24G		|2.4G无线ssid |
|pwd_24G		|2.4G无线密码	 |

## 一键体检

## 备份恢复
### 数据
路径: k2p_web_test/data/backupRestoreData.py
```python
{
	'mode' : '1',
	'backupFileDir' : "/Users/Downloads/dhcp.dat"
}
```

|	字段			| 描述										|
|-------------	|-------------------------------------------|
|mode			|功能选择（1:备份配置，2:恢复备份，3:恢复出厂设置)|
|backupFileDir	|需要恢复的备份文件目录							|

## 修改管理员密码
### 数据
路径: k2p_web_test/data/changeUserPwdData.py
```python
{
	"pwdNew" : "12345678",
	"pwdOld" : 'admin'
}
```

| 字段      	| 描述 			|
|---------	|---------------|
|pwdNew		|新密码密码		|
|pwdOld		|原密码			|

## dmz主机
### 数据
路径: k2p_web_test/data/dmz.py
```python
{
	'ip': '10.10.2.22'
}
```

|字段	|描述		|
|---	|----------	|
|ip		|dmz主机地址	|

## 端口转发
### 数据
路径: k2p_web_test/data/portForwardData.py
```python
{
	'action' : 'add',#add, del, modify
	'enable' : '1',
	'ruleName': '1',
	'serverIP': '10.10.10.3',
	'outerPort':'333',
	'innerPort': '444',
	'protocol':'TCP'
}
```

| 字段      	| 描述										|
| ---------	| ------------------------------------------|
| action	| 操作（add: 添加， modify: 修改，del: 删除		|
| enable	| 功能开关(1: 开启开关， 2: 关闭开关) 			|
| ruleName	| 规则名称 									|
| serverIP	| 服务器ip									|
| outerPort	| 外部端口									|
| innerPort	| 内部端口									|
| protocol	| 协议(TCP: TCP, UDP: UDP, TCP&UDP: TCP&UDP) |

## upnp
### 数据
路径: k2p_web_test/data/upnpData.py
```python
 {
	'enable': '0'
}
```

| 字段      	| 描述 							|
|---------	|-------------------------------|
|enable		|功能开关(1: 开启开关， 2: 关闭开关)|


