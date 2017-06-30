
networkset_data_1= {
	'mode' : 'dhcp',#dhcp
	'dns1': '114.114.114.114',
	'dns2': '8.8.8.8',
	'mtu': '1492',
	'pppoePwd': '',
	'pppoeUser': '',
	'ip': '192.168.2.1',
	'subMask': '255.255.255.0',
	'gateway': '192.168.2.1',
	'moreSet' : 'False'
}

networkset_data_2= {
	'mode' : 'pppoe',#pppoe
	'dns1': '11.11.11.11',
	'dns2': '22.22.22.22',
	'mtu': '1480',
	'pppoePwd': '123',
	'pppoeUser': '123',
	'ip': '10.10.10.1',
	'subMask': '255.255.0.0',
	'gateway': '10.10.10.1',
	'moreSet' : 'True'
}

networkset_data_3= {
	'mode' : 'static',#static
	'dns1': '10.10.10.1',
	'dns2': '',
	'mtu': '1492',
	'pppoePwd': '',
	'pppoeUser': '',
	'ip': '191.168.2.209',
	'subMask': '255.255.0.0',
	'gateway': '191.168.2.1',
	'moreSet' : 'True'
}