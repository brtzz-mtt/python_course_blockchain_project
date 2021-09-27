import datetime, time

class Logger():

    __DEBUG = 'debug'

    __log = []

    def __del__(self):
        self.__file.close()

    def __init__(self,
        file_path: str = __DEBUG + '.log',
        append_logs = True,
        debug = True
    ) -> None:
        self.__file_path = file_path
        self.__append_logs = append_logs
        self.__debug = debug
        try:
            self.__file = open(self.__file_path, ('w', 'a+')[self.__append_logs])
            self.log_ok("logging started correctly")
        except ValueError as e: # prevents application's crash if path/file not writable..
            print(e)

    def get_log(self,
        amount: None or int = None, # then return all and empty log list
    ) -> list:
        if amount and amount > 0:
            return self.__log[-amount]
        else:
            log = self.__log
            self.__log = []
            return log
    
    def log(self,
        message: str,
        level: str = __DEBUG
    ) -> None:
        if self.__debug or level != self.__DEBUG:
            now = datetime.datetime.now()
            message = now.strftime("%y-%m-%d @ %H:%M:%S") + "." + str(round(time.time() * 1000)) + " | " + level.upper() + " " + message#.lower() # DBG
            self.__log.append(message)
            self.__file.write(message + "\n")
            print(message)

    def log_error(self,
        message: str,
    ) -> None:
        self.log(message, 'error')

    def log_ok(self,
        message: str,
    ) -> None:
        self.log(message, 'ok')

    def log_warn(self,
        message: str,
    ) -> None:
        self.log(message, 'warn')
