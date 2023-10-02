#https://www.freecodecamp.org/news/python-copy-file-copying-files-to-another-directory/

from datetime import datetime
import system
from cryptography.fernet import Fernet
import shutil

#region objects
s = system.settings()
#endregion

#region variables
syslog = 'systemlog.csv'
userlog = 'userlog.csv'
orderlog = 'orderlog.csv'
itemlog = 'itemlog.csv'
DT_NOW = datetime.now()

#endregion

class LoggingDetails:
    def __init__(self):
        pass
        
    def write_system_log(self, logtype, dt, level, message, user):
        if ((s.log == 'TRUE') and (logtype == "SYSTEM")):
            file_object = open('systemlog.csv', 'a')
            file_object.write(level + ',' + dt + ',' + message + ',' + user + '\n')
            file_object.close()
            return "log file updated"

    def write_user_log(self, logtype, dt, level, message, user):
        if ((s.log == 'TRUE') and (logtype == "USER")):
            file_object = open('userlog.csv', 'a')
            file_object.write(level + ',' + dt + ',' + message + ',' + user + '\n')
            file_object.close()
            #return "log file updated"
            
    def write_orders_log(self, logtype, dt, level, message, user):
        if ((s.log == 'TRUE') and (logtype == "ORDER")):
            file_object = open('orderlog.csv', 'a')
            file_object.write(level + ',' + dt + ',' + message + ',' + user + '\n')
            file_object.close()
            #return "log file updated"
            
    def write_item_log(self, logtype, dt, level, message, user):
        if ((s.log == 'TRUE') and (logtype == "ITEM")):
            file_object = open('itemlog.csv', 'a')
            file_object.write(level + ',' + dt + ',' + message + ',' + user + '\n')
            file_object.close()
            #return "log file updated"

    def download_log(self, user, dt, logtype):
        DT_STR = DT_NOW.strftime("%d/%m/%Y %H:%M:%S")
        if user == 'A':
            if logtype == 'SYSTEM':
                shutil.copyfile(syslog, './Downloads/' + syslog + dt + '.csv')
                return "System log file downloaded"
            else:
                return "System log file not downloaded"

