import datetime
import time

class Timestamped():

    def __init__(self) -> None:
        self.__unix_timestamp = time.time()

    def get_timestamp(self) -> str:
        return datetime.datetime.fromtimestamp(self.__unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')
