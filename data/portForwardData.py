port_forward_data_1 = {
	'action' : 'add',#add, del, modify
	'enable' : '1',
	'ruleName': '1',
	'serverIP': '10.10.10.3',
	'outerPort':'333',
	'innerPort': '444',
	'protocol':'TCP'#tcp, udp, both
}
new_port_forward_data_1 = {
	'ruleName': '12',
	'serverIP': '10.10.10.33',
	'outerPort':'1111',
	'innerPort': '2222',
	'protocol':'TCP'#tcp, udp, both
}

data_list_1 = [
	{
	'action' : '',#add, del, modify
	'enable' : '1',
	'ruleName': '1',
	'serverIP': '10.10.10.3',
	'outerPort':'333',
	'innerPort': '444',
	'protocol':'TCP'#tcp, udp, both
	},
	{
	'action' : '',#add, del, modify
	'enable' : '1',
	'ruleName': '2',
	'serverIP': '10.10.10.3',
	'outerPort':'3335',
	'innerPort': '4445',
	'protocol':'UDP'#tcp, udp, both
	},
	{
	'action' : '',#add, del, modify
	'enable' : '1',
	'ruleName': '3',
	'serverIP': '10.10.10.7',
	'outerPort':'3235',
	'innerPort': '2445',
	'protocol':'TCP&UDP'#tcp, udp, both
	}
]

data_list_2 = [
	{
	'ruleName': '12',
	'serverIP': '10.10.10.33',
	'outerPort':'1111',
	'innerPort': '2222',
	'protocol':'TCP'#tcp, udp, both
	},
	{
	'ruleName': '124',
	'serverIP': '10.10.10.123',
	'outerPort':'1145',
	'innerPort': '2278',
	'protocol':'TCP&UDP'#tcp, udp, both
	},
	{
	'ruleName': '12',
	'serverIP': '10.10.10.33',
	'outerPort':'11111',
	'innerPort': '22',
	'protocol':'TCP'#tcp, udp, both
	}
]
