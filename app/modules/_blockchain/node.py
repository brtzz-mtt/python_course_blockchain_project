from app.configuration import BLOCKCHAIN, LOGGER
from app.modules.common import Timestamped
from app.modules._blockchain.account import Account

class Node(Timestamped):

    def __init__(self,
        address: str,
        account: Account,
        id: str
    ) -> None:
        super().__init__()
        self.__address = address
        self.__account = account
        self.__id = id
        LOGGER.log_ok("created node '" + self.__id + "' on address '" + self.__address + "' at " + self.get_timestamp())

    def get_account(self) -> str:
        return self.__account

    def get_address(self) -> str:
        return self.__address

    def get_data(self) -> object:
        return {
            'id': self.get_id(),
            'address': self.get_address(),
            'account_id': self.get_account().get_id(),
            'tokens': self.get_account().get_tokens(),
            'token_iso': BLOCKCHAIN.get_token_iso()
        }

    def get_id(self) -> str:
        return self.__id
