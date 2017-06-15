import sys 
sys.path.append('../../k2p_web_test')
from data import *
from src import *
import time



login.main(loginData.login_data)

#dmz.main(dmzData.dmz_data_1)
#upnp.main(upnpData.upnp_data_1)
#networkset.main(networksetData.networkset_data_1)
backupRestore.main(backupRestoreData.backupRestore_data_1)
#changeUserPwd.main(changeUserPwdData.changeUserPwd_data_2)
#time.sleep(adapter.rebootTime)
#guide.main(guideData.guide_data_1)
diagnose.main()
time.sleep(15)
adapter.closeDriver()
