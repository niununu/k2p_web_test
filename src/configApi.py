def cfgSet(fileName, section, key, value):
	path = "../data/%s.py"%fileName
	cfg = ""
	strOld = ""
	strNew = ""
	with open(path, 'r') as file_object:
		cfg = file_object.read()
		site1 = cfg.find(section)
		if site1 == -1:
			strNew = "%s{\n\t\'%s\' : \'%s\'\n}"%(section, key, value)
			cfg = cfg + "\n\n"+ strNew
			print cfg
		else:
			end1 = cfg.find('}', site1)
			site2 = cfg.find(key, site1, end1)
			if site2 == -1:
				strOld = cfg[site1 : end1 + 1]
				strNew = "%s,\n\t\'%s\' : \'%s\'\n}"%(cfg[site1 : end1 - 1], key, value)
			else:
				site3 = cfg.find('\n', site2)
				strOld = cfg[site1: site3]
				strNew = "%s\'%s\' : \'%s\'"%(cfg[site1: site2 - 1],key, value)
				if cfg[site3 - 1] == ',':
					strNew = strNew + ','
			cfg = cfg.replace(strOld, strNew)

	with open(path, 'w') as file_object:
		file_object.write(cfg)

if __name__ == '__main__':
	
	pass