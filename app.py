import json

from flask import Flask, request
from markdown import markdown
from pprint import pprint # for debug purposes..

from app.cnf import BASE_TITLE, DEBUG_MODE, LOGGER, NODES, PLAYERS

from app.functions import render

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

@app.route('/documentation')
def documentation():
    file = open('doc.md', 'r')
    html = markdown(file.read())
    return render('html.html', BASE_TITLE + " | Documentation", {'html': html})

@app.route('/report')
def report():
    return render('index.html', BASE_TITLE + " | Report") # TBD implement this

@app.errorhandler(404)
def error_handler_404(error):
    return render('layout/empty.html', BASE_TITLE + " | Error", error), 404

@app.route('/log/get'#,
    #methods = ['GET', 'POST']
)
def log_get():
    LOGGER.log("flask log_get handle called")
    return json.dumps(LOGGER.get_log())

@app.route('/node/get',
    defaults = {'id': None}
)
@app.route('/node/get/<id>')
def node_get(id):
    LOGGER.log("flask node_get handle called")
    if id in NODES:
        return NODES[id].get_data()
    else:
        data = []
        for key, value in NODES.items():
            data.append(value.get_data())
        return json.dumps(data)

@app.route('/player/get',
    defaults = {'id': None}
)
@app.route('/player/get/<id>')
def player_get(id):
    LOGGER.log("flask player_get handle called")
    if id in PLAYERS.keys():
        return PLAYERS[id].get_data()
    else:
        data = []
        for key, value in PLAYERS.items():
            data.append(value.get_data())
        return json.dumps(data)

if __name__ == '__main__':
    pprint(vars(app))
    app.run(debug = DEBUG_MODE)
