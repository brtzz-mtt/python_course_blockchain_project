from app.cnf import LOGGER
from app.modules.common import Timestamped
from app.modules.utility import generate_md5_hash

class Account(Timestamped):

    __registry = {}

    def __init__(self,
        id: str = generate_md5_hash()
    ) -> None:
        super().__init__()
        self.__id = id
        self.__tokens = 0 # balance is null at creation

        LOGGER.log_ok("created account '" + self.__id + "' at " + self.get_timestamp())

    @classmethod
    def create(cls, # default instance creator, checks if an accoutn with same id already exists in registry
        id: str
    ) -> 'Account':
        try:
            return cls.__registry[id]
        except KeyError:
            new = cls(id)
            cls.__registry[id] = new
            return new

    def get_id(self) -> str:
        return self.__id

    def get_tokens(self) -> float:
        return self.__tokens
