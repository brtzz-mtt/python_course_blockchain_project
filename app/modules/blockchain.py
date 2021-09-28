from app.configuration import LOGGER
from app.modules.common import Timestamped
from app.modules._blockchain.block import Block

class Blockchain(Timestamped):

    __blockchain = []

    def __init__(self,
        id: str
    ) -> None:
        super().__init__()
        self.__id = id
        LOGGER.log_ok("created blockchain '" + self.__id + "' at " + self.get_timestamp())
        self.append_block(Block()) # starting blockchain with genesis block

    def append_block(self,
        block: Block
    ) -> None:
        self.__blockchain.append(block)

    def get_id(self) -> str:
        return self.__id

    def get_last_block(self) -> Block:
        return self.__blockchain[-1]

    def get_length(self) -> int:
        return len(self.__blockchain)

    def get_token_iso(self) -> str:
        return self.__id[0:3].upper()
