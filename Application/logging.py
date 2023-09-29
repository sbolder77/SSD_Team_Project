import datetime
import json

# create json readable object
filename = 'system.json'
f = open(filename)
data = json.load(f)

class LoggingDetails:
    def __init__(self):
        self.test = "test"
        
    def logger(logtype, level, message):
        for x in data:
            if x['log'] != 'TRUE':
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
