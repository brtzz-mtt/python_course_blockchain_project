import random

from app.simulation import DIRECTIONS, DIRECTION_KEYS, NODES, PLAYERS, STATUS

def process_mining(entropy = 0): # experimental, for DBG
    return ((entropy + 1) * random.randint(1, 10)) / 1000

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
    for key in NODES:
        tokens = NODES[key].get_account().set_tokens(NODES[key].get_account().get_tokens() + process_mining())
        STATUS[key]['tokens'] = tokens
        result = process_movement(STATUS[key]['pos_x'], STATUS[key]['pos_y'], STATUS[key]['dir'], tokens)
        STATUS[key]['pos_x'] = result['pos_x']
        STATUS[key]['pos_y'] = result['pos_y']
        STATUS[key]['dir'] = result['dir']
    for key in PLAYERS:
        entropy = PLAYERS[key].get_entropy()
        STATUS[key]['entropy'] = entropy
        tokens = PLAYERS[key].set_tokens(PLAYERS[key].get_tokens() + process_mining(entropy))
        STATUS[key]['tokens'] = tokens
        attack = PLAYERS[key].get_attack()
        STATUS[key]['attack'] = attack
        defence = PLAYERS[key].get_defence()
        STATUS[key]['defence'] = defence
        speed = PLAYERS[key].get_speed()
        STATUS[key]['speed'] = speed
        result = process_movement(STATUS[key]['pos_x'], STATUS[key]['pos_y'], STATUS[key]['dir'], tokens, entropy, speed)
        STATUS[key]['pos_x'] = result['pos_x']
        STATUS[key]['pos_y'] = result['pos_y']
        STATUS[key]['dir'] = result['dir']
