import os

DEBUG_MODE = True

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

BLOCKCHAIN = Blockchain()

from app.modules.contract import Contract

CONTRACT = Contract(BLOCKCHAIN)

# initialization of data-pool

import time

from app.modules.player import Player
from app.modules.utility import generate_md5_hash
from app.modules._blockchain.account import Account
from app.modules._blockchain.node import Node

NODES = {}
for i in range(100):
    account = Account(generate_md5_hash(str(i)))
    node = Node('127.0.0.' + str(i), account, generate_md5_hash(str(i)))
    NODES[node.get_id()] = node

players = (
    {
        'name': "Mr. Gold",
        'color': "gold"
    }, {
        'name': "Mr. Blue Sky",
        'color': "skyblue"
    }, {
        'name': "Mr. Sandy",
        'color': "sandybrown"
    }, {
        'name': "Mr. Orange",
        'color': "orange"
    }, {
        'name': "Ms. Pinky",
        'color': "hotpink"
    }, {
        'name': "Mr. Smoke",
        'color': "whitesmoke"
    }
)

PLAYERS = {}
for player in players:
    account = Player(player['name'], player['color'])
    node = Node('127.0.0.' + str(255 - players.index(player)), account, player['name'])
    PLAYERS[node.get_id()] = node.get_account()
