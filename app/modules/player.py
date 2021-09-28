from app.configuration import BLOCKCHAIN
from app.modules._blockchain.account import Account

class Player(Account):

    def __init__(self,
        name: str,
        color: str = 'white',
        entropy: int = 1,
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
            'name': self.get_name(),
            'color': self.get_color(),
            'entropy': self.get_entropy(),
            'speed': self.get_speed(),
            'attack': self.get_attack(),
            'defence': self.get_defence(),
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
