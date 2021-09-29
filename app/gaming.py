import random

from app.configuration import BLOCKCHAIN, CONTRACT
from app.simulation import DIRECTIONS, DIRECTION_KEYS, NODES, PLAYERS, STATUS
from app.modules._blockchain.transaction import Transaction

def process_mining(entropy = 0):
    BLOCKCHAIN.add_transaction(Transaction('dummy_sender_id', 'dummy_receiver_id', {'dummy': "payload"})) # DBG
    if CONTRACT.mine():
        mining_factor = entropy + 1
        return mining_factor * BLOCKCHAIN.get_mining_reward() + random.randint(0, mining_factor) / 10 # random mining bonus
    return 0

def process_movement(
    pos_x,
    pos_y,
    dir,
    size,
    speed = 0,
    entropy = 0
) -> dict:
    speed_modifier = (speed + 1) / 10
    # new pos_x calculation
    pos_x = pos_x + speed_modifier * DIRECTIONS[dir][0]
    if pos_x <= 0:
        pos_x = 0
        dir = random.choice(DIRECTION_KEYS)
    elif pos_x > 100 - size:
        pos_x = 100 - size
        dir = random.choice(DIRECTION_KEYS)
    # new pos_y calculation
    pos_y = pos_y + speed_modifier * DIRECTIONS[dir][1]
    if pos_y <= 0:
        pos_y = 0
        dir = random.choice(DIRECTION_KEYS)
    elif pos_y > 100 - size:
        pos_y = 100 - size
        dir = random.choice(DIRECTION_KEYS)
    # new direction based on entropy
    if random.randint(0, 100) <= entropy:
        dir = random.choice(DIRECTION_KEYS)

    return {
        'pos_x': pos_x,
        'pos_y': pos_y,
        'dir': dir
    }

def update_status():
    global STATUS
    miner = random.choice(list(NODES.keys()) + list(PLAYERS.keys())) # simulates mining conditions, quite superficially
    #if not len(BLOCKCHAIN.get_blockchain()) % 10 and len(NODES): # ups.. c'ést la vie!
    #    random_node = random.choice(list(NODES.keys()))
    #    del NODES[random_node]
    #    del STATUS[random_node]
    for key in NODES:
        if key == miner:
            tokens = NODES[key].get_account().add_tokens(process_mining())
            STATUS[key]['tokens'] = tokens
        result = process_movement(STATUS[key]['pos_x'], STATUS[key]['pos_y'], STATUS[key]['dir'], STATUS[key]['tokens'])
        STATUS[key]['pos_x'] = result['pos_x']
        STATUS[key]['pos_y'] = result['pos_y']
        STATUS[key]['dir'] = result['dir']
    for key in PLAYERS:
        entropy = PLAYERS[key].get_entropy()
        STATUS[key]['entropy'] = entropy
        if key == miner:
            tokens = PLAYERS[key].add_tokens(process_mining(entropy))
            STATUS[key]['tokens'] = tokens
        attack = PLAYERS[key].get_attack()
        STATUS[key]['attack'] = attack
        defence = PLAYERS[key].get_defence()
        STATUS[key]['defence'] = defence
        speed = PLAYERS[key].get_speed()
        STATUS[key]['speed'] = speed
        result = process_movement(STATUS[key]['pos_x'], STATUS[key]['pos_y'], STATUS[key]['dir'], STATUS[key]['tokens'], entropy, speed)
        STATUS[key]['pos_x'] = result['pos_x']
        STATUS[key]['pos_y'] = result['pos_y']
        STATUS[key]['dir'] = result['dir']
