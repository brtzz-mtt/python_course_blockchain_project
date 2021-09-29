import json

from flask import Flask, request
from markdown import markdown
from operator import itemgetter
from pprint import pprint # for debug purposes..

from app.configuration import BASE_TITLE, BLOCKCHAIN, DEBUG_MODE, LOGGER
from app.functions import decorate, render
from app.gaming import update_status
from app.simulation import NODES, PLAYERS, STATUS # initial conditions, auto-generated # TBD initialization controls

app = Flask(__name__)

@app.route('/')
def index():
    return render()

@app.route('/license')
def license():
    file = open('gpl.md', 'r')
    html = markdown(file.read())
    return render('html.html', BASE_TITLE + " | License", {'html': html})

@app.route('/readme')
def readme():
    file = open('README.md', 'r')
    html = markdown(file.read())
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
#    return render('html.html', BASE_TITLE + " | Documentation", {'html': html})

@app.route('/report')
def report():
    return render('index.html', BASE_TITLE + " | Report") # TBD implement this

@app.errorhandler(404)
def error_handler_404(error):
    return render('layout/empty.html', BASE_TITLE + " | Error", error), 404

@app.route('/log/get')
def log_get():
    LOGGER.log("flask log_get handle called")
    return json.dumps(LOGGER.get_log())

@app.route('/blockchain/get/length')
def blockchain_get_length():
    LOGGER.log("flask blockchain_get_length handle called")
    return json.dumps(len(BLOCKCHAIN.get_blockchain()))

@app.route('/contract/mine',
    methods = ['GET', 'POST']
)
def contract_mine():
    LOGGER.log("request to mine from node ''") # TBD
    return json.dumps() # TBD

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
            data.append(PLAYERS[key].get_data())
        return json.dumps(sorted(data,
            key = itemgetter('tokens'),
            reverse = True
        ))

@app.route('/status/get')
def status_get():
    LOGGER.log("flask status_get handle called")
    update_status()
    return json.dumps(STATUS)

if __name__ == '__main__':
    #pprint(vars(app)) # DBG
    app.run(debug = DEBUG_MODE)