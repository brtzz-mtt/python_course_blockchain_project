from app.configuration import LOGGER
from app.modules.common import Timestamped
from app.modules._blockchain.block import Block
from app.modules._blockchain.transaction import Transaction

class Blockchain(Timestamped):

    __blockchain = []
    __pending_transactions = []

    def __init__(self,
        id: str
    ) -> None:
        super().__init__()
        self.__id = id
        LOGGER.log_ok("created blockchain '" + self.__id + "' at " + self.get_timestamp())
        self.append_block(Block()) # starting blockchain with genesis block

    def add_transaction(self,
        transaction: Transaction
    ) -> None:
        self.__pending_transactions.append(transaction)

    def append_block(self,
        block: Block
    ) -> bool:
        if block.get_previous_hash() \
        and self.get_last_block().get_hash() != block.get_previous_hash():
            LOGGER.log_error("new block's previous hash '" + block.get_previous_hash() + "' is not correct")
            return False
        elif block.get_hash() != block.generate_hash():
            LOGGER.log_error("new block's hash '" + block.get_hash() + "' doesn't match expected value")
            return False
        else:
            self.__blockchain.append(block)
            LOGGER.log_ok("a new block with hash '" + block.get_hash() + "' and '" + str(len(block.get_transactions())) + "' transactions was added to the blockchain at index '" + str(block.get_index()) + "'")
            return True

    def get_blockchain(self) -> list:
        return self.__blockchain

    def get_id(self) -> str:
        return self.__id

    def get_last_block(self) -> Block:
        return self.__blockchain[-1]

    def get_pending_transactions(self) -> list:
        return self.__pending_transactions

    def get_token_iso(self) -> str:
        return self.__id[0:3].upper()