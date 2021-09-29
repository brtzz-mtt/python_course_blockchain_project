from app.configuration import LOGGER
from app.modules.common import Timestamped

class Transaction(Timestamped):

    def __init__(self,
        sender_id: str, # sender-account's id
        receiver_id: str, # receiver-account's id
        payload: dict # multi-purpose json object
    ) -> None:
        super().__init__()
        self.__sender_id = sender_id
        self.__receiver_id = receiver_id
        self.__payload = payload
        LOGGER.log_ok("created new transaction at " + self.get_timestamp())

    def get_payload(self) -> dict:
        return self.__payload

    def get_receiver_id(self) -> str:
        return self.__receiver_id

    def get_sender_id(self) -> str:
        return self.__sender_id
