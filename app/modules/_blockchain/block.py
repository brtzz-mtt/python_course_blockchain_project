from app.configuration import LOGGER
from app.modules.common import Timestamped

class Block(Timestamped):

    def __init__(self,
        transactions: list = [],
        index: int = 0,
        prev_hash: str = None,
    ) -> None:
        super().__init__()
        self.__transactions = transactions
        self.__index = index
        self.__prev_hash = prev_hash
        LOGGER.log_ok("created block with index '" + str(self.__index) + "' at " + self.get_timestamp())
