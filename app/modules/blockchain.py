from app.cnf import LOGGER
from app.modules.common import Timestamped
from app.modules.utility import generate_md5_hash
from app.modules._blockchain.block import Block

class Blockchain(Timestamped):

    __blockchain = []

    def __init__(self,
        id: str = generate_md5_hash()
    ) -> None:
        super().__init__()
        self.__id = id

        LOGGER.log_ok("created blockchain '" + self.__id + "' at " + self.get_timestamp())

    def append_block(self,
        block: Block
    ) -> None:
        self.__blockchain.append(block)

    def get_id(self) -> str:
        return self.__id

