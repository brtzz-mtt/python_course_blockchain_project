from app.configuration import BLOCKCHAIN
from app.modules._blockchain.account import Account

class Player(Account):

    def __init__(self,
        name: str,
        color: str = 'white',
        entropy: int = 3,
        attack: int = 1,
        defence: int = 1,
        speed: int = 1
    ) -> None:
        self.__name = name
        self.__color = color
        self.__entropy = entropy
        self.__attack = attack
        self.__defence = defence
        self.__speed = speed
        super().__init__(self.__name)

    def get_data(self) -> object:
        return {
            'name': self.__name,
            'color': self.__color,
            'entropy': self.__entropy,
            'attack': self.__attack,
            'defence': self.__defence,
            'speed': self.__speed,
            'tokens': self.get_tokens(),
            'token_iso': BLOCKCHAIN.get_token_iso()
        }
    
    def get_attack(self) -> int:
        return self.__attack

    def get_color(self) -> str:
        return self.__color

    def get_defence(self) -> int:
        return self.__defence

    def get_entropy(self) -> int:
        return self.__entropy

    def get_name(self) -> str:
        return self.__name

    def get_speed(self) -> int:
        return self.__speed
