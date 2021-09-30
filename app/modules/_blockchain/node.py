from app.configuration import BLOCKCHAIN, LOGGER
from app.modules.blockchain import Blockchain
from app.modules.common import Timestamped
from app.modules._blockchain.account import Account
from app.modules._blockchain.block import Block

class Node(Timestamped):

    __blockchain_copy = []

    def __init__(self,
        address: str,
        account: Account,
        id: str,
        blockchain: Blockchain
    ) -> None:
        super().__init__()
        self.__address = address
        self.__account = account
        self.__id = id
        self.__blockchain = blockchain
        self.__blockchain_copy = blockchain.get_blockchain()
        LOGGER.log_ok("created node '" + self.__id + "' on address '" + self.__address + "' at " + self.get_timestamp())

    def append_block_to_own_blockchain(self,
        block: Block
    ) -> None:
        if self.__blockchain_copy[-1].get_hash() == block.get_previous_hash():
            self.__blockchain_copy.append(block)
        elif self.__blockchain_copy[-1].get_hash() == block.get_hash():
            self.__account.add_tokens(self.__blockchain.get_mining_reward())
        else:
            LOGGER.log_warn("blockchain copy of node '" + self.__id + "' seems broken")

    def get_account(self) -> str:
        return self.__account

    def get_address(self) -> str:
        return self.__address

    def get_blockchain(self) -> list:
        return self.__blockchain

    def get_data(self) -> object:
        return {
            'id': self.__id,
            'address': self.__address,
            'account_id': self.__account.get_id(),
            'tokens': self.__account.get_tokens(),
            'token_iso': BLOCKCHAIN.get_token_iso()
        }

    def get_id(self) -> str:
        return self.__id

    def set_blockchain(self,
        blockchain: Blockchain
    ) -> None:
        self.__blockchain = blockchain.get_blockchain()
