import sys 
sys.path.append('../../k2p_web_test')
from data import *
from src import *
import time

sleepTime = 3

def addRule():
	portForwardData.port_forward_data_1['action'] = "add"
	portForwardData.port_forward_data_2['action'] = "add"
	portForwardData.port_forward_data_3['action'] = "add"

	portForward.main(portForwardData.port_forward_data_1)
	time.sleep(sleepTime)
	portForward.main(portForwardData.port_forward_data_2)
	time.sleep(sleepTime)
	portForward.main(portForwardData.port_forward_data_3)


def modifyRule():
	portForwardData.port_forward_data_1['action'] = "modify"
	portForwardData.port_forward_data_2['action'] = "modify"
	portForwardData.port_forward_data_3['action'] = "modify"

	portForward.main(portForwardData.port_forward_data_1, portForwardData.new_port_forward_data_1)
	time.sleep(sleepTime)
	portForward.main(portForwardData.port_forward_data_2, portForwardData.new_port_forward_data_2)
	time.sleep(sleepTime)
	portForward.main(portForwardData.port_forward_data_3, portForwardData.new_port_forward_data_3)


def delRule():
	portForwardData.new_port_forward_data_1['action'] = "del"
	portForwardData.new_port_forward_data_2['action'] = "del"
	portForwardData.new_port_forward_data_3['action'] = "del"

	portForwardData.new_port_forward_data_1['enable'] = "1"
	portForwardData.new_port_forward_data_2['enable'] = "1"
	portForwardData.new_port_forward_data_3['enable'] = "1"

	portForward.main(portForwardData.new_port_forward_data_1)
	time.sleep(sleepTime)
	portForward.main(portForwardData.new_port_forward_data_2)
	time.sleep(sleepTime)
	portForward.main(portForwardData.new_port_forward_data_3)

login.main(loginData.login_data_1)

#addRule()
#time.sleep(5)
#modifyRule()
#time.sleep(5)
delRule()





