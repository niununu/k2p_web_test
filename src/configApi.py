def cfgSet(fileName, section, key, value):
	pass
	path = "../data/%s.py"%fileName
	#读取所有内容
	#file_object = open(path)
	with open(path) as file_object
	sectionFindFlag = False
	while True:
		lines = file_object.readline()
		if not lines:
			break
		if sectionFindFlag == False:
			if lines.find(section) != -1:
				sectionFindFlag = True
		else:
			if lines.find(key) != -1:
				#删除一行
				strInput = ('%s : %s') % (key, value)
				if lines.find(',') != -1:
					strInput = ('%s : %s,') % (key, value)
				#插入一行



