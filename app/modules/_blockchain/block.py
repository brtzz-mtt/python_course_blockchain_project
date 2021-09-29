from app.configuration import LOGGER
from app.modules.common import Timestamped
from app.modules.utility import generate_sha256_hash

class Block(Timestamped):

    __hashing_difficulty = 3

    def __generate_hash(self) -> str:
        string = "{0} {1} {2} {3} {4}".format(
            self.get_timestamp(),
            self.__transactions,
            self.__index,
            self.__previous_hash,
            self.__nonce
        )
        return generate_sha256_hash(string)

    def __init__(self,
        transactions: list = [],
        index: int = 0,
        previous_hash: str = None,
    ) -> None:
        super().__init__()
        self.__transactions = transactions
        self.__index = index
        self.__previous_hash = previous_hash
        self.__hash = self.generate_hash()
        LOGGER.log_ok("created block with index '" + str(self.__index) + "' at " + self.get_timestamp())

    def generate_hash(self) -> str:
        self.__nonce = 0
        hash = self.__generate_hash()
        while not hash.startswith("0" * self.__hashing_difficulty):
            self.__nonce += 1
            hash = self.__generate_hash()
        return hash

    def get_hash(self) -> str:
        return self.__hash

    def get_index(self) -> str:
        return self.__index

    def get_previous_hash(self) -> str:
        return self.__previous_hash

    def get_transactions(self) -> list:
        return self.__transactions
