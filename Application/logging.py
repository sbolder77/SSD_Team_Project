class LoggingDetails:
    def __init__(self):
        self.test = "test"
        
    def logger(level, message):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    file_object = open('logfile.log', 'a')
    file_object.write(level + ',' + dt_string + ',' + message + '\n')
    file_object.close()