import random

from app.configuration import BLOCKCHAIN
from app.modules.player import Player
from app.modules.utility import generate_md5_hash
from app.modules._blockchain.account import Account
from app.modules._blockchain.node import Node

NODES = {}
for i in range(100):
    account = Account.create((generate_md5_hash(str(i))))
    node = Node('127.0.0.1:' + str(5001 + i),
        account,
        generate_md5_hash(str(i)),
        BLOCKCHAIN # registering node for the blockchain
    )
    node.get_account().set_tokens(0)#random.randint(5, 10)) # DBG
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
    node = Node('127.0.0.1:' + str(5000 + len(NODES) + players.index(player)),
        account,
        player['name'],
        BLOCKCHAIN # registering player's node for the blockchain
    )
    node.get_account().set_tokens(1)#random.randint(5, 10)) # DBG
    PLAYERS[node.get_id()] = node

DIRECTIONS = {
    'N': [0, -1],
    'NNE': [.333, -.667],
    'NE': [.5, -.5],
    'NEE': [.667, -.333],
    'E': [1, 0],
    'SEE': [.667, .333],
    'SE': [.5, .5],
    'SSE': [.333, .667],
    'S': [0, 1],
    'SSW': [-.333, .666],
    'SW': [-.5, .5],
    'SWW': [-.666, .333],
    'W': [-1, 0],
    'NWW': [-.666, -.333],
    'NW': [-.5, -.5],
    'NNW': [-.333, -.666]
}
DIRECTION_KEYS = list(DIRECTIONS.keys())

STATUS = {}
for key in NODES:
    tokens = NODES[key].get_account().get_tokens()
    STATUS[key] = {
        'color': "grey",
        #'entropy': 0,
        #'attack': 0,
        #'defence': 0,
        #'speed': 0,
        'pos_x': random.randint(0, 100 - tokens),
        'pos_y': random.randint(0, 100 - tokens),
        'dir': random.choice(DIRECTION_KEYS),
        'tokens': tokens,
        'token_iso': BLOCKCHAIN.get_token_iso()
    }
for key in PLAYERS:
    player_account = PLAYERS[key].get_account()
    tokens = player_account.get_tokens()
    STATUS[key] = {
        'color': player_account.get_color(),
        'entropy': player_account.get_entropy(),
        'attack': player_account.get_attack(),
        'defence': player_account.get_defence(),
        'speed': player_account.get_speed(),
        'pos_x': random.randint(0, 100 - tokens),
        'pos_y': random.randint(0, 100 - tokens),
        'dir': random.choice(DIRECTION_KEYS),
        'tokens': tokens,
        'token_iso': BLOCKCHAIN.get_token_iso(),
        'auto_behaviour': player_account.get_auto_behaviour()
    }
