from .blockchain import Blockchain
from .common import Timestamped

class Contract(Timestamped):

    def __init__(self,
        id: str,
        blockchain = Blockchain
    ) -> None:
        super().__init__()
        self.__id = id
        self.__blockchain = blockchain

    def get_blockchain(self) -> Blockchain:
        return self.__blockchain
    
    def get_id(self) -> str:
        return self.__id
