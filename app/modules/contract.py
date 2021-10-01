import random

from app.configuration import LOGGER
from app.modules.blockchain import Blockchain
from app.modules.common import Timestamped
from app.modules._blockchain.account import Account
from app.modules._blockchain.block import Block
from app.modules._blockchain.transaction import Transaction

class Contract(Timestamped):

    def __init__(self,
        id: str,
        blockchain = Blockchain
    ) -> None:
        super().__init__()
        self.__id = id
        self.__blockchain = blockchain
        LOGGER.log_ok("created contract '" + self.__id + "' at " + self.get_timestamp())

    def assign_reward(self,
        account: Account,
        modifier: int = 0
    ) -> float or False:
        modifier =+ 1
        mining_reward = modifier * self.__blockchain.get_mining_reward() + random.randint(0, modifier)
        self.__blockchain.add_transaction(Transaction(None, account.get_id(), {'mod_tokens': mining_reward}))
        if self.mine():
            LOGGER.log_ok("account '" + account.get_id() + "' was rewarded with " + str(mining_reward) + " " + self.__blockchain.get_token_iso())
            return account.mod_tokens(mining_reward)
        return False

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
        for i in range(len(blockchain) - 1):
            if blockchain[i].get_hash() != blockchain[i + 1].get_previous_hash():
                break
        if i:
            self.__blockchain.set_blockchain(blockchain[0, i + 1])
        return self.__blockchain.get_last_block().get_hash()

    def proof_block(self,
        block: Block,
        hash: str
    ) -> bool:
        return hash == block.generate_hash()

    def transfer_tokens(self,
        sender_account: Account,
        receiver_account: Account,
        amount: float
    ) -> bool:
        if not amount:
            return False
        self.__blockchain.add_transaction(Transaction(sender_account.get_id(), receiver_account.get_id(), {'mod_tokens': amount}))
        sender_account.mod_tokens(-amount)
        receiver_account.mod_tokens(amount)
        LOGGER.log_ok("an amount of " + str(amount) + " " + self.__blockchain.get_token_iso() + " was transfered from account '" + sender_account.get_id() + "' to account '" + receiver_account.get_id() + "'")
        return True
