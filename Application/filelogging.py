"""https://www.freecodecamp.org/news/python-copy-file-copying-files-to-another-directory/"""

#Importing necessary modules
from datetime import datetime
import shutil
import system

#Region objects
s = system.Settings()
DT_NOW = datetime.now()
DT_STR = DT_NOW.strftime("%d/%m/%Y %H:%M:%S")

class LoggingDetails:
    """Defining LoggingDetails() class and downstream functions"""
    def __init__(self):
        pass

    def write_system_log(self, logtype, level, message, user):
        """Defining writing system log function"""
        if ((s.log == 'TRUE') and (logtype == "SYSTEM")):
            file_object = open('systemlog.csv', 'a')
            file_object.write(level + ',' + DT_STR + ',' + message + ',' + user + '\n')
            file_object.close()
            return "log file updated"

    def download_log(self, user, dt, logtype):
        """Defining download log function"""
        DT_STR = DT_NOW.strftime("%d/%m/%Y %H:%M:%S")
        if user == 'A':
            if logtype == 'SYSTEM':
                shutil.copyfile('systemlog.csv', './Downloads/' + 'syslog' + dt + '.csv')
                return "System log file downloaded"
            return "System log file not downloaded"
