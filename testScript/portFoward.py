import sys 
sys.path.append('../../k2p_web_test')
from data import *
from src import *
import time

sleepTime = 2

def addRule():
	data = portForwardData.data_list_1
	for x in xrange(0,len(data)):
		data[x]['enable'] = '1'
		data[x]['action'] = 'add'
		portForward.main(data[x])
		time.sleep(sleepTime)

def modifyRule():
	data = portForwardData.data_list_1
	new_data = portForwardData.data_list_2
	for x in xrange(0,len(data) if len(data)<len(new_data) else len(new_data)):
		data[x]['enable'] = '1'
		data[x]['action'] = 'modify'
		portForward.main(data[x], new_data[x])
		time.sleep(sleepTime)

def delRule():
	data = portForwardData.data_list_2
	for x in xrange(0,len(data)):
		data[x]['enable'] = '1'
		data[x]['action'] = 'del'
		portForward.main(data[x])
		time.sleep(sleepTime)

def main():
	login.main(loginData.login_data)
	#addRule()
	#modifyRule()
	delRule()

if __name__ == '__main__':
	main()






