from app.configuration import LOGGER
from app.modules.blockchain import Blockchain
from app.modules.common import Timestamped
from app.modules._blockchain.block import Block

class Contract(Timestamped):

    def __init__(self,
        id: str,
        blockchain = Blockchain
    ) -> None:
        super().__init__()
        self.__id = id
        self.__blockchain = blockchain
        LOGGER.log_ok("created contract '" + self.__id + "' at " + self.get_timestamp())

    def get_blockchain(self) -> Blockchain:
        return self.__blockchain
    
    def get_id(self) -> str:
        return self.__id

    def mine(self) -> bool:
        blockchain = self.get_blockchain()
        pending_transactions = blockchain.get_pending_transactions()
        if not pending_transactions:
            LOGGER.log_warn("there are no pending transactions at the moment")
            return False
        else:
            last_block = blockchain.get_last_block()
            block = Block(pending_transactions, last_block.get_index() + 1, last_block.get_hash())
            return blockchain.append_block(block)
