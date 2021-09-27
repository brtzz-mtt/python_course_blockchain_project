from app.modules._blockchain.account import Account

class Player(Account):

    def __init__(self,
        name: str,
        color: str = 'white'
    ) -> None:
        self.__name = name
        self.__color = color
        super().__init__(self.__name)

    def get_data(self) -> object:
        return {
            'name': self.get_name(),
            'color': self.get_color(),
            'tokens': self.get_tokens()
        }

    def get_color(self) -> str:
        return self.__color

    def get_name(self) -> str:
        return self.__name
