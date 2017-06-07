# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   
# VERSION    :   1.0
# DESCRIPTION:   
#
# CREATE DATE:   
#
##############################################################
import sys 
#sys.path.append('../data')
sys.path.append('../../k2p_web_test')
#import login, networkset, adapter, backupRestore, changeUserPwd, guide
#import loginData, networksetData, backupRestoreData, changeUserPwdData, guideData
from data import *
from src import *
from api import *
import time



login.main(loginData.login_data_1)

#portForward.main(portForwardData.port_forward_data_3, portForwardData.new_port_forward_data_1)
#time.sleep(5)
#parentCtrl.main(parentCtrlData.pareCtrl_data_1)
dmz.main(dmzData.dmz_data_1)
#upnp.main(upnpData.upnp_data_1)
#networkset.main(networksetData.networkset_data_1)
#backupRestore.main(backupRestoreData.backupRestore_data_1)
#changeUserPwd.main(changeUserPwdData.changeUserPwd_data_1)
#adapter.closeDriver()
#time.sleep(adapter.rebootTime)
#guide.main(guideData.guide_data_1)
#diagnose.main()
time.sleep(5)
browser.closeDriver()
