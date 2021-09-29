from app.configuration import LOGGER
from app.modules.common import Timestamped

class Account(Timestamped):

    __registry = {}

    def __init__(self,
        id: str
    ) -> None:
        super().__init__()
        self.__id = id
        self.__tokens = 0 # balance is null at creation
        LOGGER.log_ok("created account '" + self.__id + "' at " + self.get_timestamp())

    def add_tokens(self,
        amount: float
    ) -> float:
        return self.set_tokens(self.__tokens + amount)

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

    def set_tokens(self,
        amount: float
    ) -> float:
        self.__tokens = amount
        return self.__tokens
