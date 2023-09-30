import datetime
import system
from cryptography.fernet import Fernet

#region objects
s = system.settings()
syslog = 'systemlog.csv'
#endregion

class LoggingDetails:
    def __init__(self):
        pass
        
    def logger(logtype, level, message):
        if s.log == 'TRUE':
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            if logtype == "SYSTEM":
                file_object = open('systemlog.csv', 'a')
                file_object.write(level + ',' + dt_string + ',' + message + '\n')
                file_object.close()
            elif logtype == "USER":
                file_object = open('userlog.csv', 'a')
                file_object.write(level + ',' + dt_string + ',' + message + '\n')
                file_object.close()
            elif logtype == "ORDER":
                file_object = open('orderlog.csv', 'a')
                file_object.write(level + ',' + dt_string + ',' + message + '\n')
                file_object.close()
            elif logtype == "PRODUCT":
                file_object = open('productlog.csv', 'a')
                file_object.write(level + ',' + dt_string + ',' + message + '\n')
                file_object.close()

    def download_log(self, user, logtype):
        if user == 'A':
            if logtype == 'SYSTEM':
                return syslog
