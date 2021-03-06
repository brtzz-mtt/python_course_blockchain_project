import json

from flask import Flask, make_response, request
from markdown import markdown
from operator import itemgetter
from pprint import pprint # for debug purposes..

from app.configuration import BASE_TITLE, BLOCKCHAIN, CONTRACT, DEBUG_MODE, LOGGER
from app.functions import render
from app.gaming import update_status
from app.simulation import NODES, PLAYERS, STATUS # initial conditions, auto-generated # TBD initialization controls
from app.modules._blockchain.transaction import Transaction

app = Flask(__name__)

@app.route('/')
def index():
    text = ''
    index = 1
    file = open('README.md', 'r')
    with file as readme_file:
        for line in readme_file:
            if index > 10:
                text += line + "\n"
            index += 1
    html = markdown(text)
    file.close()
    return render(args = {
        'html': html
    })

@app.route('/restart') # DBG
def restart():
    #app.run(debug = DEBUG_MODE)
    return render()

@app.route('/license')
def license():
    file = open('gpl.md', 'r')
    html = markdown(file.read())
    file.close()
    return render('html.html', BASE_TITLE + " | License", {'html': html})

@app.route('/readme')
def readme():
    file = open('README.md', 'r')
    html = markdown(file.read())
    file.close()
    return render('html.html', None, {'html': html})

@app.route('/changelog')
def changelog():
    file = open('log.md', 'r')
    html = markdown(file.read())
    return render('html.html', BASE_TITLE + " | Changelog", {'html': html})

#@app.route('/documentation') # deprecated
#def documentation():
#    file = open('doc.md', 'r')
#    html = markdown(file.read())
#    file.close()
#    return render('html.html', BASE_TITLE + " | Documentation", {'html': html})

@app.route('/report')
def report():
    return render('index.html', BASE_TITLE + " | Report") # TBD implement this, frontend too..

@app.errorhandler(404)
def error_handler_404(error):
    return render('layout/empty.html', BASE_TITLE + " | Error", error), 404

@app.route('/log/get')
def log_get():
    LOGGER.log("flask log_get handle called")
    return json.dumps(LOGGER.get_log())

@app.route('/blockchain/get')
def blockchain_get():
    LOGGER.log("flask blockchain_get handle called")
    return BLOCKCHAIN.get_blockchain_to_json()

@app.route('/blockchain/get/length')
def blockchain_get_length():
    LOGGER.log("flask blockchain_get_length handle called")
    return json.dumps({
        'blockchain_length': len(BLOCKCHAIN.get_blockchain()),
        'total_transactions': BLOCKCHAIN.get_transactions_amount()
    })

@app.route('/blockchain/add/transaction',
    methods = ['GET', 'POST']
)
def blockchain_add_transaction():
    data = request.get_json()
    transaction = Transaction('dummy_sender_id', 'dummy_receiver_id', {'dummy': "payload"}) # DBG
    BLOCKCHAIN.add_transaction(transaction) # TBD
    LOGGER.log("adding new transaction by node ''") # TBD
    return True, 202

@app.route('/contract/mine',
    methods = ['GET', 'POST']
)
def contract_mine():
    data = request.get_json()
    #LOGGER.log("request to mine from node '" + data['node']['id'] + "' at address '" + data['node']['address'] + "'") # TBD
    if CONTRACT.mine():
        blockchain_length = len(BLOCKCHAIN.get_blockchain())
        last_block = BLOCKCHAIN.get_last_block()
        last_valid_hash = CONTRACT.proof_blockchain() # checking blockchain against consensus criteria
        if blockchain_length == len(BLOCKCHAIN.get_blockchain()) \
        and CONTRACT.proof_block(last_block, last_valid_hash):
            for key in NODES:
                NODES[key].append_block_to_own_blockchain(last_block)
            for key in PLAYERS:
                PLAYERS[key].append_block_to_own_blockchain(last_block)
            LOGGER.log_ok("block number '" + str(last_block.get_index()) + "' was mined")
    return True, 202

@app.route('/node/get',
    defaults = {'id': None}
)
@app.route('/node/get/<id>')
def node_get(id = None):
    LOGGER.log("flask node_get handle called")
    if id in NODES:
        return NODES[id].get_data()
    else:
        data = []
        for key in NODES:
            data.append(NODES[key].get_data())
        return json.dumps(sorted(data,
            key = itemgetter('tokens'),
            reverse = True
        ))

@app.route('/player/get',
    defaults = {'id': None}
)
@app.route('/player/get/<id>')
def player_get(id = None):
    LOGGER.log("flask player_get handle called")
    if id in PLAYERS.keys():
        return PLAYERS[id].get_data()
    else:
        data = []
        for key in PLAYERS:
            data.append(PLAYERS[key].get_account().get_data())
        return json.dumps(sorted(data,
            key = itemgetter('entropy'), # tokens
            reverse = True
        ))

@app.route('/status/get')
def status_get():
    LOGGER.log("flask status_get handle called")
    response = make_response(json.dumps(update_status()))
    response.mimetype = 'application/json'
    return response
    #return json.dumps(STATUS)

if __name__ == '__main__':
    #pprint(vars(app)) # DBG
    app.run(debug = DEBUG_MODE)
