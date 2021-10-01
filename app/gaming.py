import math, random

from app.configuration import BLOCKCHAIN, CONTRACT
from app.simulation import DIRECTIONS, DIRECTION_KEYS, NODES, PLAYERS, STATUS
from app.modules._blockchain.transaction import Transaction

def process_mining(entropy = 0):
    BLOCKCHAIN.add_transaction(Transaction('dummy_sender_id', 'dummy_receiver_id', {'dummy': "payload"})) # DBG
    if CONTRACT.mine():
        mining_factor = entropy + 1
        return mining_factor * BLOCKCHAIN.get_mining_reward() + random.randint(0, mining_factor) # random mining bonus
    return 0

def process_movement(
    pos_x,
    pos_y,
    dir,
    size,
    speed = 0,
    entropy = 0
) -> dict:
    speed_modifier = (speed + 1) / 60
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
    if random.randint(0, 100) <= entropy / 60:
        dir = random.choice(DIRECTION_KEYS)
    return {
        'pos_x': pos_x,
        'pos_y': pos_y,
        'dir': dir
    }

def process_behaviour(player, behaviour):
        tokens = player.get_tokens()
        power_up_attack_cost = player.get_attack() * 2
        power_up_defence_cost = player.get_defence() * 2
        power_up_speed_cost = player.get_speed() * 2
        if behaviour == 'ads':
            if tokens >= power_up_attack_cost:
                player.mod_tokens(-power_up_attack_cost)
                player.inc_attack()
            elif tokens >= power_up_defence_cost:
                player.mod_tokens(-power_up_defence_cost)
                player.inc_defence()
            elif tokens >= power_up_speed_cost:
                player.mod_tokens(-power_up_speed_cost)
                player.inc_speed()
        elif behaviour == 'asd':
            if tokens >= power_up_attack_cost:
                player.mod_tokens(-power_up_attack_cost)
                player.inc_attack()
            elif tokens >= power_up_speed_cost:
                player.mod_tokens(-power_up_speed_cost)
                player.inc_speed()
            elif tokens >= power_up_defence_cost:
                player.mod_tokens(-power_up_defence_cost)
                player.inc_defence()
        elif behaviour == 'dsa':
            if tokens >= power_up_defence_cost:
                player.mod_tokens(-power_up_defence_cost)
                player.inc_defence()
            elif tokens >= power_up_speed_cost:
                player.mod_tokens(-power_up_speed_cost)
                player.inc_speed()
            elif tokens >= power_up_attack_cost:
                player.mod_tokens(-power_up_attack_cost)
                player.inc_attack()
        elif behaviour == 'das':
            if tokens >= power_up_defence_cost:
                player.mod_tokens(-power_up_defence_cost)
                player.inc_defence()
            elif tokens >= power_up_attack_cost:
                player.mod_tokens(-power_up_attack_cost)
                player.inc_attack()
            elif tokens >= power_up_speed_cost:
                player.mod_tokens(-power_up_speed_cost)
                player.inc_speed()
        elif behaviour == 'sda':
            if tokens >= power_up_speed_cost:
                player.mod_tokens(-power_up_speed_cost)
                player.inc_speed()
            elif tokens >= power_up_defence_cost:
                player.mod_tokens(-power_up_defence_cost)
                player.inc_defence()
            elif tokens >= power_up_attack_cost:
                player.mod_tokens(-power_up_attack_cost)
                player.inc_attack()
        elif behaviour == 'sad':
            if tokens >= power_up_speed_cost:
                player.mod_tokens(-power_up_speed_cost)
                player.inc_speed()
            elif tokens >= power_up_attack_cost:
                player.mod_tokens(-power_up_attack_cost)
                player.inc_attack()
            elif tokens >= power_up_defence_cost:
                player.mod_tokens(-power_up_defence_cost)
                player.inc_defence()

def process_attacks():
    global NODES, PLAYERS, STATUS
    nodes = {**NODES, **PLAYERS}
    for key in nodes:
        distance = 100
        target = None
        for targets_key in nodes:
            if key != targets_key:
                diff_x = abs((STATUS[key]['pos_x'] + STATUS[key]['tokens'] / 4) - (STATUS[targets_key]['pos_x'] + STATUS[targets_key]['tokens'] / 4))
                diff_y = abs((STATUS[key]['pos_y'] + STATUS[key]['tokens'] / 4) - (STATUS[targets_key]['pos_y'] + STATUS[targets_key]['tokens'] / 4))
                dist = math.sqrt(diff_x**2 + diff_y**2)
                if distance >= dist:
                    distance = dist
                    target_key = targets_key
        amount = (STATUS[key]['attack'] - STATUS[target_key]['defence']) / 60
        if amount <= 0: # attack was unsuccessful
            continue
        if target_key in NODES:
             target = NODES[target_key]
        elif target_key in PLAYERS:
            target = PLAYERS[target_key]
        else:
            continue
        target.get_account().mod_tokens(-amount)
        if target.get_account().get_tokens() < 0: # target was killed
            del STATUS[target_key]
            if target_key in NODES:
                del NODES[target_key]
            elif target_key in PLAYERS:
                del PLAYERS[target_key]
        if key in NODES:
             aggressor = NODES[key]
        elif key in PLAYERS:
            aggressor = PLAYERS[key]
        else:
            continue
        aggressor.get_account().mod_tokens(amount)

def update_status():
    if len({**NODES, **PLAYERS}) == 1:
        return
    global STATUS
    miner = random.choice(list(NODES.keys()) + list(PLAYERS.keys())) # simulates mining conditions, quite superficially
    #if not len(BLOCKCHAIN.get_blockchain()) % 10 and len(NODES): # ups.. c'ést la vie!
    #    random_node = random.choice(list(NODES.keys()))
    #    del NODES[random_node]
    #    del STATUS[random_node]
    for key in NODES:
        if key == miner:
            tokens = NODES[key].get_account().mod_tokens(process_mining())
            STATUS[key]['tokens'] = tokens
        result = process_movement(STATUS[key]['pos_x'], STATUS[key]['pos_y'], STATUS[key]['dir'], STATUS[key]['tokens'])
        STATUS[key]['pos_x'] = result['pos_x']
        STATUS[key]['pos_y'] = result['pos_y']
        STATUS[key]['dir'] = result['dir']
    for key in PLAYERS:
        player_account = PLAYERS[key].get_account()
        entropy = player_account.get_entropy()
        STATUS[key]['entropy'] = entropy
        if key == miner:
            tokens = player_account.mod_tokens(process_mining(entropy))
            STATUS[key]['tokens'] = tokens
        attack = player_account.get_attack()
        STATUS[key]['attack'] = attack
        defence = player_account.get_defence()
        STATUS[key]['defence'] = defence
        speed = player_account.get_speed()
        STATUS[key]['speed'] = speed
        result = process_movement(STATUS[key]['pos_x'], STATUS[key]['pos_y'], STATUS[key]['dir'], STATUS[key]['tokens'], entropy, speed)
        STATUS[key]['pos_x'] = result['pos_x']
        STATUS[key]['pos_y'] = result['pos_y']
        STATUS[key]['dir'] = result['dir']
        process_behaviour(player_account, STATUS[key]['auto_behaviour'])
    if len(BLOCKCHAIN.get_blockchain()) > 60:
        process_attacks()
    return STATUS
