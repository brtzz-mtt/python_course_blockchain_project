import datetime, time

class Logger():

    __log = []

    def __del__(self):
        self.__file.close()

    def __init__(self,
        file_path: str = 'debug.log',
        append_logs = True
    ) -> None:
        self.__file_path = file_path
        try:
            self.__file = open(self.__file_path, ('w', 'a+')[append_logs])
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
        level: str = 'debug'
    ) -> None:
        now = datetime.datetime.now()
        message = now.strftime("%y-%m-%d @ %H:%M:%S") + "." + str(round(time.time() * 1000)) + " | " + level.upper() + " " + message.lower()
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
