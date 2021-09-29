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
        pending_transactions = self.__blockchain.get_pending_transactions()
        if not pending_transactions:
            LOGGER.log_warn("there are no pending transactions at the moment")
            return False
        else:
            last_block = self.__blockchain.get_last_block()
            block = Block(pending_transactions, last_block.get_index() + 1, last_block.get_hash())
            return self.__blockchain.append_block(block)

    def proof_blockchain(self) -> str:
        blockchain = self.__blockchain.get_blockchain()
        for i in range(0, len(blockchain) - 1):
            if blockchain[i].get_hash() != blockchain[i + 1].get_previous_hash():
                break
        self.self.__blockchain.set_blockchain(blockchain[0, i + 1])
        return self.__blockchain.get_last_block().get_hash()

    def proof_block(self,
        block: Block,
        hash: str
    ) -> bool:
        return hash == block.generate_hash()
