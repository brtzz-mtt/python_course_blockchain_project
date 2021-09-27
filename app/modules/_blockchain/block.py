from app.modules.common import Timestamped

class Block(Timestamped):

    def __init__(self,
        transactions: list,
        index: int = 0,
        prev_hash: str = None,
    ) -> None:
        super().__init__()
