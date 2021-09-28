import os

DEBUG_MODE = False

BASE_PATH = os.path.dirname(__file__) + '/'

with open(BASE_PATH + '../log.md') as log_file:
    VERSION = log_file.readline().strip()

with open(BASE_PATH + '../README.md') as readme_file:
    BASE_TITLE = readme_file.readline().strip() + " v" + VERSION
    for line in readme_file:
        pass
    COPYRIGHT = line

from app.modules.logger import Logger

LOGGER = Logger(BASE_PATH + '../app.log', False, DEBUG_MODE)

from app.modules.blockchain import Blockchain

BLOCKCHAIN = Blockchain(BASE_TITLE)

from app.modules.contract import Contract

CONTRACT = Contract(BLOCKCHAIN)
