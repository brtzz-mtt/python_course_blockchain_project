from app.cnf import LOGGER
from app.modules.common import Timestamped
from app.modules.utility import generate_md5_hash
from app.modules._blockchain.account import Account

class Node(Timestamped):

    def __init__(self,
        address: str,
        account: Account,
        id: str = generate_md5_hash()
    ) -> None:
        super().__init__()
        self.__address = address
        self.__account = account
        self.__id = id

        LOGGER.log_ok("created node '" + self.__id + "' at " + self.get_timestamp())

    def get_account(self) -> str:
        return self.__account

    def get_address(self) -> str:
        return self.__address

    def get_data(self) -> object:
        return {
            'id': self.get_id(),
            'address': self.get_address(),
            'account_id': self.get_account().get_id(),
            'tokens': self.get_account().get_tokens()
        }

    def get_id(self) -> str:
        return self.__id
